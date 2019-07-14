import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports

class toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

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
            await ctx.send("This command can't be used in PM's! Sorry.")
    


def setup(bot):
    bot.add_cog(toggle(bot))
