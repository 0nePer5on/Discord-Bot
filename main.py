import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

from placeholders.apikeys import *

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= '!', intents=intents)

@client.event
async def on_ready():
  print("Bot ready!")

initial_extensions = []

for file in os.listdir('./cogs'):
  for fileName in os.listdir('./cogs/' + file):
    if fileName.endswith('.py'):
      initial_extensions.append("cogs." + file + '.' + fileName[:-3])

if __name__ == '__main__':
  for extension in initial_extensions:
    client.load_extension(extension)

client.run(botToken)