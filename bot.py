import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '.')
status = cycle(['Status 1', 'Status 2'])


#Events
@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

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


client.run()