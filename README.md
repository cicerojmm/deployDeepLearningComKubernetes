#Deploy do modelo de Deep Learning (CNN) com Flask e Kubernetes

Exemplo de como realizar o deploy de um modelo de Deep Learning, neste caso um CNN (Convolutional Neural Network) com alta disponibilidade utilizando o Kubernetes.

- O modelo:
O modelo de exemplo se trata do MNIST, onde é utilizado os dados para treinar o modelo que possa reconhecer caracteres textuais digitados a mão.

- API Flask:
A API está escrita em Python com flask e contém um endpoint para realizar a predição de uma imagem que é passada como parâmetro.

- Kubernetes
É utilizado o Docker e o Kubernetes para colocar essa API em funcionamento, visando a alta disponiblidade e escalabilidade que o Kubernetes pode oferecer.
