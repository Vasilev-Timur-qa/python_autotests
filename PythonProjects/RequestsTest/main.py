import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '4ee2776381d0346292e7b4c8a26b4d5b'}
body_pokemons = {
    "name": "generate",
    "photo": "generate"
}
body_name = {
    "pokemon_id": "26477",
    "name": "shanghai zero",
    "photo": "generate"
}
body_add = {
    "pokemon_id": "26482"
}

'''response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_creation.text)'''

'''response_namechange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_namechange.text)'''

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_addpokeball.text)