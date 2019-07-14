import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def invite(self,ctx): 
        if ctx.guild is None:
            e3 = discord.Embed(title="My invite link!", description="Uuu, I don't know about this. W-What if they don't like me?", color=conf.norm)
            e3.add_field(name="O-Oh, well... Here goes nothing...", value="[Click here to invite me!](https://discordbots.org/bot/436350586670153730)", inline=True)
            await ctx.send(embed=e3)

        elif ctx.guild.id not in conf.act2:
            e1 = discord.Embed(title="My invite link!", description="Uuu, I don't know about this. W-What if they don't like me?", color=conf.norm)
            e1.add_field(name="O-Oh, well... Here goes nothing...", value="[Click here to invite me!](https://discordbots.org/bot/436350586670153730)", inline=True)
            await ctx.send(embed=e1)
            
        elif ctx.guild.id in conf.act2:
            e2 = discord.Embed(title="My invite link!", description="Ahahaha! I suppose I could visit other servers, but you're all I need!", color=conf.norm)
            e2.add_field(name="Still, here you are!", value="[Click here to invite me!](https://discordbots.org/bot/436350586670153730)", inline=True)
            await ctx.send(embed=e2)
        

def setup(bot):
    bot.add_cog(Invite(bot))
