import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '4ee2776381d0346292e7b4c8a26b4d5b'}
TRAINER_ID = 2587

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Икенат'