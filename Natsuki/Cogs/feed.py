import discord, random, asyncio
from discord.ext import commands
#Imports


class General(commands.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @commands.command()
    async def feed(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("Hey! You wanted to ask me something so what is it?!")
            
        elif arg1 == u"\U0001F36A":#Cookie
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("I suppose a cookie wouldn't hurt.") #Cookie
        #------------------- Cookie ------------------- 


        elif arg1 == u"\U0001F363" or arg1 == u"\U0001F371" or arg1 == u"\U0001F35B" or arg1 == u"\U0001F359" or arg1 == u"\U0001F35A" or arg1 == u"\U0001F358" or arg1 == u"\U0001F35C" or arg1 == u"\U0001F362" or arg1 == u"\U0001F361" or arg1 == u"\U0001F365":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Ah, this is a more familiar meal.") #Sushi
        #------------------- Sushi ------------------- 


        elif arg1 == u"\U0001F355":#Pizza
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("F-fine, I'll have a slice.") #Pizza
        #------------------- Pizza ------------------- 


        elif arg1 == u"\U0001F354":#Pizza
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("...only because there's cheese on it...") #Pizza
        #------------------- Burger ------------------- 


        elif arg1 == u"\U0001F367" or arg1 == u"\U0001F366" or arg1 == u"\U0001F368":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Thanks, I guess. I was actually feeling a bit warm.")
        #------------------- Cold Foods ------------------- 


        elif arg1 == u"\U0001F37A" or arg1 == u"\U0001F37B" or arg1 == u"\U0001F377" or arg1 == u"\U0001F378" or arg1 == u"\U0001F379" or arg1 == u"\U0001F37E" or arg1 == u"\U0001F376" or arg1 == u"\U0001F942" or arg1 == u"\U0001F943":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Hey, what's the idea?? You trying to get me drunk??")
        #------------------- Alcohol ------------------- 


        elif arg1 == u"\u2615":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("I don't really like coffee that much, but thanks, anyway.")
        #------------------- Coffee -------------------  Who put soup in my coffee? 


        elif arg1 == u"\U0001F375":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("I don't really like coffee that much, but thanks, anyway.")
        #------------------- Tea ------------------- '''


        elif arg1 == u"\U0001F35E" or arg1 == u"\U0001F956":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Well, it's more than Papa gives me...")
        #------------------- Bread ------------------- 


        elif arg1 == u"\U0001F336":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("H-Hey!! My freaking mouth is on fire!!!")
        #------------------- Hot Pepper ------------------- '''


        elif arg1 == u"\U0001F373":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Sunny-side up? How did you know that's how I liked them?")
        #------------------- Cooking ------------------- '''


        elif arg1 == u"\U0001F32E" or arg1 == u"\U0001F32F":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Mexican, huh? Not my first choice, but it's still pretty good...")
        #------------------- Mexican -------------------  Does that include burritos?


        elif arg1 == u"\U0001F370" or arg1 == u"\U0001F36E" or arg1 == u"\U0001F36C" or arg1 == u"\U0001F36B" or arg1 == u"\U0001F369":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Well, I suppose it would be nice to eat a sweet that I didn't bake, for once.")
        #------------------- Sweets ------------------- '''


        elif arg1 == u"\U0001F37F":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("*crunch crunch crunch*")
        #------------------- Popcorn ------------------- '''

        elif arg1 == u"\U0001F37C" or arg1 == u"\U0001F36D":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("I feel like there's a loli joke to be made here...")
        #------------------- Baby Bottle ------------------- '''

        elif arg1 == u"\U0001F95A":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("*crunch crunch crunch*")
        #------------------- Egg ------------------- '''


        elif arg1 == u"\U0001F374" or arg1 == u"\U0001F37D" or arg1 == u"\U0001F944":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("I'd prefer actual food here, please! N-not that you have to give me any or anything...")
        #------------------- Silverware ------------------- '''
        

        elif arg1 == u"\U0001F95B":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("What, you didn't have strawberry milk?? Ah, whatever. I guess this is fine...")
        #------------------- Milk ------------------- '''
        

        elif arg1 == u"\U0001F382":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Huh? It's not my birthday!")
        #------------------- Birthday Cake ------------------- '''


        elif arg1 == u"\U0001F34E" or arg1 == u"\U0001F34F" or arg1 == u"\U0001F350" or arg1 == u"\U0001F34A" or arg1 == u"\U0001F34B" or arg1 == u"\U0001F34C" or arg1 == u"\U0001F349" or arg1 == u"\U0001F347" or arg1 == u"\U0001F353" or arg1 == u"\U0001F348" or arg1 == u"\U0001F352" or arg1 == u"\U0001F351" or arg1 == u"\U0001F34D" or arg1 == u"\U0001F345" or arg1 == u"\U0001F346" or arg1 == u"\U0001F33D" or arg1 == u"\U0001F360" or arg1 == u"\U0001F36F" or arg1 == u"\U0001F357" or arg1 == u"\U0001F356" or arg1 == u"\U0001F364" or arg1 == u"\U0001F35F" or arg1 == u"\U0001F32D" or arg1 == u"\U0001F35D" or arg1 == u"\U0001F950" or arg1 == u"\U0001F951" or arg1 == u"\U0001F952" or arg1 == u"\U0001F953" or arg1 == u"\U0001F954" or arg1 == u"\U0001F955" or arg1 == u"\U0001F957" or arg1 == u"\U0001F958" or arg1 == u"\U0001F959" or arg1 == u"\U0001F95C" or arg1 == u"\U0001F95D" or arg1 == u"\U0001F95E" or arg1 == u"\U0001F9C0":
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("...t-thank you. *slowly eats*")
        #------------------- Misc ------------------- '''


        else:
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await ctx.send("Are you trying to kill me?? That's not food!")        
            #------------------- Not Listed ------------------- '''



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(General(bot))
