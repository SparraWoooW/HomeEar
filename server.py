{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "69c62092",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import tensorflow as tf\n",
    "import os\n",
    "import numpy as np\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "bf60feb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = tf.keras.models.load_model(\"densenet201v1.hdf5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "31da407d",
   "metadata": {},
   "outputs": [],
   "source": [
    "label = ('door_knock',\n",
    "         'doorbell',\n",
    "         'emergency_alarm ',\n",
    "         'kettle_clicking',\n",
    "         'kettle_running', \n",
    "         'kettle_whistling',\n",
    "         'microwave_beeping' ,\n",
    "         'microwave_running' ,\n",
    "         'telephone',\n",
    "         'wakeup_alarm',\n",
    "         'washing_machine',\n",
    "         'water_running')\n",
    "\n",
    "def print_prediction (x, db):\n",
    "    predicted_vector=model.predict(x)\n",
    "    predicted_proba=np.argmax(predicted_vector,axis=1)\n",
    "    if label[predicted_proba[0]] == label[0] or label[predicted_proba[0]] == label[1] or label[predicted_proba[0]] == label[2] or label[predicted_proba[0]] == label[9]:\n",
    "        #print(db)\n",
    "        return label[predicted_proba[0]]\n",
    "        #print(label[predicted_proba[0]])\n",
    "        #print(predicted_vector[0][predicted_proba[0]])\n",
    "        #print(predicted_vector[0])\n",
    "    elif predicted_vector[0][predicted_proba[0]] >= .50 and db > -30.0:\n",
    "        #print(db)\n",
    "        return label[predicted_proba[0]]\n",
    "        #print(predicted_vector[0][predicted_proba[0]])\n",
    "        #print(label[predicted_proba[0]])\n",
    "        #print(predicted_vector[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "94978cf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\", methods=[\"POST\"])\n",
    "def index():\n",
    "    #get feature\n",
    "    feature = np.array(request.json[\"feature\"])\n",
    "    dB = np.array(request.json[\"dB\"])\n",
    "    #make prediction\n",
    "    prediction = print_prediction(feature, dB)\n",
    "    #send in json format\n",
    "    return jsonify({\"prediction\": prediction})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "856f39a5",
   "metadata": {
    "scrolled": 1
   },
  
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cebaa4c0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
