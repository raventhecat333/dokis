import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): 
        e = discord.Embed(title=f"A majour bug-fixing update! This has been changed at 26/07/2019. Version: {conf.version}",description='''
```
-Rewrote the tagging function to use regex [ALL]

-Fixed the "Poems" command [MONIKA]

=Fixed "toggle" command [ALL]

-Updated a string for the toggle command [ALL]

-Monika now has her own DBL link!

-Traceback embed has the correct color [SAYORI, MC]

-Added DM support [YURI]

-Added changelog command [ALL]

-MC has been made!

-The ACT system has been changed to use one list to fix some issues [YURI]

-The TOGGLE system has been changed to use one list to fix some issues [ALL]

-Added new playing statuses [ALL]

-Cogs are now loaded differently to make the file much more cleaner [ALL]

-Confused responses have been reverted back to the old responses [ALL]

-Added the command "Shard" to check what shard your guild is on [ALL]

-Added the "Act" command to check what act you're on [YURI]

-Changed the "that's not food" string [NATSUKI]
```
''', color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
