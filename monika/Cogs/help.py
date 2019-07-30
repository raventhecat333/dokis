import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Help(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def help(self,ctx): 
        embed = discord.Embed(title="Greetings! I'm Monika!", description="Cole ~~finally~~ turned my .chr file into a .py file so I can join Discord! I'm not fully self-aware like I was in DDLC, but this will have to suffice!", color=0x12ba01)
        embed.add_field(name="m_ask", value="Use this to ask me a yes-or-no question. I'm admittedly not the smartest person ~~in the game~~ on Earth, but I'll try my hardest to answer correctly!", inline=True)
        embed.add_field(name="m_delete", value="Do you need something 'deleted' from your server? I'll be happy to help!", inline=True)
        embed.add_field(name="m_feed", value="Would you like to feed me something? You can with this command!", inline=True)
        embed.add_field(name="m_headpat", value="Ahaha! I don't understand the appeal of patting girls on the head, but I suppose I can figure it out...", inline=True)
        embed.add_field(name="m_hug", value="I'm always open to giving a hug to anyone who wants one! Or, let's be honest, even if they *don't* want one!", inline=True)
        embed.add_field(name="m_tickle", value="O-Oh! Well, I guess there are worse things to do to me than tickling!", inline=True)
        embed.add_field(name="m_changelog", value="Check out what's been changed!", inline=True)
        embed.add_field(name="@Monika", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say! Type 'm_phrases' for a full list!", inline=True)
        embed.add_field(name="I do believe that's it!", value="I'm still in very early stages of development, but if Cole was able to create the other girls quickly, I'm sure I'll be finished before you know it!")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.remove_command("help")
    bot.add_cog(Help(bot))
