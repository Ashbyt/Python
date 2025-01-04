import requests
#https://openweathermap.org/api
api_key = ''
location = input('please enter the location to look up weather in: ')
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={location}')
print('here is the response:')
print(response.json())


