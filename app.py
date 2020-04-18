# Web App Para Previsão de Dígitos

# Imports
from flask import Flask, request, jsonify
import imageio
import cv2
import numpy as np
import tensorflow as tf
import re
import base64
import sys 
import os

# Carrega o nosso modulo de load do modelo
sys.path.append(os.path.abspath("model"))
from load import * 

app = Flask(__name__)

global model
model = init()

# Converte a imagem para png
def convertImage(img_data):
	img_str = re.search('base64,(.*)', img_data).group(1)
	with open('output.png','wb') as output:
		output.write(base64.b64decode(img_str))
	
# Endpoint de teste
@app.route('/')
def index():
	return "API para identificar digitos escrito a mão com Deep Learning."

#Endpoint para predição
@app.route('/predict', methods=['GET'])
def predict():
	imgData = request.args.get('imagem')
	
	# Converter imagem para poder utilizar no modelo
	convertImage(imgData)
	
	# Carrega a imagem na memória
	x = imageio.imread('output.png', pilmode='L')
	
	# Calcula uma inversão bit-wise
	# Basicamente inversão de cores
	x = np.invert(x)
	
	# Redimensiona a imagem para o tamanho que o modelo espera
	x = cv2.resize(x,(28,28))

	# Converte para array de 4d
	x = x.reshape(1,28,28,1)
	
	# faz a predicao com o modelo carregado
	out = model.predict(x)
	# Converte a resposta em uma string
	output = np.argmax(out,axis=1)
	response = {'valor': str(output[0])}
	return response, 200

	return 'bad request', 400

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
