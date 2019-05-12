import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def invite(self,ctx): 
        e = discord.Embed(title="My invite link!", description="F-fine! I guess I can join someone else's server, too... but I probably won't like it!", colour=conf.norm)
        e.add_field(name="Here goes...", value="(Click here to invite me!)[https://discordapp.com/api/oauth2/authorize?client_id=436351740787294208&permissions=8&scope=bot]", inline=True)
        await ctx.send(embed=e)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Invite(bot))
