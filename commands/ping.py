import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Ping(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command(pass_context=True, aliases=['doki'])
    @client.cooldown(1, 2, BucketType.user)
    async def ping(self,ctx):
        color = self.bot.character.color
        e = discord.Embed(color=int(color, base=16))
        e.add_field(name='Pong! :ping_pong:', value=f'`{round(self.bot.latency * 1000)}ms`', inline=False)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Ping(bot))