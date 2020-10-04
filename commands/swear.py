import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Swear(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def swear(self,ctx):
        await self.bot.send(ctx, self.bot.character.swear())

def setup(bot):
    bot.add_cog(Swear(bot))

def check(character):
    return hasattr(character, "swear")