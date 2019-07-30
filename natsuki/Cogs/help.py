import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Help(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def help(self,ctx): 
        embed = discord.Embed(title="Hey, it's me, Natsuki.", description="Freaking Cole decided to turn my .chr file into a file that lets me be on this Discord server. It's not like I'm here because I want to be or anything, you dummies! A-anyway, here are the things I can do:", color=conf.norm)
        embed.add_field(name="n_ask", value="You can ask me any yes-or-no question with this. But don't get mad if I don't know the answer or if I give the wrong answer!", inline=True)
        embed.add_field(name="n_feed", value="Y-you don't have to or anything, but I guess you could feed me some food i-if you really wanted to... *(Format like this: 'n_feed :food_emoji:')*", inline=True)
        embed.add_field(name="n_headpat", value="You can use this to pat me on the head, but why any normal person would want to, I have no clue...", inline=True)
        embed.add_field(name="n_hug", value="Ugh. Hugs are gross, but if you want me to hug you or anyone on the server, I guess I can do that for you... Just leave it blank if you want me to hug you or @mention someone to have me hug them. *(Format like this: n_hug @mention)*", inline=True)
        embed.add_field(name="n_invite", value="You can use this to show the link to invite me to other servers. But don't think that I'll enjoy it, you dummy!", inline=True)
        embed.add_field(name="n_motivate", value="I-it's not like I want to, but if you need motivation or encouragement, I'll try to help you out, I guess.", inline=True)
        embed.add_field(name="n_quote", value="You can use this to make me say one of my quotes from the game.", inline=True)
        embed.add_field(name="n_recipe", value="Do you like baking, like me? Well, I've got a few recipes in my cookbook; feel free to check them out!", inline=True)
        embed.add_field(name="n_tickle", value="You can use this to... TICKLE ME?? Oh, don't you dare use that unless you want a trip to the hospital!", inline=True)
        embed.add_field(name="n_changelog", value="Check out what's been changed!", inline=True)
        embed.add_field(name="@Natsuki", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say! Type 'n_phrases' for a full list!", inline=True)
        embed.add_field(name="I guess that's it...", value="Cole will make me do more stuff soon, but I'm not looking forward to it! If you want, you can go visit his Support Server and give him a piece of my mind! Anyway, see you later, ~~bakas~~ everyone!", inline=True)
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.remove_command("help")
    bot.add_cog(Help(bot))
