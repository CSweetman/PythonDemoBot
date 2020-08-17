import discord
from discord.ext import commands

def is_it_Nabe(ctx):
    return ctx.author.id == 650607052988874762

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
    @commands.has_permissions(manage_messages=True)     #Code to check for permissions and
    async def clear(self, ctx, amount : int):         #Very basic way, will need to learn how to deal 0 or checking permissions, : int is to specify an int
        await ctx.channel.purge(limit = amount)
    

    @commands.command()
    @commands.check(is_it_Nabe)
    async def at(self, ctx, member : discord.Member):
        await ctx.send(f"Hello {member.mention}, this special command is only for Nabe. I love you Nabe!")


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
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the amount of messages to clear")  
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions to clear messages.")   

    @at.error
    async def at_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not Nabe, stahp, STOPPU")



def setup(client):
    client.add_cog(Admin(client))