import discord, json, os, time
import discord.ext.commands as client
from datetime import datetime

class Changelog(client.Cog):

    def __init__(self, bot):
         self.bot = bot
         self.file = open("changelog.txt", "r").read()

    @client.command(pass_context=True, aliases=['log'])
    async def changelog(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        config = json.loads(open("config.json", "r").read())
        color = self.bot.character.color
        date = datetime.strptime(time.ctime(os.path.getmtime("changelog.txt")), '%a %b %d %H:%M:%S %Y')
        daySuffix = 'th' if 11<=date.day<=13 else {1:'st',2:'nd',3:'rd'}.get(date.day%10, 'th')
        date = date.strftime(f'%b %d{daySuffix}, %Y')
        e = discord.Embed(title = f"Latest updates since {date} at version {config['version']}!",
        description = f"```{self.file}```",
        color = int(color, base=16))
        e.set_author(name=f"Changelog of {self.bot.name}.", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)
        return

def setup(bot):
    bot.add_cog(Changelog(bot))