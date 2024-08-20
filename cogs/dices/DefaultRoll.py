import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import math
import re

from placeholders.apikeys import *

from random import randint

def remOperators(text):
    pattern = r'[+\-*\/%^()]'
    text_without_operators = re.sub(pattern, '', text)
    return text_without_operators

def rollDice(txt):
    try:
        values = remOperators(txt)
        values = values.split()
        results = []
        for i in values:
            if('d' in i):
                dice = i.split('d')
                num = 0
                if dice[0] == '':
                    num = randint(1, int(dice[1]))
                    results.append([i, str(num), str([num])])
                else:
                    diceOutput = []
                    for j in range(int(dice[0])):
                        diceOutput.append(randint(1, int(dice[1])))
                    num += sum(diceOutput)   
                    results.append([i, str(num), str(sorted(diceOutput))])
        operation = txt
        rolls = ""
        for i in range(len(results)):
            operation = operation.replace(results[i][0], results[i][1], 1)
            rolls += results[i][2]
        return rolls, eval(operation)
    except:
        return 0 

class DefaultRoll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="r", guild_ids=[serverId])
    async def roll(self, interaction: Interaction, message, modifier = 1):
        try:
            dices, result = rollDice(message)
            if(modifier == 1):
                await interaction.response.send_message(f"Request:`[{message}]` \nRoll:`{dices}` \nResult:`{result}`")
            else:
                if(',' in modifier):
                    modifier = modifier.replace(',', '.')
                await interaction.response.send_message(f"Request:`[({message}) * {modifier}]` \nRoll:`{dices}` \nResult:`{math.floor(result * float(modifier))}`")
        except:
            print("An error ocurred")

def setup(client):
    client.add_cog(DefaultRoll(client))