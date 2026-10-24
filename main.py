import requests
import random

def random_pokemon():
    pokemonID = random.randint(1,1351)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonID}"
    x = requests.get(url)
    return x.json()

def play_game():
    data = random_pokemon()
    if not data:
        return

    name = data['name'].lower()
    height = data['height']
    weight = data['weight']

    print("WHO IS THAT POKEMON?!")
    print(f"Height: {height}cm")
    print(f"Weight: {weight}kg")

    tries = 5

    while tries:
        print(f"="*30)
        user_answer = input(f'GUESS <Attempts: {tries}>: ').lower()
        
        if user_answer == name:
            print('You got the correct answer!')
            break
        else:
            tries -= 1
            if tries>0:
                print("wrong answer!")
            else:
                print(f"="*30)
                print(f"The answer is: {name}")
                print("Better luck next time!")

play_game()
