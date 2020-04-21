import discord, random
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Tickle(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def tickle(self,ctx):
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {ctx.guild.id if ctx.guild else 0}) OR (type = 'user' AND id = {ctx.author.id})").fetchone() is not None else False
        await self.bot.send(ctx, self.bot.character.tickle(tamper=tampered))

def setup(bot):
    bot.add_cog(Tickle(bot))