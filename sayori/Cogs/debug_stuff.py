import discord, random, Cogs.checks, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports

checks = Cogs.checks
class Debug(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    #A test command to see if the "Act" function is working properly as intended

    @checks.dev()
    @client.command(enabled=True)
    async def debug(self,ctx):
        e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
Discord.py Version: {discord.__version__}
Python Version: {sys.version}
''',color=0x36393f)
        e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)

        if ctx.guild.id in conf.w_tog_off:
            e2 = discord.Embed(title=f'''Does Guild use chat triggers: Yes
''',color=0x36393f)
        else:
            e2 = discord.Embed(title=f'''Does Guild use chat triggers: No
''',color=0x36393f)        

        if conf.sharding is True:
            e3 = discord.Embed(title=f'''Number of Shard's: {len(self.b.shard_ids)}
Total Guilds: {len(self.b.guilds)}
''',color=0x36393f)
        else:
            pass

        e4 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
''',color=0x36393f)

        await ctx.send(embed=e)
        await ctx.send(embed=e2)
        if conf.sharding is True:
            await ctx.send(embed=e3)
        else:
            pass
        await ctx.send(embed=e4)




def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Debug(bot))
