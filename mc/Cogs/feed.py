import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Feed(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.guild_only()
    async def feed(self,ctx, arg1=None):
        if arg1 is None: # If you don't provide an emoji :P
            await ctx.send("It's fine, I brought my own food...")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send("A cookie?? Yummy! Thank you so much!")
        #------------------- Cookie ------------------- 

        elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I mean, it's from my homeland. *eats happily*") 
        #------------------- Japanese Food ------------------- 

        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Pizza, eh? Ok, then. *eats*") 
        #------------------- Pizza ------------------- 

        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("A burger? I'm not sure about this...") 
        #------------------- Burger ------------------- 

        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("AHH! Brain freeze!!")
        #------------------- Cold Foods ------------------- 

        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("What the fuck? I'm not drinking alcohol!")
        #------------------- Alcohol ------------------- 

        elif arg1 == "☕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("How could I refuse a hot cup of tea? Thank you!")
        #------------------- Coffee -------------------  Who put soup in my coffee? 

        elif arg1 == "🍵":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, the delicious beverage known as coffee! Where would I be without thee?")
        #------------------- Tea ------------------- '''

        elif arg1 == "🍞" or arg1 == "🥖":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I mean, I suppose I could survive off of plain bread...")
        #------------------- Bread ------------------- 

        elif arg1 == "🌶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("***OWOWOWOWHOTHOTHOTHOT!!!***")
        #------------------- Hot Pepper ------------------- '''

        elif arg1 == "🍳":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I made eggs and toast!")
        #------------------- Cooking ------------------- '''

        elif arg1 == "🌮" or arg1 == "🌯":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ole!")
        #------------------- Mexican -------------------  Does that include burritos?

        elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(f"Something sweet? For me? Thanks, {ctx.author.id}")
        #------------------- Sweets ------------------- '''

        elif arg1 == "🍿":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("*crunch crunch crunch*")
        #------------------- Popcorn ------------------- '''

        elif arg1 == "🍼" or arg1 == "🍭":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Hey! I'm not a baby!")
        #------------------- Baby Bottle ------------------- '''

        elif arg1 == "🥚":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I feel like I should cook this, first...")
        #------------------- Egg ------------------- '''

        elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I didn't know you could eat silverware!")
        #------------------- Silverware ------------------- '''
        
        elif arg1 == "🥛":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, a nice, cold glass of milk is always welcoming!")
        #------------------- Milk ------------------- '''
        
        elif arg1 == "🎂":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(f"It's not my birthday, and even if it was, I don't want a cake {ctx.author.id}")
        #------------------- Birthday Cake ------------------- '''

        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Um, thanks? *eats the food*")
        #------------------- Misc ------------------- '''

        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ptoo ptoo! This isn't food, you meanie!")        
        #------------------- Not Listed ------------------- '''


def setup(bot):
    bot.add_cog(Feed(bot))
