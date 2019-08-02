import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Feed(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def feed(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("I suppose I am a bit hungry... What do you recommend?")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send("Not as homemade as Natsuki's, but it's still very delicious! Thank you!") 
        #------------------- Cookie ------------------- 


        elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Aw, you brought me a meal from my home? How thoughtful of you!") 
        #------------------- Japenese Food ------------------- 


        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah... There's pepperoni on it... You do remember I'm a vegetarian, right?") 
        #------------------- Pizza ------------------- 


        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Is it a veggie burger? If not, I'll have to respectfully decline.") 
        #------------------- Burger ------------------- 


        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, nothing like some cold treats to brighten your day!")
        #------------------- Cold Foods ------------------- 


        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Oh! Ahaha... A-As curious as I am, I'm afraid I cannot allow alcoholic beverages here.")
        #------------------- Alcohol ------------------- 


        elif arg1 == "☕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Ah, thank you! I've been needing something to wake me up a bit!")
        #------------------- Coffee -------------------  Who put soup in my coffee? 


        elif arg1 == "🍵":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("It's like I'm back in the clubroom! All I need is one of Natsuki's cupcakes.")
        #------------------- Tea ------------------- '''


        elif arg1 == "🍞" or arg1 == "🥖":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("It's a start, but I'll need to go to the grocery store to make a proper sandwich. ~~Would you like to come with?~~")
        #------------------- Bread ------------------- 


        elif arg1 == "🌶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("*cough cough* Oh, my! That certainly caught me off-guard!")
        #------------------- Hot Pepper ------------------- '''


        elif arg1 == "🍳":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Hm... as a vegetarian, would it even be okay to eat this...?")
        #------------------- Cooking ------------------- '''


        elif arg1 == "🌮" or arg1 == "🌯":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Well, I'm always in the mood for something different!")
        #------------------- Mexican -------------------  Does that include burritos?


        elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Sweets! A girl's best friend!")
        #------------------- Sweets ------------------- '''


        elif arg1 == "🍿":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("*crunch crunch crunch*")
        #------------------- Popcorn ------------------- '''

        elif arg1 == "🍼" or arg1 == "🍭":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("U-Um... I'm not sure what you're insinuating here...")
        #------------------- Baby Bottle ------------------- '''

        elif arg1 == "🥚":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Oh, you silly goose! Are you trying to be funny?")
        #------------------- Egg ------------------- '''


        elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I've got my silverware ready! What are we eating with them?")
        #------------------- Silverware ------------------- '''
        

        elif arg1 == "🥛":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I suppose it's a good thing I'm not a vegan! Ahaha~!")
        #------------------- Milk ------------------- '''
        

        elif arg1 == "🎂":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("How wonderful, but I don't believe it's my birthday just yet...")
        #------------------- Birthday Cake ------------------- '''


        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("A nice meal is always great! Thank you~")
        #------------------- Misc ------------------- '''


        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Um.. not to be rude, but I don't think this is edible.")        
            #------------------- Not Listed ------------------- '''



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Feed(bot))
