import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    """
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all required arguments.")
    """
    @commands.command()
    async def clear(self, ctx, amount : int):         #Very basic way, will need to learn how to deal 0 or checking permissions, : int is to specify an int
        await ctx.channel.purge(limit = amount)

    @commands.command()
    async def at(self, ctx, member : discord.Member):
        await ctx.send(f"Hello {member.mention}")


    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None): #Asterick, all parameters after members and stacks up to reason
        await member.kick(reason = reason)


    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None): #Asterick, all parameters after members and stacks up to reason
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention}")
    
    @commands.command()
    async def unban(self, ctx, *, member):   #this member is different, cant mention them in the server. Will need name (why * is needed) 
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
    
        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return
    
    @clear.error
    async def load_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the amount of messages to clear")    



def setup(client):
    client.add_cog(Admin(client))