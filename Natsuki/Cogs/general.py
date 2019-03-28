import discord
from discord.ext import commands
#Imports


class General(commands.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @commands.command()
    async def testy(self,ctx):
        await ctx.send("Testing 123!!!")



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(General(bot))
