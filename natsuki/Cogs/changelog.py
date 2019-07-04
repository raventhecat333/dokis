import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): 
        e = discord.Embed(title=f"A beta update! This has been changed at 29/06/2019. Version: {conf.version}",description='''
```

-Fixed a majour bug that caused people to spam the doki's using trigger words

-Added the "changelog" command

```
''', color=conf.norm)
        e.set_author(name="The Changelog for Natsuki.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
