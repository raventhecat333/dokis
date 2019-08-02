import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Feed(client.Cog):

    def __init__(self, bot):
         self.b = bot #

    @client.command()
    async def feed(self,ctx, arg1=None): 
        if arg1 is None:
            await ctx.send("H-hey! Don't feel like you have to feed me anything! I'm okay!")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send("A cookie?? Yummy! Thank you so much!")
         #------------------- Cookie ------------------- 


        elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Oooo! Japanese food! Reminds me of home!") 
        #------------------- Japenese Food ------------------- 


        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I love pizza! Thanks!") 
        #------------------- Pizza ------------------- 


        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Mmmmm! Burgers are delicious!") 
        #------------------- Burger ------------------- 


        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("AHH! Brain freeze!!")
        #------------------- Cold Foods ------------------- 


        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("H-Hey! I'm too young for that!")
        #------------------- Alcohol ------------------- 


        elif arg1 == "🍵":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("How could I refuse a hot cup of tea? Thank you!")
        #------------------- Tea -------------------  Who put soup in my Tea? 

        elif arg1 == "☕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, the delicious beverage known as coffee! Where would I be without thee?")
        #------------------- Coffee ------------------- '''


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
            await ctx.send("Sweets! My one, true weakness!! *omnomnomnomnom*")
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
            await ctx.send("It's not my birthday, but I accept!")
        #------------------- Birthday Cake ------------------- '''


        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("*om nom nom* Thank you! That was delicious! :grin:")
        #------------------- Misc ------------------- '''


        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ptoo ptoo! This isn't food, you meanie!")        
            #------------------- Not Listed ------------------- '''



def setup(bot):
    bot.add_cog(Feed(bot))
