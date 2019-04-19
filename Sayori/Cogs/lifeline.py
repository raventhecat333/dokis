import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Lifeline(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def lifeline(self,ctx): 
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send("Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255")

def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Lifeline(bot))

