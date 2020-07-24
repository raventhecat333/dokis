import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Headpat(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(pass_context=True, aliases=['pat'])
    @client.cooldown(1, 2, BucketType.user)
    async def headpat(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        tampered = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        await self.bot.send(ctx, self.bot.character.headpat(tamper=tampered))

def setup(bot):
    bot.add_cog(Headpat(bot))