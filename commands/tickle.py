import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Tickle(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def tickle(self,ctx):
        tampered = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        await self.bot.send(ctx, self.bot.character.tickle(tamper=tampered))

def setup(bot):
    bot.add_cog(Tickle(bot))