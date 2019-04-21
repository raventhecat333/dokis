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
        chat_filter = ["nigger"]

        name_words = ["cinnamon bun", "best girl"]
        name_list = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]

        goodnight_words = ["goodnight", "gn", "goodnight,", "goodnight!"]
        goodnight_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]

        breakfast_words = ["breakfast"]
        breakfast_list = ["i want breakfast"]

        hang_words = ["hang", "hanging", "hung", "hanged"]
        hang_list = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
        suicide_list = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]

        kill_words = ["kill"]
        kill_list = []
        # ------------------------------------------------------------------------------------------------------------------------------------------------

        if message.content.lower() in name_words: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(random.choice(name_list)) 

        elif message.content.lower() in hang_words: 
            if message.author.id == self.bot.user.id:
                pass

            elif message.content.upper().startswith(f"<@{self.bot.user.id}>"):
                pass

            elif "myself" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await channel.send(random.choice(suicide_list))
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await channel.send(random.choice(hang_list))
            
        elif message.content.lower() in breakfast_words: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send(random.choice(breakfast_list)) 


        elif message.content.lower() in goodnight_words: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send(random.choice(breakfast_list)) 

        elif message.content.lower() in chat_filter:
            await message.delete()
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Hey! Don't be a big meanie, <@{message.author.id}>!")

        elif message.content.lower() in kill_words: 
            if message.author.id == self.bot.user.id:
                pass

            elif message.content.upper().startswith(f"<@{self.bot.user.id}>"):
                pass

            elif "myself" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await channel.send(random.choice(suicide_list))
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await channel.send(random.choice("Can we change the topic to something more wholsem please?"))

            # -------------------------------------------------------Tagging-------------------------------------------------------
        elif message.content.lower().startswith(f"<@{self.b.user.id}>"):
            if len(message.content.lower().split(" ")) == 1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Yes?")

            else:
                message1 = message.content.lower().split(" ")[1]

                if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                    hello_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(hello_list))

                elif "test" in message.content.lower():
                    await message.channel.send("Testing, testing! 1-2-1-2 testing! Looks like it's working!")

                elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                    love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(love_list))

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodnight_list))

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                    goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodmorning_list))

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))

                elif "you are cute" in message.content.lower() or "you're cute" in message.content.lower() or "you are beautiful" in message.content.lower() or "you're beautiful" in message.content.lower():
                    cute_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(cute_list))

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                    apology_reactions = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(apology_list))

                elif 'loves you' in message.content.lower():
                    love_tag_list = [f"Aww! Well, you can tell {member} that I love them, too!", f"{member} does? Well, that's so sweet to hear!", f"And I love {member}, too! :heart:", f"Yay! I'm loved by {member}!"]
                    if 'nigger' in message.content.lower():
                        pass

                    elif member == f'<@{conf.natsuki_id}>': #Natsuki
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await channel.send("Awww, she does??")
                        return
                        
                    elif member == f'<@{conf.yuri_id}>': #Yuri
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await channel.send("Well, of course she does! Yuri loves everybody!")
                    
                    elif member == f'<@{conf.monika_id}>': #Monika
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await channel.send("Yay! I'm glad she does!")
                    
                    elif member == 'everyone' or member == '@everyone' or member == '@here' or member == 'everybody':
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await channel.send("R-really? EVERYONE? Oh, my!")
                        return
                    
                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await channel.send(random.choice(love_tag_list))


                elif 'syka blyat' in message.content.lower() or 'pidor ebony' in message.content.lower():
                    russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await channel.send(random.choice(russian_reactions))
                    return

                elif "best girl" in message.content.lower():
                    best_girl = ["Ha! It's obviously me!","Clearly i'm the best girl than all the other dokis"]

            elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                if message1 == "Monika" or message1 == "Natsuki" or message1 == "Yuri" or message1 == "<@436350586670153730>" or message1 == "<@433834936450023424>":
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await channel.send("Well, I respect your opinion!")
                    return
                elif message1 == "is" or message1 == "<@436350586670153730>" or message1 == "you" or message1 == "you're":
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await channel.send("S-Stop it! That's not true!")
                    return
                
                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    no_responses = ["Huh? I don't understand.", "I don't get it.", "???", "Maybe try something I actually understand?"]  
                    await message.channel.send(random_choice(no_responses))


            # -------------------------------------------------------Tagging-------------------------------------------------------


            #Can someone else please work on this stupid tagging thing which is making this neat file look like a mess?
        
def setup(bot):
    bot.add_cog(Event(bot))

























































#My body, my body is, my body is ready! My body is ready! My bo-bo-bo-body is ready! My body, my body i-, my body is ready! My-my-my body is ready! My body is-body is- b-b-b body is ready! My body, my body is, my body is ready! My body is ready! My bo-bo-bo-body is ready! My body, my body i-, my body is ready! My-my-my body is ready! My body is-body is- b-b-b body is ready! My body, my body is, my body is ready! My body is ready! My bo-bo-bo-body is ready! My body, my body i-, my body is ready! My-my-my body is ready! My body is-body is- b-b-b body is ready!  
