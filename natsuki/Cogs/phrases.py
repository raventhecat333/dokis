import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Phrases(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def phrases(self,ctx): 
        e = discord.Embed(title="Phrases!", description="Here are all the words/phrases you can use when you @mention me! Though it's ***VERY*** important that the @mention is at the very beginning!", color=conf.norm)
        e.add_field(name="Hi, Hello", value="I-It's not like you have to greet me or anything!", inline=True)
        e.add_field(name="Test", value="I'm usually working fine, you dummy!", inline=False)
        e.add_field(name="I love you, ILY", value="R-Really? You, out of all people, actually l-love me?!", inline=True)
        e.add_field(name="@mention loves you", value="Someone else on this server l-loves me? Just make sure you tell me like this: ***@Natsuki @mention loves you***", inline=True)
        e.add_field(name="Goodnight, Good night, Good morning", value="You definitely don't need to bother me in the morning or at night! Y-You don't!", inline=True)
        e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="***WHAT? N-NO, I'M NOT!!!***", inline=True)
        e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Well, at least you can acknowledge that you were a jerk!", inline=True)
        e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="I hope you get well, then! I-It's not like I care or anything...", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Phrases(bot))
