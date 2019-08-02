import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): 
        e = discord.Embed(title=f"A bug-fixing update! This has been changed on August 2, 2019. Version: {conf.version}",description='''
```
- Fixed self-hug responses [MONIKA, NATSUKI, SAYORI]

- Dokis should tell us poems now [ALL DOKIS]

- Fixed mentioned love responses [ALL DOKIS]

- All commands work in DMs now (except Yuri's Act toggle) [ALL DOKIS]

- Sayori and Natsuki won't print "hugs None" unintentionally [NATSUKI, SAYORI]

- Fixed an issue where Natsuki didn't ping the user when hugging them [NATSUKI]

- Sayori no longer butts into another doki's conversation [SAYORI]

- The rest of the dokis respond to "@MC loves you" in its own way now (it used to be just Sayori doing it) [MONIKA, NATSUKI, YURI]
```
''', color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
