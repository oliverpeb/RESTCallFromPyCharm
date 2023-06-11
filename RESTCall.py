import requests

def get_all_temperatures():
    response = requests.get('http://localhost:5025/temp')
    if response.status_code == 200:
        temperatures = response.json()
        for temperature in temperatures:
            print(temperature)
    else:
        print('Fejl: Kunne ikke hente temperaturmålinger')

def get_temperature_by_id(temperature_id):
    url = f'http://localhost:5025/temp/{temperature_id}'
    response = requests.get(url)
    if response.status_code == 200:
        temperature = response.json()
        print(temperature)
    else:
        print(f'Fejl: Kunne ikke hente temperaturmåling med id {temperature_id}')

def insert_temperature(temperature):
    url = 'http://localhost:5025/temp'
    response = requests.post(url, json=temperature)
    if response.status_code == 201:
        print('Temperaturmåling blev indsat succesfuldt')
    else:
        print('Fejl: Kunne ikke indsætte temperaturmåling')

get_all_temperatures()

get_temperature_by_id(1)

new_temperature = {
    'RoomNumber': '101',
    'Temperature': 25,
    'Day': 'Thursday'
}
insert_temperature(new_temperature)