import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def invite(self,ctx): 
        e = discord.Embed(title="My invite link!", description="Oh, you would like to add me to a new server? You can get my link below!", colour=conf.norm)
        e.add_field(name="Here it is!", value="[Click here to invite me!](https://discordbots.org/bot/436351740787294208)", inline=True)
        await ctx.send(embed=e)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Invite(bot))
