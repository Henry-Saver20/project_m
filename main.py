import discord
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()




#Helper functions for the Project----------------------------------------------
def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    return(json_data['message'])





#----------------------------------------------------------------------------


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Yoooo whats up '  + str(message.author) + '!')

    if message.content.startswith('ayo what the dog doin'):
        dog = get_dog()
        await message.channel.send(str(message.author) + ' This is what the dog doin!! :)')
        await message.channel.send(dog)


client.run(os.getenv('TOKEN'))