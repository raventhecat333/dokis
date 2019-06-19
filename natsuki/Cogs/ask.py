import discord, random, asyncio
from discord.ext import commands as client
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def ask(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("Hey! You wanted to ask me something so what is it?!")
        else:
            answer_list = ["Eh. Probably not.","I guess so.","How should I know, dummy?", "I don't know. Ask Monika if you want the answer that badly.", "No.","Pfft. In your dreams!", "Is manga literature?", "Yuri might know."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(0.4) 
            await ctx.send(random.choice(answer_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
