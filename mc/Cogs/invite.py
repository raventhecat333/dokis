import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def invite(self,ctx): 
            e = discord.Embed(title="My invite link!", description="Here's the server invite link so anyone else here can invite me to their server!", color=conf.norm)
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordapp.com/oauth2/authorize?client_id=596407346176065552&scope=bot&permissions=130112)", inline=True)
            await ctx.send(embed=e)



def setup(bot):
    bot.add_cog(Invite(bot))
