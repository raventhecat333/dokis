import discord, random, asyncio, sys
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Testing(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def test(self,ctx): 
        e = discord.Embed(description=f'''
Hi i'm Monika! I'm just going to go through the basics of setting me up on your server!

First of all if you haven't already invited me to your server, run the m_invite to do so.

__**How to disable/enable chat triggers and use commands**__
Chat triggers can be enabled/disabled using the command `{conf.prefix1}toggle`

__**How to use my tagging reactions**__
To use a chat trigger such as "hi" do:

"@mention hi"

This will make me say hi right back to you!

__**Permissions**__
When trying to enable/disable my chat triggers please make sure one of your roles has the `manage messages` permission set to ON.
Also be sure to allow me to send Embeds and Text in the channel

__**For more infomation**__
If you are still struggling then you can visit the Doki Bot Testing server to ask for support which you can join by clicking [here!](https://discordbots.org/bot/436351740787294208)

If you want a list of all the commands then run "m_help", or if you want to see a full list of my phrases then run 'm_phrases'
''', color=conf.norm)

        e.set_author(name=f"{self.b.user.name}",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)

    @client.command()
    async def bugme(self,ctx,shit2=None,*, shit3=None):
        if shit2 is None or shit3 is None:
            await ctx.send("Hey you're missing some args there pal")
        else:
            bug = shit3
            doki = shit2
            e = discord.Embed(colour=conf.err)
            e.add_field(name="The bug:", value=f"```{bug}```")
            e.add_field(name="The doki:", value=f"```{doki}```",inline=False)
            e.set_author(name="Fuck you Obama",icon_url=ctx.message.author.avatar_url)
            e.set_footer(text="v"+conf.version)
            await ctx.send(embed=e)
            

def setup(bot):
    bot.add_cog(Testing(bot))
