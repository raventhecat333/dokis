import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Swears(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def swear(self,ctx): 
        swear_list = ["HECK!", "DARN IT!", "POOP!", "CRUD!", "FRICK!", "SON OF A BISCUIT!", "MOTHERTRUCKER!"]        
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(swear_list))


def setup(bot):
    bot.add_cog(Swears(bot))
