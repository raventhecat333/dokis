import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Hug(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def hug(self,ctx, *, message=None):
        # TODO: Find a way to condense these two if statements into one

        if ctx.guild is None: #Runs in direct messages. 
            if message is None: #No argument? Just assume it's you
                user = ctx.author
                hug_list5 = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs <@{user.id}>*", f"Just let me know if this is too much for you... *hugs <@{user.id}>*", f"*hugs <@{user.id}>* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(hug_list5))

            elif message == '@everyone' or message == '@here':
                await ctx.send(conf.everyone_tag)
            
            elif message == f'<@{self.b.user.id}>': # Oh noes it's me!
                hug_list6 = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(hug_list6))

            else: # Argument, okay let's spit whatever the user just said
                hug_list7 = [f"Y-you want me to hug them? Well, o-okay, I guess I can do that for you... *hugs {message}*", f"Just let me know if this is too much for you... *hugs {message}*", f"*hugs {message}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(hug_list7))

        if ctx.guild.id not in conf.act2: # Runs if in a guild and in Act 1
            if message is None: #No argument? Just assume it's you
                user = ctx.author
                hug_list1 = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs <@{user.id}>*", f"Just let me know if this is too much for you... *hugs <@{user.id}>*", f"*hugs <@{user.id}>* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(hug_list1))

            elif message == '@everyone' or message == '@here':
                await ctx.send(conf.everyone_tag)
            
            elif message == f'<@{self.b.user.id}>': # Oh noes it's me!
                hug_list2 = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(hug_list2))

            else: # Argument, okay let's spit whatever the user just said
                hug_list3 = [f"Y-you want me to hug them? Well, o-okay, I guess I can do that for you... *hugs {message}*", f"Just let me know if this is too much for you... *hugs {message}*", f"*hugs {message}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send(random.choice(hug_list3))

        if ctx.guild.id in conf.act2: #This is incase the guild that this command was used in is set to act2
            if message is None: #No argument? Just assume it's you
                user = ctx.author
                hug_list4 = [f"*hugs <@{user.id}>* Ahaha... I could hug you forever...!", f"Oh, you have no idea how long I've been waiting for you to say that!! *hugs <@{user.id}>*", f"*hugs <@{user.id}>* Mmm... You smell so wonderful! I wish I could smell this smell forever!", f"Uhuhu... You can even grab my ass while we hug if you wanted. I don't mind ;) *hugs <@{user.id}>*", f"*hugs <@{user.id}>* Oh, you're pressing hard against my chest. I must say, I really, really love it!"]
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send(random.choice(hug_list4))

            elif message == '@everyone' or message == '@here':
                await ctx.send(conf.everyone_tag)
            
            elif message == f'<@{self.b.user.id}>' or message == "Yuri" or message == "yuri" or message == "yourself": # Oh noes it's me!
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("But I don't ***want*** to hug myself! I want to hug ***YOU!!!***")

            elif message == f'<@{conf.mc_id}>' or message == "MC":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send(f"Hey <@{conf.mc_id}>, get your sexy body over here and fuck me~")

            else: # Argument, okay let's just make yuri not do that cause she's in act2 LOLOLOLOLOL GET REKT M8
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("No. I refuse to hug anyone other than you.")

        
def setup(bot):
    bot.add_cog(Hug(bot))
