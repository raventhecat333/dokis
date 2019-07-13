import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Commands(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def commands(self,ctx): 
        e = discord.Embed(title="Commands!", description="Here are all the commands/words/phrases you can use when you @mention me, although I hope you don't do this.", color=0xfcc608)
        e.add_field(name="Hi, Hello", value="Nothing wrong with a greeting, even when I don't want to do it.", inline=True)
        e.add_field(name="Test", value="Just to see if I'm fine (which I usually am).", inline=True)
        e.add_field(name="I love you, ILY", value="Uhhhhh...", inline=True)
        e.add_field(name="@mention loves you", value="No no no no no no no", inline=True)
        e.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to recieve a message like this when you wake up/go to sleep.", inline=True)
        e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="No, I'm not.", inline=True)
        e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="In case you ever do something wrong.", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Commands(bot))
