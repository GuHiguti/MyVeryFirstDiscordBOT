import os
import discord
import requests
import json

client = discord.Client()

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
  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")
  if message.content.startswith("$inspire"):
    await message.channel.send(get_quote())
  
#TOKEN is a variable from an .env
client.run(os.environ['TOKEN'])
