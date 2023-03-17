import requests
message = input()
url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={message}&appid=e903c049b4d03dc6fa46a716693acb3f').json()
weather = url['main']['temp']

print(weather - 273.15)