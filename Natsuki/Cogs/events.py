import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports 


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
        print(f"Config name: '{conf.name}''")
        print("Are you braindead: Most Likely")
        print(f"Defualt Prefix: '{conf.prefix}''")
        await self.b.change_presence(activity=discord.Game(name='Online', status=discord.Status.online))


    
    @client.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return# Now the bot won't respond to itself
        ''' ---------------------- ''' 
        dad_words = ["daddy","papa","dad","father"]
        dad_list = ["Hey! Can you not say that word around me, you jerk??","W-what?? Is Papa here??"] # Just a list of responses to the dad phrase

        cupcake_words = ["cupcake"]
        cupcake_list = ["Did someone mention me?", "What did you call me??", "Yes?"]

        manga_words = ["manga"]
        manga_list = ["You like manga, too?? I-I mean, it's not like I like manga or anything...!", "...!", "***MANGA IS LITERATURE!***"]
        ''' ---------------------- ''' 
        
        if message.content in dad_words: # Is the user saying a word inside of dad_words?
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await message.channel.send(random.choice(dad_list)) # Pick out something inside of dad_list and say it 

        elif message.content in cupcake_words: # Is the user saying a word inside of cupcake_words?
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            await message.channel.send(random.choice(cupcake_list)) # Pick out something inside of dad_list and say it 
    
        elif message.content in manga_words: # Is the user saying a word inside of manga_words?
            async with message.channel.typing():
                await asyncio.sleep(0.4) 
            await message.channel.send(random.choice(manga_list)) # Pick out something inside of manga_list and say it 



            # -------------------------------------------------------Tagging-------------------------------------------------------
        elif message.content.startswith(f"<@{self.b.user.id}>"):
            message1 = message.content.split(" ")
            if len(message1) == 1:
                await message.channel.send("Yes")

            elif "hi" in message.content or "hello" in message.content or "hey" in message.content:
                hello_list = ["Hi, I guess...", "What, do I have to greet you back or something?", "Hey there, Dummy!"]
                await message.channel.send(random.choice(hello_list))

            elif "test" in message.content:
                await message.channel.send("tagging me is working just fine.")

            elif "i love you" in message.content or "ily" in message.content:
                love_list = ["...I love you, too, okay??", "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!", "*urk!* :flushed:", "Shut up! You don't mean that!"]
                await message.channel.send(random.choice(love_list))

            elif "good night" in message.content or "goodnight" in message.content:
                goodnight_list = ["Goodnight, Dummy!", "Goodnight, then.", "You better get good rest or I'll punch you!", "Sleep well, baka!"]
                await message.channel.send(random.choice(goodnight_list))

            elif "good morning" in message.content or "goodmorning" in message.content:
                goodmorning_list = ["Well, it's *A* morning, I guess...", "Good morning to everyone except my dad.", "Did you get a good night's sleep? Er, not that I really care!!"]
                await message.channel.send(random.choice(goodmorning_list))

            elif "good afternoon" in message.content or "goodafternoon" in message.content:
                goodafternoon_list = ["Good afternoon, I guess.", "Afternoon.", "Yeah, so it's the afternoon. What's your point?"]
                await message.channel.send(random.choice(goodafternoon_list))

            elif "you are cute" in message.content or "you're cute" in message.content or "you are so cute" in message.content or "you're so cute" in message.content:
                cute_list = ["***I'M NOT CUTE!!!***", "Hey! I'm not cute!", "Sh-shut up! I'm not cute!!", "Have you ever considered that maybe I want to be something other than cute?!"]
                await message.channel.send(random.choice(cute_list))

            elif "i apologise" in message.content or "sorry" in message.content:
                apology_list = ["Hmph. I'll forgive you, but it's not like you deserve it!", "Fine. I guess I'll let it go...", "You better be sorry, you baka!"]
                await message.channel.send(random.choice(apology_list))

            elif "best girl" in message.content:
                apology_list = ["Ha! It's obviously me!","Clearly i'm the best girl than all the other dokis"]

            # -------------------------------------------------------Tagging-------------------------------------------------------


            #Can someone else please work on this stupid tagging thing which is making this neat file look like a mess?
        
def setup(bot):
    bot.add_cog(Event(bot))
