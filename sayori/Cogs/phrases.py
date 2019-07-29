import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Phrases(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command(aliases=['commands'])
    async def phrases(self,ctx): 
        e = discord.Embed(title="Phrases!", description="Here are all the words/phrases you can use when you @mention me! Though it's ***VERY*** important that the @mention is at the very beginning!", color=conf.norm)
        e.add_field(name="Hi, Hello", value="Nothing wrong with a simple hello every now and then, right?", inline=True)
        e.add_field(name="Test", value="Just to see if I'm working properly!", inline=True)
        e.add_field(name="I love you, ILY", value="Even though I'm not worthy of being loved, you're still free to tell me that you love me if you'd like! Ehehe...", inline=True)
        e.add_field(name="@mention loves you", value="Want to let me know if someone in the server loves me? Let me know by formatting the message like this: ***@Sayori @mention loves you***", inline=True)
        e.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to recieve a message like this when you wake up/go to sleep.", inline=True)
        e.add_field(name="@mention is a meanie, @mention is being a meanie", value="Someone in the server being a meanie? Use this to let me know so I can call them out on it! (Full message should look like this: ***@Sayori @mention is (being) a meanie***)", inline=True)
        e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="What? A girl likes to be complimented!", inline=True)
        e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Did you accidentally hurt me? Feel free to tell me that you're sorry! It's the right thing to do.", inline=True)
        e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="Oh my are you sick? Well i'll wish you luck to get better then!", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Phrases(bot))
