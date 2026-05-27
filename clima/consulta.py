import requests
import json

api_key = 'ae3f472126f64f8fabd150224262705'
link_api = 'http://api.weatherapi.com/v1/current.json'

parametros = {
    'key': api_key,
    'q': 'Sâo Paulo',
    'lang': 'pt'


}


dados = requests.get(link_api,params=parametros)

print(dados.status_code)