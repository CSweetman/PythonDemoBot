import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready.")


"""
#events are piece of code that runs when a specific action that has happened
@client.event   #takes variable client from above, declarator saying that function are events
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
"""

client.run("")

