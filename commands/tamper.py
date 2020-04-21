import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Tamper(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def tamper(self,ctx):
        color = self.bot.character.color
        if ctx.guild is not None:
            if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND type = 'guild' AND id = {ctx.guild.id}").fetchone() is None:
                self.bot.globalCursor.execute(f"INSERT INTO tampered VALUES ('{self.bot.name}','guild',{ctx.guild.id})")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'{self.bot.name} got tampered with!',color=int(color, base=16))
                await ctx.send(embed=e)
            else:
                self.bot.globalCursor.execute(f"DELETE FROM tampered WHERE bot = '{self.bot.name}' AND type = 'guild' AND id = {ctx.guild.id}")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'{self.bot.name} got fixed!',color=int(color, base=16))
                await ctx.send(embed=e)
        else:
            if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND type = 'user' AND id = {ctx.author.id}").fetchone() is None:
                self.bot.globalCursor.execute(f"INSERT INTO tampered VALUES ('{self.bot.name}','user',{ctx.author.id})")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'{self.bot.name} got tampered with!',color=int(color, base=16))
                await ctx.send(embed=e)
            else:
                self.bot.globalCursor.execute(f"DELETE FROM tampered WHERE bot = '{self.bot.name}' AND type = 'user' AND id = {ctx.author.id}")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'{self.bot.name} got fixed!',color=int(color, base=16))
                await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Tamper(bot))