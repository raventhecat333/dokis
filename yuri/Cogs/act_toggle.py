import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Tickle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def act1(self,ctx): 
        if ctx.guild.id in conf.act2:
            conf.act2.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            conf.act1.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode 
            await ctx.send("Running in act1 mode")
        elif ctx.guild.id in conf.act1:
            await ctx.send("I'm already in act1 mode")
        else:
            conf.act1.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode
            await ctx.send("Running in act1 mode")


    @client.command()
    async def act2(self,ctx): 
        if ctx.guild.id in conf.act1:
            conf.act1.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            conf.act2.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode 
            await ctx.send("Running in act2 mode")
        elif ctx.guild.id in conf.act2:
            await ctx.send("I'm already in act2 mode")
        else:
            conf.act2.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode
            await ctx.send("Running in act2 mode")


def setup(bot):
    bot.add_cog(Tickle(bot))
