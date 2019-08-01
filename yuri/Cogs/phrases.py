import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Phrases(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def phrases(self,ctx):
        if ctx.guild.id not in conf.act2:
            e = discord.Embed(title="Phrases!", description="Uuuuu... So here are all the words/phrases you can use when you @mention me. It's ***VERY*** important that you @mention me at the very beginning...", color=conf.norm)
            e.add_field(name="Hi, Hello", value="I guess a greeting doesn't hurt every now and then...", inline=True)
            e.add_field(name="Test", value="Just to see if I'm working just fine ~~even when I'm silently reading and avoiding interaction~~.", inline=True)
            e.add_field(name="I love you, ILY", value="Uuuuu... That seems embarrassing, but you can still tell me this if you like.", inline=True)
            e.add_field(name="@mention loves you", value="Someone out there l-loves me? If they do, just t-tell me like this: ***@Yuri @mention loves you***", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="I-I-I-It's nice to be told if you're going to sleep or j-just waking up.", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="W-W-W-W-Who? M-M-Me? Uuuuuuu... :confounded:", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="D-D-Did you hurt me? Y-You know I forgive you, r-right???", inline=True)
            e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="Well, I hope you get w-well soon.", inline=True)
        else:
            e = discord.Embed(title="Phrases!", description="So here are all the words/phrases you can use when you @mention me. It's ***VERY*** important you @mention me at the beginning, or this won't work!", color=conf.norm)
            e.add_field(name="Hi, Hello", value="It's good to greet me so I know you're here! ~~I don't know what I would do if you weren't!!!~~", inline=True)
            e.add_field(name="Test", value="Oh, so I need to be tested to see if I'm fine! How adorable!!!", inline=True)
            e.add_field(name="I love you, ILY", value="Tell me this as much as you want! It still makes me so wet!!!", inline=True)
            e.add_field(name="@mention loves you", value="They don't love me as much I love you, you know! But if you must, tell me like this: ***@Yuri @mention loves you***", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="If you're going to sleep or if you woke up, please tell me! ~~That way, I can make sure nobody takes you away when you're unconscious.~~", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="Of course I am, but not as much as you!!!", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="It's so cute when you do that~~, it makes me so wet!!!~~", inline=True)
            e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="I hope you get well soon! I don't know what I would do if you don't!", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Phrases(bot))
