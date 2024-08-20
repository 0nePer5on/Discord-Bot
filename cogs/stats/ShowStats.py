import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import SlashOption
import json

from placeholders.apikeys import *
from placeholders.gameInfo import playerOp

fileName = "./data/stats.json"

class ShowStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="show_stat", guild_ids=[serverId])
    async def show(self, interaction: Interaction, opitions:str=SlashOption(name="player", choices=playerOp)):
        try:
            with open(fileName, "r") as f:
                temp = json.load(f)

            file = nextcord.File('images/' + opitions + '.jpg')
            embed = nextcord.Embed(title=opitions, color=0xADD8E6)
            embed.set_thumbnail(url="attachment://Damian.jpg")
            for stats in temp[opitions]:
                embed.add_field(name=stats, value=temp[opitions][stats], inline=False)
            await interaction.send(file=file, embed=embed)
        except:
            print("An error ocurred")

def setup(client):
    client.add_cog(ShowStats(client))