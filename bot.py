import discord
import os 
import requests
import json


client = discord.Client()


def get_quote():
  responses = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(responses.text)
  quote = json_data[0] ['q']
  return(quote)
  

@client.event
async def on_ready():
  print('aj to topi hogi')
  
@client.event
async  def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('geh'):
    await message.channel.send('asfar is gay')
   
    if message.content.startswith('insp'):
      quote = get_quote()
    await message.channel.send('quote')


client.run('Token')
