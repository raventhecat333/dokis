import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Quotes(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def quote(self,ctx): 
        quote_list = ["As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!", "I'm confident that we can all really grow this club before we graduate!", "Then that makes it official! Welcome to the Literature Club!", "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom.", "I guess you could say that I had some kind of epiphany recently. It's been influencing my poems a bit.", "...That's my advice for today! Thanks for listening~", "Wait...is this tip even about writing? What am I even talking about? Ahaha!", "Humans aren't two-dimensional creatures. I think you'd know that better than anyone.", "Also, that joke makes no sense in translation!", "And I also care about the well-being of my club members, you know?", "Have you thought that maybe you've always seen her as so cheerful because that's just how she is when she's around you?", "C-Catchphrase? I don't have a catchphrase...", "Yay, you picked me!", "You kind of left her hanging this morning, you know?", "Don't worry. I probably know a lot more than you think."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(quote_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Quotes(bot))
