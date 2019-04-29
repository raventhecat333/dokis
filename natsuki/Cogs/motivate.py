import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Motivate(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def motivate(self,ctx, *, message=None): 
        member = ctx.message.content.split(" ")[0]
        if message is None: #No argument? Just assume it's you
            user = ctx.author
            motivate_list = [f"I believe in you {user.name}, you stupid sack of shit!", "C'mon, dummy! You can do it!", "*grabs shoulders* You've got this! I know you do!", "I'll bake you as many cupcakes as you want!", "You better do good or I'll shatter your shins!", "C'mon! Don't be a lazy goofball like Sayori!", "You better not act as dense as MC!", "DO IT! Just DO IT!!!", "Don't let your dreams be dreams!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I need someone to motivate! (n_motivate someone)")

        elif message == '@everyone' or message == '@here':
            await ctx.send(conf.everyone_tag)
            
        elif message == 'y_act' or message == 'y_act1' or message == 'y_act2':
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Nice try, Baka.")

        else: 
            motivate_list = [f"I believe in you {message}, you stupid sack of shit!", "C'mon, dummy! You can do it!", "*grabs shoulders* You've got this! I know you do!", "I'll bake you as many cupcakes as you want!", "You better do good or I'll shatter your shins!", "C'mon! Don't be a lazy goofball like Sayori!", "You better not act as dense as MC!", "DO IT! Just DO IT!!!", "Don't let your dreams be dreams!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(motivate_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Motivate(bot))
