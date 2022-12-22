import requests

API_KEY = '5fc2318a1ec822456514c292542c613b'
cidade = "Itapecuru Mirim"

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

resposta = requests.get(link)
resposta_dic = resposta.json()

status = resposta_dic['weather'][0]['description']
temperaturaKelvin = resposta_dic['main']['temp']

temperatura = temperaturaKelvin - 273.15

print(int(temperatura), status)