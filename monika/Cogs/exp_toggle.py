import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Expermental_Commands(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def exp(self,ctx):
        if ctx.guild.id in conf.exp_on:
            e = discord.Embed(title="Are you sure you want to disable experimental commands that may not be completed?",color=conf.norm)
            await ctx.send(embed=e)
            def check(m):
                return m.author == ctx.message.author and m.channel == ctx.message.channel
            response_wait = await self.b.wait_for('message',check=check, timeout=300)
            msg2 = response_wait.content.split(' ')[0].lower()

            if msg2 == "yes":
                conf.exp_on.remove(ctx.guild.id) 
                e = discord.Embed(title="Ok! Experimental commands have been disabled.",color=conf.norm)
                await ctx.send(embed=e)
            elif msg2 == "no":
                e = discord.Embed(title="Ok! Experimental commands have not been disabled.",color=conf.err)
                await ctx.send(embed=e)


        elif ctx.guild.id not in conf.exp_on:
            e = discord.Embed(title="Are you sure you want to enable experimental commands that may not be completed?",color=conf.norm)
            await ctx.send(embed=e)
            def check(m):
                return m.author == ctx.message.author and m.channel == ctx.message.channel
            response_wait = await self.b.wait_for('message',check=check, timeout=300)
            msg2 = response_wait.content.split(' ')[0].lower()

            if msg2 == "yes":
                conf.exp_on.insert(0, ctx.guild.id) 
                e = discord.Embed(title="Ok! Experimental commands have been enabled.",color=conf.norm)
                await ctx.send(embed=e)
            elif msg2 == "no":
                e = discord.Embed(title="Ok! Experimental commands have not been enabled.",color=conf.err)
                await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Expermental_Commands(bot))
