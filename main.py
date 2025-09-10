import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

#Computer generated pokemon
print("You will play against the computer")

# Generate a random pokemon by ID
random_id = random.randint(1, 1302)

# Get request to retrieve pokemon details with random id
pokemon2 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_id}/').json()

# Assign values from API
pokemon2_name = pokemon2['name']
pokemon2_ability = pokemon2['abilities'][0]['ability']['name']
pokemon2_height = pokemon2['height'] / 10
pokemon2_weight = pokemon2['weight'] / 10

# Display pokemon details from API
print("\nComputer's Pokémon:")
print(f"Name: {pokemon2_name.capitalize()}")
print(f"Ability: {pokemon2_ability.capitalize()}")
print(f"Height: {pokemon2_height} m")
print(f"Weight: {pokemon2_weight} kg")

#Start of game prompt
print("Start game? (y/n)")
choice = input().lower()
#if choice == 'y':
   # print("")