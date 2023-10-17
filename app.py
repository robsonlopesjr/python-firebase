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

# Criar um produto (POST)
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

# Editar Venda
dados = {
    'cliente': 'Robson',
    'preco': 149.90,
    'produto': 'fone de ouvido'
}

requisicao = requests.patch(
    f'{database_url}/Vendas/-NgyvetfDRF71Ci_aWV_/.json',
    data=json.dumps(dados)
)

print(requisicao)
print(requisicao.text)
