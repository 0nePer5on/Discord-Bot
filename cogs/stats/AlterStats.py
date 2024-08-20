import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import SlashOption
import json

from placeholders.apikeys import *
from placeholders.gameInfo import *

fileName = "./data/stats.json"

class AlterStats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="alter_stat", guild_ids=[serverId])
    async def alter(self, interaction: Interaction, new_value, player:str=SlashOption(name='player', choices=playerOp), stat:str=SlashOption(name='stats', choices=statsOp)):
        try:
            with open(fileName, "r") as f:
                temp = json.load(f)
            temp[player][stat] = int(new_value)
            with open(fileName, "w") as f:
                json.dump(temp, f)
            await interaction.response.send_message("Valor alterado com sucesso")
        except:
            print("An error ocurred")

def setup(client):
    client.add_cog(AlterStats(client))