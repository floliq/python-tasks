import requests
import json
from typing import Dict, List


def get_data(url: str) -> Dict:
    """
    Функция получения данных после запроса
    """

    req = requests.get(url)
    data = json.loads(req.text)
    return data


def get_pilots(data: str) -> List:
    """
    функция получения пилотов
    """

    pilots_list = []
    for pilot in data:
        data = get_data(pilot)
        pilot_dict = dict()
        pilot_dict['name'] = data['result']['properties']['name']
        pilot_dict['height'] = data['result']['properties']['height']
        pilot_dict['mass'] = data['result']['properties']['mass']
        planet_data = get_data(data['result']['properties']['homeworld'])
        pilot_dict['homeworld'] = planet_data['result']['properties']['name']
        pilot_dict['homeworld_url'] = data['result']['properties']['homeworld']
        pilots_list.append(pilot_dict)
    return pilots_list


data = get_data('https://www.swapi.tech/api/starships/12')
result = dict()
result['name'] = data['result']['properties']['name']
result['starship_class'] = data['result']['properties']['starship_class']
result['max_atmosphering_speed'] = data['result']['properties']['max_atmosphering_speed']
result['pilots'] = get_pilots(data['result']['properties']['pilots'])
print(result)
with open('x-wing.json', 'w') as file:
    json.dump(result, file, indent=4)
