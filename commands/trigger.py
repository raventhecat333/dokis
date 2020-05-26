import discord
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Trigger(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(pass_context=True, aliases=['triggers'])
    @client.cooldown(1, 2, BucketType.user)
    async def trigger(self,ctx):
        color = self.bot.character.color
        if ctx.guild is not None:
            member = await ctx.guild.fetch_member(ctx.author.id)
            if not ctx.channel.permissions_for(member).administrator:
                e = discord.Embed(title="You got no permissions to do that!",color=int(color, base=16))
                await ctx.send(embed=e)
                return
            if self.bot.globalCursor.execute(f"SELECT * FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'guild' AND id = {ctx.guild.id}").fetchone() is None:
                self.bot.globalCursor.execute(f"INSERT INTO offTriggers VALUES ('{self.bot.name}','guild',{ctx.guild.id})")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'Triggers are now disabled',color=int(color, base=16))
                await ctx.send(embed=e)
            else:
                self.bot.globalCursor.execute(f"DELETE FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'guild' AND id = {ctx.guild.id}")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'Triggers are now enabled',color=int(color, base=16))
                await ctx.send(embed=e)
        else:
            if self.bot.globalCursor.execute(f"SELECT * FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'user' AND id = {ctx.author.id}").fetchone() is None:
                self.bot.globalCursor.execute(f"INSERT INTO offTriggers VALUES ('{self.bot.name}','user',{ctx.author.id})")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'Triggers are now disabled',color=int(color, base=16))
                await ctx.send(embed=e)
            else:
                self.bot.globalCursor.execute(f"DELETE FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'user' AND id = {ctx.author.id}")
                self.bot.globalConnection.commit()
                e = discord.Embed(title = f'Triggers are now enabled',color=int(color, base=16))
                await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Trigger(bot))