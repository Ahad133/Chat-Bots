import nextcord
from nextcrod import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '$' , intents=intents)

@client.event
async def on_ready():
    print("me ghareeb hu me chutya ho")



client.run('')