import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports

class toggle(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.has_permissions(manage_messages=True)
    async def toggle(self,ctx): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if ctx.guild.id in conf.w_tog_on:
            conf.w_tog_on.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            await ctx.send("Okay, I won't react to the triggers in chat!")
        elif ctx.guild.id not in conf.w_tog_on:
            conf.w_tog_on.insert(0, ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            await ctx.send("Okay, I'll react to the triggers in chat!")
        else:
            await ctx.send("Hey so an error happened, i'll just leave a code for you to report! ERROR: 17: Returned ELSE, is this in a PM?")
    


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(toggle(bot))
