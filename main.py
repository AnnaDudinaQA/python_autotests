import requests

token = '6dea5221ab2d24b9b2a23bcba235de2c'
host = 'https://api.pokemonbattle.ru/v2'
header = {'Content-Type'  :  'application/json',
               'trainer_token' : token }
body = { 
    "name": "Iliana",
    "photo_id": "5"
}

response = requests.post(url = f'{host}/pokemons', headers= header, json = body, verify=False)

json_response = response.json()

print(json_response["id"])

id = json_response["id"]

response_activation = requests.put ( f'{host}/pokemons', headers= header, json = {
    "pokemon_id": id,
    "name": "Gus",
    "photo_id": "5"
}, verify=False)

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', headers= header, json = {
    "pokemon_id": id,
}, verify=False )

print(response_pokeball.text)