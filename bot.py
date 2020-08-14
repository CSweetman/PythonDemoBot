import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

"""
#events are piece of code that runs when a specific action that has happened
@client.event   #takes variable client from above, declarator saying that function are events
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
"""


@client.event
async def on_ready():
    print("Bot is ready.")

#context is passed in automatically
#Command piece of code when user tells bot to do something
#parameters can change attribute of the command 
@client.command()   
async def ping(ctx):   
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=['8ball'])  #aliases
async def _8ball(ctx, *, question):     #asterick will take multiple arguments as 1.
    responses = ["It is certain.",
                 "It is decidely so.",
                 "Without a doubt",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply haze, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=5):         #Very basic way, will need to learn how to deal 0 or checking permissions
        await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None): #Asterick, all parameters after members and stacks up to reason
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None): #Asterick, all parameters after members and stacks up to reason
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):   #this member is different, cant mention them in the server. Will need name (why * is needed) 
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
client.run("")