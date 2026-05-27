import requests
import json

api_key = 'ae3f472126f64f8fabd150224262705'
link_api = 'http://api.weatherapi.com/v1/current.json'
cidade = input('Digite a cidade desejada: ')
parametros = {
    'key': api_key,
    'q': cidade,
    'lang': 'pt'


}

requisiçao_api = requests.get(link_api,params=parametros)


if requisiçao_api.status_code == 200:
    dados = requisiçao_api.json()
    with open('estudoapi/tempo.json','w') as arq:
        json.dump(dados,arq,ensure_ascii=False,indent=4)
    print('Requisição Concluida!')
    estado = dados['location']['region']
    cidade = dados['location']['name']
    condicao = dados['current']['condition']['text']
    temperatura = dados['current']['temp_c']
    att = dados['current']['last_updated']
    print(f'A cidade de {cidade} localizada no estado de {estado } está com {condicao}, na temperatura atual de {temperatura} [ULTIMA ATUALIZAÇÃO EM: {att}]')


else:
    print('Requisição falhou!')



