import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Jokes(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command(pass_context=True, aliases=['joke'])
    @client.cooldown(1, 2, BucketType.user)
    async def jokes(self,ctx):
        await self.bot.send(ctx, self.bot.character.jokes())

def setup(bot):
    bot.add_cog(Jokes(bot))

def check(character):
    return hasattr(character, "jokes")