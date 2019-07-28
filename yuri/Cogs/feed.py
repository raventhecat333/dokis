import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports

class Feed(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def feed(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        #---------------------------PM's---------------------------
        if ctx.guild is None:
            if arg1 is None:
                await ctx.send("Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
            
            elif arg1 == "🍪":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed) 
                await ctx.send("Oh, the chocolate chips just melt in my mouth!") 
            #------------------- Cookie ------------------- 


            elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...") 
            #------------------- Japenese Food ------------------- 


            elif arg1 == "🍕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("A slice of pizza never hurt, right...?") 
            #------------------- Pizza ------------------- 


            elif arg1 == "🍔":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Fast food? I-I suppose that'll do.") 
            #------------------- Burger ------------------- 


            elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
            #------------------- Cold Foods ------------------- 


            elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Alcohol ------------------- 

            elif arg1 == "🍷":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Wine ------------------- 

            elif arg1 == "☕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm more of a tea drinker. I'm sorry...")
            #------------------- Coffee -------------------  Who put soup in my coffee? 


            elif arg1 == "🍵":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, thank you so much. All I need now is a good book.")
            #------------------- Tea -------------------


            elif arg1 == "🍞" or arg1 == "🥖":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hm... I suppose I need more ingredients than this, don't you think?")
            #------------------- Bread ------------------- 


            elif arg1 == "🌶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("O-Oh! Oh my goodness! That has quite a kick!!")
            #------------------- Hot Pepper ------------------- '''


            elif arg1 == "🍳":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I didn't know you knew how to cook eggs!")
            #------------------- Cooking ------------------- '''


            elif arg1 == "🌮" or arg1 == "🌯":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
            #------------------- Mexican -------------------  Does that include burritos?


            elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I suppose a sweet wouldn't be such a bad idea...")
            #------------------- Sweets ------------------- '''

            elif arg1 == "🍫":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send("Oh! This brings up some... memories... with MC...")

            elif arg1 == "🍿":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("*crunch crunch crunch*")
            #------------------- Popcorn ------------------- '''

            elif arg1 == "🍼" or arg1 == "🍭":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
            #------------------- Baby Bottle ------------------- '''

            elif arg1 == "🥚":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, is it hard-boiled? Oh... no, it's not...")
            #------------------- Egg ------------------- '''


            elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, I'm generally used to chopsticks, but silverware will suffice.")
            #------------------- Silverware ------------------- '''
            

            elif arg1 == "🥛":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Th-Thank you. I love a nice glass of milk.")
            #------------------- Milk ------------------- '''
            

            elif arg1 == "🎂":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
            #------------------- Birthday Cake ------------------- '''


            elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, you didn't really have to, but thank you so much. *munch munch*")
            #------------------- Misc ------------------- '''


            else:
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uuuu!! Th-that's not food!")        
                #------------------- Not Listed ------------------- '''
        #---------------------------PM's---------------------------



        #---------------------------Act1---------------------------
        if ctx.guild.id not in conf.act2:
            if arg1 is None:
                await ctx.send("Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
            
            elif arg1 == "🍪":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed) 
                await ctx.send("Oh, the chocolate chips just melt in my mouth!") 
            #------------------- Cookie ------------------- 


            elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...") 
            #------------------- Japenese Food ------------------- 


            elif arg1 == "🍕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("A slice of pizza never hurt, right...?") 
            #------------------- Pizza ------------------- 


            elif arg1 == "🍔":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Fast food? I-I suppose that'll do.") 
            #------------------- Burger ------------------- 


            elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
            #------------------- Cold Foods ------------------- 


            elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Alcohol ------------------- 

            elif arg1 == "🍷":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Wine ------------------- 

            elif arg1 == "🍵":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm more of a tea drinker. I'm sorry...")
            #------------------- Coffee -------------------  Who put soup in my coffee? 


            elif arg1 == "☕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, thank you so much. All I need now is a good book.")
            #------------------- Tea ------------------- '''


            elif arg1 == "🍞" or arg1 == "🥖":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hm... I suppose I need more ingredients than this, don't you think?")
            #------------------- Bread ------------------- 


            elif arg1 == "🌶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("O-Oh! Oh my goodness! That has quite a kick!!")
            #------------------- Hot Pepper ------------------- '''


            elif arg1 == "🍳":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I didn't know you knew how to cook eggs!")
            #------------------- Cooking ------------------- '''


            elif arg1 == "🌮" or arg1 == "🌯":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
            #------------------- Mexican -------------------  Does that include burritos?


            elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I suppose a sweet wouldn't be such a bad idea...")
            #------------------- Sweets ------------------- '''

            elif arg1 == "🍫":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send("Oh! This brings up some... memories... with MC...")

            elif arg1 == "🍿":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("*crunch crunch crunch*")
            #------------------- Popcorn ------------------- '''

            elif arg1 == "🍼" or arg1 == "🍭":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
            #------------------- Baby Bottle ------------------- '''

            elif arg1 == "🥚":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, is it hard-boiled? Oh... no, it's not...")
            #------------------- Egg ------------------- '''


            elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, I'm generally used to chopsticks, but silverware will suffice.")
            #------------------- Silverware ------------------- '''
            

            elif arg1 == "🥛":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Th-Thank you. I love a nice glass of milk.")
            #------------------- Milk ------------------- '''
            

            elif arg1 == "🎂":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
            #------------------- Birthday Cake ------------------- '''


            elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, you didn't really have to, but thank you so much. *munch munch*")
            #------------------- Misc ------------------- '''


            else:
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uuuu!! Th-that's not food!")        
                #------------------- Not Listed ------------------- '''






        #---------------------------Act2---------------------------
        elif ctx.guild.id in conf.act2:            
            if arg1 is None:
                await ctx.send("I'll eat anything you like, Darling. Anything.")
            

            elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I'm too young for this, but I'll drink it because you want me to! *chugs*")
            #------------------- Alcohol ------------------- 

            elif arg1 == "🍼" or arg1 == "🍭":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, are you into that kind of thing? Well, I'll happily play along for you. Wah! Waah!")
            #------------------- Baby Bottle ------------------- 

            elif arg1 == "🥚":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uhuhuhu! Raw eggs? Now you're just being silly, but I'll still accept!")
            #------------------- Egg ------------------- 


            elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Well, I'll admit that it wasn't as disgusting as I had originally assumed!")
            #------------------- Silverware ------------------- 
            

            elif arg1 == "🎂":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("It's not my birthday, but I'll still eat this cake!")
            #------------------- Birthday Cake ------------------- 


            elif arg1 == "🍆":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Mmmm.... I wish this was your long, hard cock... :smirk: I can shove it all the way down my throat, if you'd like...")
            #------------------- Eggplant ------------------- 


            elif arg1 == "🍑":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("It's so sweet and juicy... I just wanna lick all the juices up!")
            #------------------- Peach ------------------- 
 

            elif arg1 == "🖊️":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I do believe this is the one with my juices on it. *licks* Mmm... Tasty...")
            #------------------- Pen ------------------- 


            elif arg1 == "🔪":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Mmmm.... I just wanna rub the blade across my tongue and taste the blood... Maybe I could let you taste it, as well...")
            #------------------- Knife ------------------- 



            else:
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("*munch munch munch* Does that please you, my beloved?")        
            #------------------- Not Listed ------------------- 

        #---------------------------Non Guild---------------------------
        else:
            if arg1 is None:
                await ctx.send("Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
            
            elif arg1 == "🍪":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed) 
                await ctx.send("Oh, the chocolate chips just melt in my mouth!") 
            #------------------- Cookie ------------------- 


            elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...") 
            #------------------- Japenese Food ------------------- 


            elif arg1 == "🍕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("A slice of pizza never hurt, right...?") 
            #------------------- Pizza ------------------- 


            elif arg1 == "🍔":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Fast food? I-I suppose that'll do.") 
            #------------------- Burger ------------------- 


            elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
            #------------------- Cold Foods ------------------- 


            elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Alcohol ------------------- 

            elif arg1 == "🍷":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("T-Thank you, but I'll have to kindly decline.")
            #------------------- Wine ------------------- 

            elif arg1 == "☕":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, thank you so much. All I need now is a good book.")
            #------------------- Coffee -------------------  Who put soup in my coffee? 


            elif arg1 == "🍵":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm more of a tea drinker. I'm sorry...")
            #------------------- Tea ------------------- '''


            elif arg1 == "🍞" or arg1 == "🥖":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hm... I suppose I need more ingredients than this, don't you think?")
            #------------------- Bread ------------------- 


            elif arg1 == "🌶":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("O-Oh! Oh my goodness! That has quite a kick!!")
            #------------------- Hot Pepper ------------------- '''


            elif arg1 == "🍳":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I didn't know you knew how to cook eggs!")
            #------------------- Cooking ------------------- '''


            elif arg1 == "🌮" or arg1 == "🌯":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
            #------------------- Mexican -------------------  Does that include burritos?


            elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I suppose a sweet wouldn't be such a bad idea...")
            #------------------- Sweets ------------------- '''

            elif arg1 == "🍫":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send("Oh! This brings up some... memories... with MC...")

            elif arg1 == "🍿":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("*crunch crunch crunch*")
            #------------------- Popcorn ------------------- '''

            elif arg1 == "🍼" or arg1 == "🍭":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
            #------------------- Baby Bottle ------------------- '''

            elif arg1 == "🥚":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, is it hard-boiled? Oh... no, it's not...")
            #------------------- Egg ------------------- '''


            elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Ah, I'm generally used to chopsticks, but silverware will suffice.")
            #------------------- Silverware ------------------- '''
            

            elif arg1 == "🥛":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Th-Thank you. I love a nice glass of milk.")
            #------------------- Milk ------------------- '''
            

            elif arg1 == "🎂":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
            #------------------- Birthday Cake ------------------- '''


            elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Oh, you didn't really have to, but thank you so much. *munch munch*")
            #------------------- Misc ------------------- '''


            else:
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send("Uuuu!! Th-that's not food!")        
                #------------------- Not Listed ------------------- '''



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Feed(bot))
