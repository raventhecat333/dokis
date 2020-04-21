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
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {ctx.guild.id if ctx.guild else 0}) OR (type = 'user' AND id = {ctx.author.id})").fetchone() is not None else False
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
            print("---------------------------")
            print(poem[1])
            print("---------------------------")
            e = discord.Embed(title=poem[0], description=poem[1],color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)

def setup(bot):
    bot.add_cog(Poems(bot))