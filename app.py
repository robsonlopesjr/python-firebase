import requests
import json
from decouple import config

database_url = config('urldb')

# Criar uma venda (POST)
dados = {
    'cliente': 'Junior',
    'preco': 150,
    'produto': 'teclado'
}

requisicao = requests.post(
    f'{database_url}/Vendas/.json',
    data=json.dumps(dados)
)

print(requisicao)
print(requisicao.text)

# # Criar um produto (POST)
dados = {
    'nome': 'teclado',
    'preco': 150,
    'quantidade': 80
}

requisicao = requests.post(
    f'{database_url}/Produtos/.json',
    data=json.dumps(dados)
)

print(requisicao)
print(requisicao.text)
