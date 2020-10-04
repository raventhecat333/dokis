import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType

class Ask(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def ask(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        tampered = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        if not ctx.message.content.partition(' ')[2]:
            await self.bot.send(ctx, self.bot.character.ask(tamper=tampered, nothing=True))
        else:
            await self.bot.send(ctx, self.bot.character.ask(tamper=tampered, nothing=False))
        return

def setup(bot):
    bot.add_cog(Ask(bot))