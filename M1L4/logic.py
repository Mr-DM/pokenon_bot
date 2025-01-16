from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = 20
        self.power = 4 

        Pokemon.pokemons[pokemon_trainer] = self


    def attack(self, enemy):
        enemy.hp -= self.power
        if enemy.hp > 0:
            return f"Enemy HP: {enemy.hp}"
        else:
            return "It lose"
        
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Name your pokemon: {self.name} Strong: {self.power} Health: {self.hp}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Fighter(Pokemon):
    def attack(self, enemy):
        self.power += 5 
        result = super().attack(enemy)
        self.power -= 5
        return result
    def info(self):
        return f"Name your Fighter pokemon: {self.name} Strong: {self.power} Health: {self.hp}"

class Wizard(Pokemon):
    def attack(self, enemy):
        self.hp += 5
        result = super().attack(enemy)
        self.hp -= 5
        return result
    def info(self):
        return f"Name your Wizard pokemon: {self.name} Strong: {self.power} Health: {self.hp}"

if __name__ == "__main__":
    Pokemon1 = Pokemon("")
    Pokemon2 = Pokemon("")
    print(Pokemon1.attack(Pokemon2))
