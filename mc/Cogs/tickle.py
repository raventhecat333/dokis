import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Tickle(client.Cog):

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.guild_only()
    async def tickle(self,ctx): 
        #laughs = ["Hehehehehe!~", "Ahahahaha!!", "*giggles*", "**PFFFT AHAHAHAHAHAHHAHAHAHHAHA!!!!!**", "Ehehe!~", "WAHAHAHAHAHA!!!~"]        
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        #await ctx.send(random.choice(laughs))
        await ctx.send("I'm not ticklish, please stop.")


def setup(bot):
    bot.add_cog(Tickle(bot))
