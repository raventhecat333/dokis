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
        if message is None: #No argument? Just assume it's you
            user = ctx.author
            hug_list = [f"One hug, coming right up! *hugs <@{user.id}>*", f"I'll try not to squeeze too hard! *hugs <@{user.id}>*", f"Time for the super-mega-cinnamon-bun hug! *hugs <@{user.id}>*", f"How could I say no to a hug? *hugs <@{user.id}>*", f"Yay, hugs! *hugs <@{user.id}>*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(hug_list))

        elif message == '@everyone' or message == '@here':
            await ctx.send(conf.everyone_tag)
            
        elif message == f'<@{self.b.user.id}>': # Oh noes it's me!
            hug_list = [f"...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(hug_list))

        else: # Argument, okay let's spit whatever the user just said
            hug_list = [f"One hug, coming right up! *hugs {message}*", f"I'll try not to squeeze too hard! *hugs {message}*", f"Time for the super-mega-cinnamon-bun hug! *hugs {message}*", f"How could I say no to a hug? *hugs {message}*", f"Yay, hugs! *hugs {message}*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(hug_list))


def setup(bot):
    bot.add_cog(Hug(bot))
