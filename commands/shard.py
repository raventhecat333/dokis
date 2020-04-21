import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Shard(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def shard(self,ctx):
        color = self.bot.character.color
        e = discord.Embed(title = f'You are on shard {ctx.guild.shard_id}',color=int(color, base=16))
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Shard(bot))