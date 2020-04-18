# Carrega o Modelo

# Imports
import os
import numpy as np
from tensorflow.keras.models import model_from_json

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

# Carrega os arquivos do modelo
def init(): 
	json_file = open('model/model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights("model/model.h5")

	# Compila e Avalia o Modelo Carregado
	loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	return loaded_model