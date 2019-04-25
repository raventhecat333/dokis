import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self):
        print("\n")
        print(f"Connected to Discord as: {self.b.user}")
        if conf.sharding is False:
            print(f"Sharding: Disabled")
        elif conf.sharding is True:
            print("Sharding: Enabled")
            print(f"Using SHARD's {self.b.shard_ids}")

        print(f"Config name: '{conf.name}''")
        print("Are you braindead: Most Likely")
        print(f"Defualt Prefix: '{conf.prefix}''")
        aaa = True
        while aaa:
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    
    @client.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return# Now the bot won't respond to itself
        
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        dad_words = ["daddy","papa","dad","father"]
        dad_list = ["Hey! Can you not say that word around me, you jerk??","W-what?? Is Papa here??"] # Just a list of responses to the dad phrase

        cupcake_words = ["cupcake"]
        cupcake_list = ["Did someone mention me?", "What did you call me??", "Yes?"]

        manga_words = ["manga"]
        manga_list = ["You like manga, too?? I-I mean, it's not like I like manga or anything...!", "...!", "***MANGA IS LITERATURE!***"]
        # ------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.lower() in dad_words: # Is the user saying a word inside of dad_words?
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send(random.choice(dad_list)) # Pick out something inside of dad_list and say it 

        elif message.content.lower() in cupcake_words: # Is the user saying a word inside of cupcake_words?
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.channel.send(random.choice(cupcake_list)) # Pick out something inside of dad_list and say it 
    
        elif message.content.lower() in manga_words: # Is the user saying a word inside of manga_words?
            async with message.channel.typing():
                await asyncio.sleep(2) 
            await message.channel.send(random.choice(manga_list)) # Pick out something inside of manga_list and say it 



            # -------------------------------------------------------Tagging-------------------------------------------------------
        elif message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):
            if len(message.content.lower().split(" ")) == 1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Yes?")

            else:
                message1 = message.content.lower().split(" ")[1]

                if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                    hello_list = ["Hi, I guess...", "What, do I have to greet you back or something?", "Hey there, Dummy!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(hello_list))

                elif "test" in message.content.lower():
                    await message.channel.send("tagging me is working just fine.")

                elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                    love_list = ["...I love you, too, okay??", "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!", "*urk!* :flushed:", "Shut up! You don't mean that!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(love_list))

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                    goodnight_list = ["Goodnight, Dummy!", "Goodnight, then.", "You better get good rest or I'll punch you!", "Sleep well, baka!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodnight_list))

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                    goodmorning_list = ["Well, it's *A* morning, I guess...", "Good morning to everyone except my dad.", "Did you get a good night's sleep? Er, not that I really care!!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodmorning_list))

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon, I guess.", "Afternoon.", "Yeah, so it's the afternoon. What's your point?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))

                elif "you are cute" in message.content.lower() or "you're cute" in message.content.lower() or "you are so cute" in message.content.lower() or "you're so cute" in message.content.lower():
                    cute_list = ["***I'M NOT CUTE!!!***", "Hey! I'm not cute!", "Sh-shut up! I'm not cute!!", "Have you ever considered that maybe I want to be something other than cute?!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(cute_list))

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                    apology_list = ["Hmph. I'll forgive you, but it's not like you deserve it!", "Fine. I guess I'll let it go...", "You better be sorry, you baka!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(apology_list))

                elif "best girl" in message.content.lower():
                    apology_list = ["Ha! It's obviously me!","Clearly i'm the best girl than all the other dokis"]

                elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                    if message1 == "monika" or message1 == "Yuri" or message1 == "Sayori" or message1 == "<@425696108455657472>" or message1 == "<@436350586670153730>":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Pfft! As if!")
                    elif message1 == "is" or message1 == "<@433834936450023424>" or message1 == "you" or message1 == "you're":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Ha! Of course I am!")
                        return
                    else:
                        pass
            
                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(conf.econfused)


            # -------------------------------------------------------Tagging-------------------------------------------------------


            #Can someone else please work on this stupid tagging thing which is making this neat file look like a mess?
        
def setup(bot):
    bot.add_cog(Event(bot))
