import discord, random, asyncio
from discord.ext import commands
from Cogs.config import conf
#Imports 


class Event(commands.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\n")
        print("Connected to Discord as: {}")
        if conf.sharding is False:
            print(f"Sharding: Disabled")
        elif conf.sharding is True:
            print("Sharding: Enabled")
        print(f"Config name: {conf.name}")
        print("Are you braindead: Most Likely")
        print(f"Defualt Prefix: {conf.prefix}")
        await self.b.change_presence(activity=discord.Game(name='Online', status=discord.Status.online))


    
    @commands.Cog.listener()
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


        
def setup(bot):
    bot.add_cog(Event(bot))
