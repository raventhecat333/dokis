import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Poems(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command(pass_context=True, aliases=['poem'])
    @client.cooldown(1, 2, BucketType.user)
    async def poems(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        tampered = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        color = self.bot.character.color
        poemName = ctx.message.content.partition(' ')[2]
        poem = self.bot.character.poems(tamper=tampered, name=poemName)
        if len(poem[1]) > 2000:
            poem_half_first, poem_half_second = poem[1][:len(poem[1])//2],  poem[1][len(poem[1])//2:] 
            e = discord.Embed(title=poem[0], description=poem_half_first,color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)
            e = discord.Embed(description=poem_half_second,color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)
        else:
            e = discord.Embed(title=poem[0], description=poem[1],color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)

def setup(bot):
    bot.add_cog(Poems(bot))