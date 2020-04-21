import discord, random
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
        tampered = 1 if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {ctx.guild.id if ctx.guild else 0}) OR (type = 'user' AND id = {ctx.author.id})").fetchone() is not None else 0
        await self.bot.send(ctx, self.bot.character.headpat(tamper=tampered))

def setup(bot):
    bot.add_cog(Headpat(bot))