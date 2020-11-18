import asyncio, discord, json, rstr, sys
import discord.ext.commands as client

class Debug(client.Cog):

    def __init__(self, bot):

         self.bot = bot

    @client.command()
    async def debug(self,ctx):

        if await self.bot.DetectEveryoneMention(ctx):
            return
        config = json.loads(open("config.json", "r").read())
        color = self.bot.ChrFile["about"]["color"]
        e = discord.Embed(title = f"Debug info for {self.bot.ChrFile['about']['name']}", description = f'''**Version:** {config['version']}
**Username:** {self.bot.user.name}#{self.bot.user.discriminator}
**ID:** {self.bot.user.id}
**Possible Prefix:** {rstr.xeger(self.bot.ChrFile["about"]["prefix"])}
**Discord.py Version:** {discord.__version__}
**Python Version:** {'.'.join(map(str, sys.version_info[:3]))}
**Shards**: {len(self.bot.shards)}
**Guilds:** {len(self.bot.guilds)}''',
        color = int(color, base=16))
        await ctx.send(embed=e)

def setup(bot):

    bot.add_cog(Debug(bot))