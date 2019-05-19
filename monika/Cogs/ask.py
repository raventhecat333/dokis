import discord, random, asyncio
from discord.ext import commands as client
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def ask(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("Ahaha! D-did you want to ask me something?")
        else:
            answer_list = ["Yes!", "No!", "Ahaha! I-I don't really know, to be honest...", "As Club President, I say 'yes'!", "As Club President, I say 'no'!", "As Club President, I say 'maybe'!", "Uh... Well, uh... I think the Vice President would be better suited for this question!", "Y-Yuri's smart, right? I'm sure she can answer that!", "Maybe you can try asking Natsuki; she knows more than she lets on."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(0.4) 
            await ctx.send(random.choice(answer_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
