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
        embed.add_field(name="mc_ask", value="You can ask me anything, I really don't care.", inline=False)
        embed.add_field(name="mc_feed", value="I'll eat really anything, but I'm fine with my own food.", inline=False)
        embed.add_field(name="mc_headpat", value="Useless command.", inline=False)
        embed.add_field(name="mc_hug", value="You can hug me, I don't know why but you can.", inline=False)
        embed.add_field(name="mc_invite", value="I don't know why but you can invite me to your server, if you want to.", inline=False)
        embed.add_field(name="mc_quote", value="You can make me say a quote from the game, I don't know why you would want to, but you can.", inline=False)
        embed.add_field(name="mc_tickle", value="I'm not tickleish, don't bother.", inline=False)
        embed.add_field(name="mc_changelog", value="Check out what's been changed!", inline=False)
        embed.add_field(name="mc_confess", value="Don't use this at all!", inline=False)
        embed.add_field(name="mc_rename", value="You can change my name (note, this only for the server and you must have manage nicknames or administrator permissions)", inline=True)
        embed.add_field(name="@MC", value="So use this I think to get my attention. You can also type 'mc_commands' for a full list of what I can do (not much) or mc_invite if for some reason you want me on your server.", inline=True)
        embed.add_field(name="I think that's all about me!", value="Most likely Cole will make me do more things (sadly) if I’m buggy blame Monika and let Cole know if you have any questions I guess, I’m going back to sleep now~")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
