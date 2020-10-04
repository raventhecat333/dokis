import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Rename(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def rename(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        color = self.bot.character.color
        if not ctx.message.channel.permissions_for(ctx.message.author).manage_nicknames:
            e = discord.Embed(title = "You don't have the proper permissions to change my name.",color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)
            return
        name = ctx.message.content.partition(' ')[2]
        if name == "MC":
            name = ""
        await ctx.message.author.guild.me.edit(nick=f"{name}")
        if not name:
            e = discord.Embed(title = f"Name has reset!",color=int(color, base=16))
        else:
            e = discord.Embed(title = f"Name set to: {name}!",color=int(color, base=16))
        await self.bot.send(ctx, "", embed= e)

def setup(bot):
    bot.add_cog(Rename(bot))

def check(character):
    return hasattr(character, "rename")