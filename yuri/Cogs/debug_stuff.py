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
        if ctx.guild.id not in conf.act2:
            e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
This guild is currently on Act 1 Mode.

''',color=0x36393f)
            e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)


            e2 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
''',color=0x36393f)

            await ctx.send(embed=e)
            await ctx.send(embed=e2)











#---------------------------------------------------------------------------------------------------------









        elif ctx.guild.id in conf.act2:
            e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
This guild is currently on Act 2 Mode.

''',color=0x36393f)
            e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)


            e2 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
''',color=0x36393f)

            await ctx.send(embed=e)
            await ctx.send(embed=e2)






        elif ctx.guild.id in conf.act1 and conf.act2:
            e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
Better dm cheezy about this, it's running on both acts for whatever reason.

''',color=0x36393f)
            e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)


            e2 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
''',color=0x36393f)

            await ctx.send(embed=e)
            await ctx.send(embed=e2)




        else:
            e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
Strange, is this in a DM?

''',color=0x36393f)
            e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)


            e2 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
''',color=0x36393f)

            await ctx.send(embed=e)
            await ctx.send(embed=e2)
def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Debug(bot))
