import discord, random, re
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Hug(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def hug(self,ctx):
        tampered = 1 if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {ctx.guild.id if ctx.guild else 0}) OR (type = 'user' AND id = {ctx.author.id})").fetchone() is not None else 0
        target = ctx.message.content.partition(' ')[2]
        mc = next( (c for c in self.bot.chrs if c["name"].lower() == "mc"), None)
        mcID = mc["character"].id
        if not target:
            await self.bot.send(ctx, self.bot.character.hug(tamper=tampered, target="player", targetName=f"<@{ctx.author.id}>"))
        elif re.search(f"^({self.bot.name}|<@!?{self.bot.user.id}>|yourself)$", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.hug(tamper=tampered, target="self", targetName=""))
        elif re.search(f"^(mc|<@!?{mcID}>)$", target, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.hug(tamper=tampered, target="mc", targetName=f"<@{mcID}>"))
        else:
            await self.bot.send(ctx, self.bot.character.hug(tamper=tampered, target="", targetName=target))

def setup(bot):
    bot.add_cog(Hug(bot))