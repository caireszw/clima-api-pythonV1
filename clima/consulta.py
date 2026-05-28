import requests
import json

api_key = 'ae3f472126f64f8fabd150224262705'
link_api = 'http://api.weatherapi.com/v1/current.json'


def visualizar_clima():
    cidade = input('Digite a Cidade/Estado que deseja ver as informações climaticas: ')
    parametros = {
        'key': api_key,
        'q': cidade,
        'lang': 'pt'
    }

    requisicao_api = requests.get(link_api,params=parametros)


    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        info_clima = {
            'Cidade': dados['location']['name'],
            'Estado': dados['location']['region'],
            'Temperatura': dados['current']['temp_c'],
            'Condicao': dados['current']['condition']['text'],
            'Umidade': dados['current']['humidity'],
            'Vento': dados['current']['wind_kph'],
            'Att': dados['current']['last_updated']
        }

        with open('dados/tempo.json', 'r', encoding='utf-8') as arq:
            historico = json.load(arq)

        historico.append(info_clima)

        with open('dados/tempo.json', 'w', encoding='utf-8') as arq:
            json.dump(historico, arq, ensure_ascii=False, indent=4)

        print(
        f'CIDADE: {info_clima["Cidade"]}\n'
        f'ESTADO: {info_clima["Estado"]}\n'
        f'TEMPERATURA: {info_clima["Temperatura"]}°C\n'
        f'CONDIÇÃO: {info_clima["Condicao"]}\n'
        f'UMIDADE: {info_clima["Umidade"]}%\n'
        f'VELOCIDADE DO VENTO: {info_clima["Vento"]} km/h\n'
        f'ÚLTIMA ATUALIZAÇÃO: {info_clima["Att"]}'
        )

    else:
        print('Requisiçao negada!')



def consultar_historico():
    with open('dados/tempo.json','r') as arq:
        conteudo = json.load(arq)
        
    print(conteudo)