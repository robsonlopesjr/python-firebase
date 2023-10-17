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

# Buscar uma venda especifica ou todas as vendas (GET)

# 1) Trazer todos os dados das duas tabelas
requisicao = requests.get(f'{database_url}/.json')
print(requisicao)
dic_requisicao = requisicao.json()

print(dic_requisicao)
print(dic_requisicao["Produtos"])

# 2) Trazer todos os dados da tabela Vendas
requisicao = requests.get(f'{database_url}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()

print(dic_requisicao)

# 3) Buscar os dados da venda de um cliente
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']

    if cliente == 'Robson':
        requisicao = requests.get(f'{database_url}/Vendas/{id_venda}.json')
        print(requisicao)
        print(requisicao.json())
