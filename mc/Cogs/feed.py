import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Feed(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def feed(self,ctx, arg1=None):
        if arg1 is None: # If you don't provide an emoji :P
            await ctx.send("It's fine, I brought my own food...")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send("I mean, it's not made by Natsuki but I'll eat it.")
        #------------------- Cookie ------------------- 

        elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I mean, it's from my homeland. *eats happily*") 
        #------------------- Japanese Food ------------------- 

        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Yay, pizza!") 
        #------------------- Pizza ------------------- 

        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Yay, I love hamburgers!") 
        #------------------- Burger ------------------- 

        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Burr, cold.")
        #------------------- Cold Foods ------------------- 

        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("What the fuck? I'm not drinking alcohol!")
        #------------------- Alcohol ------------------- 

        elif arg1 == "☕" or arg1 == "🍵":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Time to start the day...")
        #---------------- Coffee or Tea ----------------

        elif arg1 == "🍞" or arg1 == "🥖":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I mean, I suppose I could survive off of plain bread...")
        #------------------- Bread ------------------- 

        elif arg1 == "🌶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("***HOTHOTHOTHOTHOT!!!***")
        #------------------- Hot Pepper -------------------

        elif arg1 == "🍳":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ugh, breakfast foods, great.")
        #------------------- Cooking -------------------

        elif arg1 == "🌮" or arg1 == "🌯":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Noche de taco maravilloso!")
        #------------------- Mexican -------------------

        elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(f"Something sweet? For me? Thanks, <@{ctx.author.id}>")
        #------------------- Sweets -------------------

        elif arg1 == "🍿":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send("*crunch crunch crunch*")
        #------------------- Popcorn -------------------

        elif arg1 == "🍼" or arg1 == "🍭":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I'm-I'm not a baby...")
        #------------------- Baby Bottle -------------------

        elif arg1 == "🥚":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ugh, breakfast foods, great...")
        #------------------- Egg ------------------- '''

        elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Well, what are we eating?")
        #------------------- Silverware -------------------
        
        elif arg1 == "🥛":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, a nice, cold glass of milk is always welcoming!")
        #------------------- Milk -------------------
        
        elif arg1 == "🎂":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(f"It's not my birthday, and even if it was, I don't want a cake <@{ctx.author.id}>")
        #------------------- Birthday Cake -------------------

        elif arg1 == "🔪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I'm not Act 2 Yuri; feed that to her.")
        #------------------- Knife ------------------- 

        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Um, thanks? *eats the food*")
        #------------------- Misc -------------------

        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I don't think I can eat that.")        
        #------------------- Not Listed -------------------


def setup(bot):
    bot.add_cog(Feed(bot))
