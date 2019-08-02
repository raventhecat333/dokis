import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def ask(self, ctx, arg1=None):
        if arg1 is None:
            await ctx.send("I can't answer a non-existent question.")
        else:
            answer_list = ["I don't know why you're asking me, go ask Sayori.", "Yes, I guess.", "No, I think; I don't care either way.", "Maybe? Monika would know.", "Yeh.", "No, just no."]            
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(answer_list))


def setup(bot):
    bot.add_cog(Ask(bot))
