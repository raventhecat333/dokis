import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Help(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def help(self,ctx): 
        embed = discord.Embed(title="I'm MC, I guess.", description="So somehow my non-existent .chr file was turned into a discord bot file, or whatever the hell it's called, anyways I'm here because Sayori dragged me here. I don't have any talents or anything so I don't know why I'm here.", color=conf.norm)
        embed.add_field(name="mc_ask", value="You can ask me anything, I really don't care.", inline=True)
        embed.add_field(name="mc_feed", value="I'll eat really anything, but I'm fine with my own food.", inline=True)
        embed.add_field(name="mc_headpat", value="Useless command.", inline=True)
        embed.add_field(name="mc_hug", value="You can hug me, I don't know why but you can.", inline=True)
        embed.add_field(name="mc_invite", value="I don't know why but you can invite me to your server, if you want to.", inline=True)
        embed.add_field(name="mc_quote", value="You can make me say a quote from the game, I don't know why you would want to, but you can.", inline=True)
        embed.add_field(name="mc_tickle", value="I'm not tickleish, don't bother.", inline=True)
        embed.add_field(name="mc_changelog", value="Check out what's been changed!", inline=True)
        embed.add_field(name="mc_confess", value="Don't use this at all!", inline=True)
        embed.add_field(name="@MC", value="Use this to either get my attention or to use special 'trigger words/phrases' to get certain responses out of me! Type 'mc_commands' for a full list!", inline=True)
        embed.add_field(name="And that's about it!", value="I'm sure Cole will add more stuff for me to do soon, but for now, I hope you enjoy my presence on the server! If you have any questions, comments, or bugs, let Cole know! Oh, and please don't be a meanie :unamused:. That's all for now. Bye!~")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot): 
    bot.remove_command("help")
    bot.add_cog(Help(bot))
