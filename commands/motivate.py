import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Motivate(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def motivate(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        target = ctx.message.content.partition(' ')[2]
        if not target:
            target = f"<@{ctx.author.id}>"
        await self.bot.send(ctx, self.bot.character.motivate(target=target))

def setup(bot):
    bot.add_cog(Motivate(bot))

def check(character):
    return hasattr(character, "motivate")