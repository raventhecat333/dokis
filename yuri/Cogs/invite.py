import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def invite(self,ctx): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if ctx.guild.id in conf.act1:
            e = discord.Embed(title="My invite link!", description="Uuu, I don't know about this. W-What if they don't like me?", color=conf.norm)
            e.add_field(name="O-Oh, well... Here goes nothing...", value="https://discordbots.org/bot/436350586670153730", inline=True)
            await ctx.send(embed=e)
            
        elif ctx.guild.id in conf.act2:
            e = discord.Embed(title="My invite link!", description="Ahahaha! I suppose I could visit other servers, but you're all I need!", color=conf.norm)
            e.add_field(name="Still, here you are!", value="https://discordbots.org/bot/436350586670153730", inline=True)
            await ctx.send(embed=e)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Invite(bot))