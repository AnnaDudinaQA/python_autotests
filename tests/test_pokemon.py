import requests
import pytest

token = '6dea5221ab2d24b9b2a23bcba235de2c'
host = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type'  :  'application/json',
               'trainer_token' : token }


def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 7473})
    assert  respons.status_code == 200 

def test_trainer_name_in_response():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 7473})
    assert  respons.json()['data'][0]['trainer_name'] == 'Аннушка'