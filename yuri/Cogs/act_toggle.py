import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf 
#Imports


class act_toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.has_permissions(administrator=True)
    async def act1(self,ctx): 
        if ctx.guild.id in conf.act2:
            conf.act2.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            conf.act1.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode 
            await ctx.send("O-Oh... Wh-What just happened? I feel funny...")
        elif ctx.guild.id in conf.act1:
            await ctx.send("I'm already in my 'Act 1' mode. And I'd prefer if it stayed that way...")
        elif ctx.guild.id in conf.act1 and ctx.guild.id in conf.act2:
            await ctx.send("Ok. This is a bug. Please contact your Maid to fix this thanks bye. Report this, i don't know. (Also report that both acts are running at the same time)")
        else:
            await ctx.send("Ok. This is a bug. Please contact your Maid to fix this thanks bye. Report this, i don't know. (Also report that this is an ELSE statement)")


    @client.command()
    @client.has_permissions(administrator=True) #Cooldowns when
    async def act2(self,ctx): 
        if ctx.guild.id in conf.act1:
            conf.act1.remove(ctx.guild.id) #If the ID is already in act2 but we're trying to get back into act1 just remove it from act2
            conf.act2.insert(0, ctx.guild.id) #Inserting the ID into act1 so if that id matches the guild ID we run in act1 mode and not act2 mode 
            await ctx.send("Ha. Haha. HAHAHAHAHHAHAHA!!!!")
        elif ctx.guild.id in conf.act2:
            await ctx.send("Oh, you little cutie! I'm already in Act 2 mode! Ahaha!!")
        elif ctx.guild.id in conf.act1 and ctx.guild.id in conf.act2:
            await ctx.send("Ok. This is a bug. Please contact your Maid to fix this thanks bye. Report this, i don't know. Sorry about this. (Also report that both acts are running at the same time)")
        else:
            await ctx.send("Ok. This is a bug. Please contact your Maid to fix this thanks bye. Report this, i don't know. Sorry about this. (Also report that this is an ELSE statement)")


def setup(bot):
    bot.add_cog(act_toggle(bot))
