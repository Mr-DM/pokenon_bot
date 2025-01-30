import telebot 
import random
from config import token

from logic import Pokemon , Fighter

bot = telebot.TeleBot(token) 



@bot.message_handler(commands=['go'])
def go(message):
    random_power = random.randint(1, 3)
    if message.from_user.username not in Pokemon.pokemons.keys():
        if random_power == 1:
            pokemon = Pokemon(message.from_user.username)
        elif random_power == 2:
            pokemon = Fighter(message.from_user.username)

        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "You create your pokemon")

@bot.message_handler(commands=['attack'])
def pokemon_attack(message):
    if message.reply_to_message: 
        Pokemon1 = Pokemon.pokemons[message.from_user.username]
        Pokemon2 = Pokemon.pokemons[message.replay_to_message.from_user.username]
    
        bot.reply_to(message, Pokemon1.attack(Pokemon2))
    else:

        bot.reply_to(message.chat.id, "Command /attack need to replay message ")

@bot.message_handler(commands=["help"])
def help(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info( ))

@bot.message_handler(commands=["feed"])
def help(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.feed())
    
bot.infinity_polling(none_stop=True)

