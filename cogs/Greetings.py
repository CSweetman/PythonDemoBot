import discord
import random
from discord.ext import commands

class Greetings(commands.Cog):     #inherit from commands.cog

    def __init__(self, client):     #references client in bot.py
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.Cog.listener()   #takes variable client from above, declarator saying that function are events
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server')

    
    #Commands
    #context is passed in automatically
    #Command piece of code when user tells bot to do something
    #parameters can change attribute of the command 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")
    
def setup(client):
    client.add_cog(Greetings(client))