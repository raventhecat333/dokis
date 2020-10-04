import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Quotes(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(pass_context=True, aliases=['quote'])
    @client.cooldown(1, 2, BucketType.user)
    async def quotes(self,ctx):
        await self.bot.send(ctx, self.bot.character.quotes())

def setup(bot):
    bot.add_cog(Quotes(bot))