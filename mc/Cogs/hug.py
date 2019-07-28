import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Hug(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def hug(self,ctx, *, message=None): 
        member = ctx.message.content.split(" ")[0]
        if message is None: # No argument? Just assume it's you
            user = ctx.author
            hug_list = [f"Uh, ok? *hugs <@{user.id}>*", f"I don't do hugs, <@{user.id}>", f"I mean, if you want. *hugs <@{user.id}>*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs <@{user.id}>*", "*runs away*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        elif message == '@everyone' or message == '@here':
            await ctx.send(f"No.")
            
        elif message == 'f<@{self.b.user.id}>': # Oh no it's me!
            hug_list = [f"...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        else: # Argument, okay let's spit whatever the user just said
            hug_list = [f"Uh, ok? *hugs {message}*", f"I don't do hugs, <@{ctx.author.id}>", f"I mean, if you want. *hugs {message}*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs {message}*","*runs away*"] 
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))


def setup(bot):
    bot.add_cog(Hug(bot))
