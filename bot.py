import discord
import os
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

#cogs: Organize code/classes to divide commands and events to different files
@client.command()
async def load(ctx, extension): #extension is the cog that is going to be loaded
    client.load_extension(f"cogs.{extension}")         #loads the extension, cogs.extension goes into the cogs folder and look at cog

@client.command()
async def unload(ctx, extension): #unloads the extension
    client.unload_extension(f"cogs.{extension}")   

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")   
    client.load_extension(f"cogs.{extension}") 

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

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