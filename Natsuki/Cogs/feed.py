import discord, random, asyncio
from discord.ext import commands
#Imports


class General(commands.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @commands.command()
    async def feed(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("Hey! You wanted to ask me something so what is it?!")
        elif arg1 == "🍇":
            await ctx.send("Grape!")
        elif arg1 == "🍣":
            await ctx.send("Ah, this is a more familiar meal.")
        else:
            await ctx.send("Are you trying to kill me?? That's not food!")



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(General(bot))
