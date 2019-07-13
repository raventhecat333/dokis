import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Expermental_Commands(client.Cog):

    def __init__(self, bot):
         self.b = bot 
    '''
    @client.command()
    async def exp(self,ctx): 
        e = discord.Embed(title="Are you sure?", description="Are you sure you want to enable experimental commands that may not be completed?",color=conf.norm)
        await ctx.send(embed=e)
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        response_wait = await self.b.wait_for('message',check=check, timeout=300)
        msg2 = response_wait.content.split(' ')[0].lower()

        if msg2 == "yes":
            await ctx.send(f"Ok, experimental commands have been enabled.")
        elif msg2 == "no":
            await ctx.send(f"Ok, experimental commands have not been enabled.")
    ''' #Remember to finish this command.


def setup(bot):
    bot.add_cog(Expermental_Commands(bot))
