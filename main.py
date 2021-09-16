import os
import discord
import requests
import json
import random

client = discord.Client()

sad_words = ['sad', 'triste', 'depressivo', 'depressão', 'depressed', 'suicidal', 'suicide', 'suicídio', 'tristeza', 'unhappy', 'infeliz', 'miserable']

start_encouragements = [
  'Be happy',
  'Hold on',
  'drink a beer',
  'drink a bear(?)'
]

#get the zen quotes fro an API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n-" + json_data[0]['a']
  return quote

#Alert went connect to the server
@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))

#Check if a message was sended an which rensponse it should give
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #respond hello when called
  if msg.startswith("$hello"):
    await message.channel.send("Hello!")

  #send an inspirational quote
  if message.content.startswith("$inspire"):
    await message.channel.send(get_quote())

  #encourage people when the send sad words
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(start_encouragements))
  
  
#TOKEN is a variable from an .env
client.run(os.environ['TOKEN'])
