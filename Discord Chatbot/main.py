import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant('Chat.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(""):
        response = chatbot.request((message.content[0:]))
        await message.channel.send(response)

client.run('OTg3Njk4ODExMjczMDg5MDQ0.GupQz7.lrgccX4_38ECzZf88J0Rlm9uxmGSMUD-Qq1v3I')