import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def ask(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if ctx.guild is None:
            if arg1 is None:
                await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
            else:
                answer_list0 = ["Y-Yes.", "No...", "I'm not really sure.", "I don't believe so...", "I think that's a question best suited for Sayori.", "Perhaps Monika could be of better help?", "I-I don't know. I'm sorry...", "Natsuki might know.", "I believe so!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed) 
                await ctx.send(random.choice(answer_list0))


        elif ctx.guild.id not in conf.act2: #This is incase the guild that this command was used in is set to act1
            if arg1 is None:
                await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
            else:
                answer_list1 = ["Y-Yes.", "No...", "I'm not really sure.", "I don't believe so...", "I think that's a question best suited for Sayori.", "Perhaps Monika could be of better help?", "I-I don't know. I'm sorry...", "Natsuki might know.", "I believe so!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed) 
                await ctx.send(random.choice(answer_list1))

        elif ctx.guild.id in conf.act2: #This is incase the guild that this command was used in is set to act2
            if arg1 is None:
                await ctx.send("Ahaha... If you don't have a question, that's okay. I'd rather stare at you.")
            else:
                answer_list2 = ["Yes.", "I don't know, and I don't care. I just want to look at you...", "No.", "Possibly, but who knows?", "Meet me in the closet and we'll find out... :kissing_closed_eyes:", "Ahaha! You're so silly to ask such a question!", "I'm not sure... I'll think about it while I'm touching myself to you tonight."]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send(random.choice(answer_list2))            
        



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
