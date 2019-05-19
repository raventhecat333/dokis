import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Tickle(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def tickle(self,ctx): 
        laughs = ["Ahahahaha!!", "Hehehehehe!", "N-Now, hold on! Th-This isn't right! Ahahaha!!", "Ehehehehehehe!!!"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(laughs))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Tickle(bot))
