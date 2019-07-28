import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Hug(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def hug(self,ctx, *, message=None): 
        if message is None: #No argument? Just assume it's you
            user = ctx.author
            hug_list = [f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs <@{user.id}>*", f"Of course I'll hug you! You don't have to even ask twice! *hugs <@{user.id}>*",f"Have you had a rough day? Here, I'll make it a little better! *hugs <@{user.id}>*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        elif message == '@everyone' or message == '@here':
            await ctx.send(conf.everyone_tag)
            
        elif message == f'<@{self.b.user.id}>': # Oh noes it's me!
            hug_list = ["Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*", "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?", "Well, as Club President, it's my job to set a good example! *hugs myself*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        else: # Argument, okay let's spit whatever the user just said
            hug_list = [f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs {message}*", f"Of course I'll hug you! You don't have to even ask twice! *hugs {message}*",f"Have you had a rough day? Here, I'll make it a little better! *hugs {message}*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Hug(bot))
