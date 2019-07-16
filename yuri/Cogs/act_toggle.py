import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf 
#Imports


class act_toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.has_permissions(manage_messages=True) #Change this to "manage_messages"
    @client.guild_only()
    async def act1(self,ctx): 
        if ctx.guild.id in conf.act2:
            conf.act2.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            await ctx.send("O-Oh... Wh-What just happened? I feel funny...")
        elif ctx.guild.id not in conf.act2:
            await ctx.send("I'm already in my 'Act 1' mode. And I'd prefer if it stayed that way...")



    @client.command()
    @client.has_permissions(manage_messages=True) #Cooldowns when
    @client.guild_only()
    async def act2(self,ctx): 
        if ctx.guild.id not in conf.act2:
            conf.act2.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode 
            await ctx.send("Ha. Haha. HAHAHAHAHHAHAHA!!!!")
        elif ctx.guild.id in conf.act2:
            await ctx.send("Oh, you little cutie! I'm already in Act 2 mode! Ahaha!!")



def setup(bot):
    bot.add_cog(act_toggle(bot))
