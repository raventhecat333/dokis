import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Quotes(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def quote(self,ctx): 
        quote_list = ["MANGA IS LITERATURE!", "I'M NOT CUTE!", "Well, you know what?! I wasn't the one whose boobs magically grew a size bigger as soon as MC started showing up!!", "Whoa, be careful or you might cut yourself on that edge, Yuri. Oh, my bad... You already do, don't you?", "Freaking Monika!", "***fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm***", "You really shouldn't do that kind of thing to girls...unless you really like them...", "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--", "You really need to...beat...the crap out of it!", "If you really just came for the cupcakes, I would be super pissed."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(quote_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Quotes(bot))
