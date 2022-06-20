import discord
import os
import requests
import json
from neuralintents import GenericAssistant

chatbot = GenericAssistant('Chat.json')
chatbot.train_model()
chatbot.save_model()


client = discord.Client()
@client.event
async def on_ready(message):
  print('aj to topi hogi')
   # await message.channel.send('asfar is gay')

@client.event
async  def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('geh'):
    await message.channel.send('asfar is gay')

  if message.content.startswith('geh'):
    await message.channel.send('asfar is gay')

  if message.content.startswith('lora'):
    await message.channel.send('chossna mera kaam')

  if message.content.startswith("%hey"):
    response = chatbot.request(message.content[3:])
  await message.channel.send(response)


client.run('OTg3Njk4ODExMjczMDg5MDQ0.GFvIQW.k6CHvs9p4QBI-ik_dtKxaa1F6huih4Gv1L--B8')
