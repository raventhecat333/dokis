import discord, json, rstr, sys
import discord.ext.commands as client

class Debug(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    async def debug(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        config = json.loads(open("config.json", "r").read())
        color = self.bot.character.color
        onTrigger = self.bot.globalCursor.execute(f"SELECT * FROM offTriggers WHERE (type = 'guild' AND id = '{0 if not ctx.guild else ctx.guild.id}') OR ( type = 'user' AND id = '{ctx.author.id}')").fetchone()
        onTamper = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        triggerMode = 'Yes' if onTrigger is None else 'No'
        tamperMode = 'Yes' if onTamper else 'No'
        e = discord.Embed(title = f"Debug info for {self.bot.name}", description = f'''**Version:** {config['version']}
**Username:** {self.bot.user.name}#{self.bot.user.discriminator}
**ID:** {self.bot.user.id}
**Possible Prefix:** {rstr.xeger(self.bot.character.prefix)}
**Discord.py Version:** {discord.__version__}
**Python Version:** {'.'.join(map(str, sys.version_info[:3]))}
**Shards**: {len(self.bot.shards)}
**Guilds:** {len(self.bot.guilds)}
**Are Triggers Enabled?** {triggerMode}
**Is Tamper Mode Enabled?** {tamperMode}''',
        color = int(color, base=16))
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Debug(bot))