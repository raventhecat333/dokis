import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Suggestions(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def suggest(self,ctx): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        e = discord.Embed(title="Wow! You wanna suggest something? Alrighty!",description="[Click here](https://forms.gle/beiyyP3F1BEsbuVF8) to go to the suggestions form!", color=conf.norm)
        await ctx.send(embed=e)

def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Suggestions(bot))
