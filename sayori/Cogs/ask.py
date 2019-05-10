import discord, random, asyncio
from discord.ext import commands as client
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def ask(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("I can't answer the question if you don't ask one, silly!")
        else:
            answer_list = ["Yes!", "No.", "Maybe.", "Possibly?", "Of course, silly!", "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!", "I'd say ask Yuri, but she's a little shy at the moment.", "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!", "You've got a better chance of having a happy ending in DDLC! Ehehe...~", "Maybe we should ask The Magic Conch, instead.", "As sure as I'm depressed!", "Not really.", "My Vice President Powers tell me yes!", "My Vice President Powers tell me no!", "My Vice President Powers tell me maybe!", "J-Just a little bit!"]            
            async with ctx.message.channel.typing():
                await asyncio.sleep(0.4) 
            await ctx.send(random.choice(answer_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
