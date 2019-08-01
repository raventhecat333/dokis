import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Act_check(client.Cog):

    def __init__(self, bot):
         self.b = bot

    #A test command to see if the "Act" function is working properly as intended

    @client.command()
    async def act(self,ctx):
        try:
            if ctx.guild.id not in conf.act2:
                await ctx.send("I'm on Act 1.")
            else:
                await ctx.send("I'm on Act 2.")
        except:
            await ctx.send("This command can not be used in PM's! Sorry.")


def setup(bot):
    bot.add_cog(Act_check(bot))
