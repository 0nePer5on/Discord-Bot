import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import SlashOption

from placeholders.apikeys import *

choices = ['1', '2', '3']

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name='test' ,guild_ids=[serverId])
    async def choose_a_number(
        self,
        interaction: nextcord.Interaction,
        number: str = SlashOption(
            name="number",
            choices=choices,
        ),
    ):
        await interaction.response.send_message(f"You chose {number}!")


def setup(client):
    client.add_cog(Test(client))