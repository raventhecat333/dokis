import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Help(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def help(self,ctx): 
        embed = discord.Embed(title="Hi! I'm Sayori!", description="Cole was kind enough to turn my .chr file into a file that can let me interact with you guys to a certain extent! My commands are as follows:", color=conf.norm)
        embed.add_field(name="s_ask", value="Use this to ask me a yes-or-no question and receive an answer! Will I always be correct? Probably not, but my answers could yield some silly results!~", inline=True)
        embed.add_field(name="s_feed", value="Use this to feed me any of the foods available in the 'food' section of the Discord Emojis! Don't worry, I have a big stomach, so you can feed me as much as you want! *(Format like this: s_feed :food_emoji:)*", inline=True)
        embed.add_field(name="s_headpat", value="Use this to pat me on the head! :grin:", inline=True)
        embed.add_field(name="s_hug", value="Use this to have me hug someone! Leave it blank to have me hug you, or mention someone to have me hug them! *(Format like this: s_hug @mention)*", inline=True)
        embed.add_field(name="s_invite", value="Use this to put my Discord invite link in the chat so anyone can invite me to their own server!", inline=True)
        embed.add_field(name="s_joke", value="Use this to have me tell a random joke!", inline=True)
        embed.add_field(name="s_lifeline", value="I-Is someone on the server talking about ending their life...? Use this to pull up the National Suicide Prevention Lifeline. It doesn't really guarantee that they'll call it, but at least it's something you can do to try and help!", inline=True)
        embed.add_field(name="s_poems", value="Use this to read one of the poems from Doki Doki Literature Club!", inline=True)
        embed.add_field(name="s_quote", value="Use this to have me say one of my quotes from the game!", inline=True)
        embed.add_field(name="s_swear", value="Use this to have me swear! Why you would want me to, I'm not sure, but the option is there!", inline=True)
        embed.add_field(name="s_tickle", value="Use this to make me laugh!", inline=True)
        embed.add_field(name="s_changelog", value="Check out what's been changed!", inline=True)
        embed.add_field(name="@Sayori", value="Use this to either get my attention or to use special 'trigger words/phrases' to get certain responses out of me! Type 's_phrases' or `s_commands` for a full list!", inline=True)
        embed.add_field(name="And that's about it!", value="I'm sure Cole will add more stuff for me to do soon, but for now, I hope you enjoy my presence on the server! If you have any questions, comments, or bugs, let Cole know! Oh, and please don't be a meanie :unamused:. That's all for now. Bye!~")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.remove_command("help")
    bot.add_cog(Help(bot))
