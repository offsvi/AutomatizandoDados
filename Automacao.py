import pandas as pd
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)

data = pd.read_csv(url, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
data['total_length'] = data['sepal_length'] + data['petal_length']
data.to_csv('iris_transformed.csv', index=False)

# O programa baixa os dados, realiza tranformações neles e salva os resultados em um arquivo CSV. 