import requests
import json
from rich import print
from rich.panel import Panel


api_key = 'ae3f472126f64f8fabd150224262705'
link_apitime = 'http://api.weatherapi.com/v1/current.json'
link_apiprevisao = 'http://api.weatherapi.com/v1/forecast.json'


def visualizar_clima():
    cidade = input('Digite a Cidade/Estado que deseja ver as informações climaticas: ')
    parametros = {
        'key': api_key,
        'q': cidade,
        'lang': 'pt'
    }

    requisicao_api = requests.get(link_apitime,params=parametros)


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

        print(Panel(f'CIDADE: {info_clima["Cidade"]}\n'
        f'ESTADO: {info_clima["Estado"]}\n'
        f'TEMPERATURA: {info_clima["Temperatura"]}°C\n'
        f'CONDIÇÃO: {info_clima["Condicao"]}\n'
        f'UMIDADE: {info_clima["Umidade"]}%\n'
        f'VELOCIDADE DO VENTO: {info_clima["Vento"]} km/h\n'
        f'ÚLTIMA ATUALIZAÇÃO: {info_clima["Att"]}'))
        
    else:
        print('Requisiçao negada!')



def consultar_historico():
    with open('dados/tempo.json','r') as arq:
        conteudo = json.load(arq)
        
    for item in conteudo:
        print(
        Panel(
            f'CIDADE: {item["Cidade"]}\n'
            f'ESTADO: {item["Estado"]}\n'
            f'TEMPERATURA: {item["Temperatura"]}°C\n'
            f'CONDIÇÃO: {item["Condicao"]}\n'
            f'UMIDADE: {item["Umidade"]}%\n'
            f'VELOCIDADE DO VENTO: {item["Vento"]} km/h\n'
            f'ÚLTIMA ATUALIZAÇÃO: {item["Att"]}',

            title='HISTÓRICO CLIMÁTICO'
        )
    )
    
def proximos_dias():
    cidade = str(input('Digite a cidade: '))
    while True:
        dias = int(input('DIGITE A QUANTIDADE DE DIAS [1 A 14]: '))    # FAZER UM IF PRA MAIS DE 14 DIAS 
        if dias > 14:
            print('A PREVISÃO MAXIMA É DE 14 DIAS!')
        else:
            break
    
    parametros = {
        'key': api_key,
        'q' : cidade,
        'lang': 'pt',
        'days': dias
    }
    
    requisicao_api = requests.get(link_apiprevisao,params=parametros)
    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        
        previsão_limpa = [ ]
        
        for dia in dados['forecast']['forecastday']:
            info_dia = {
                'Dia': dia['date'],
                'TemperaturaMaxima': dia['day']['maxtemp_c'],
                'TemperaturaMinima': dia['day']['mintemp_c'],
                'TempeaturaMedia': dia['day']['avgtemp_c'],
                'VelocidadeVento': dia['day']['maxwind_kph'],
                'Condicao': dia['day']['condition']['text'],
                'ChanceChuva': dia['day']['daily_chance_of_rain']   
            }
            
            previsão_limpa.append(info_dia)
        
        with open('dados/previsao.json','w') as arq:
            json.dump(previsão_limpa,arq,ensure_ascii=False,indent=4)
        
        for item in previsão_limpa:
            print(
            Panel(
        f'DIA: {item["Dia"]}\n'
        f'TEMPERATURA MÁXIMA: {item["TemperaturaMaxima"]}°C\n'
        f'TEMPERATURA MÍNIMA: {item["TemperaturaMinima"]}°C\n'
        f'TEMPERATURA MÉDIA: {item["TempeaturaMedia"]}°C\n'
        f'VELOCIDADE DO VENTO: {item["VelocidadeVento"]} km/h\n'
        f'CONDIÇÃO: {item["Condicao"]}\n'
        f'CHANCE DE CHUVA: {item["ChanceChuva"]}%',
        title = f'Previsão Do Tempo {cidade}'
        )
)
        
            
    else:
        print('Requisição negada')
        print(requisicao_api.status_code)
      
def comparar_temperatura():
    with open('dados/tempo.json','r') as arq:
        conteudo = json.load(arq)
    maior = 0
    menor = float('inf')
        
    for item in conteudo:
        if item['Temperatura']> maior:
            maior = item['Temperatura']
            dados_maior = item
        if item['Temperatura'] < menor:
            menor = item['Temperatura']
            dados_menor = item
    
    
    print(Panel(f'Maior temperatura -> Cidade: {dados_maior["Cidade"]} | Temperatura: {dados_maior["Temperatura"]} | Dia e Hora: {dados_maior["Att"]} \nMenor temperatura -> Cidade: {dados_menor['Cidade']} | Temperatura: {dados_menor['Temperatura']} | Dia e Hora: {dados_menor['Att']}',title = 'COMPARATIVO DE TEMPERATURAS'))

      
      
def limpar_historico():
    with open('dados/tempo.json','w', encoding= 'utf-8') as arq:
        json.dump([],arq)
        
        
    print('HISTORICO APAGADO!')
        
        
        
