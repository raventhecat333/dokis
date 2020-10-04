import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Recipes(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command(pass_context=True, aliases=['recipe'])
    @client.cooldown(1, 2, BucketType.user)
    async def recipes(self,ctx):
        await self.bot.send(ctx, self.bot.character.recipes())

def setup(bot):
    bot.add_cog(Recipes(bot))

def check(character):
    return hasattr(character, "recipes")