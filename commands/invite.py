import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Invite(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def invite(self,ctx):
        color = self.bot.character.color
        e = discord.Embed(title = f"Invite {self.bot.user.name}!",
        description = f"[Click here to invite {self.bot.name}.chr!](https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot)",
        color=int(color, base=16))
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Invite(bot))