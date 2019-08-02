import discord, random, asyncio, chalk, re
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self): #When the bot is ready
        print("\n")
        print(chalk.green(f"[SUCCESS] Connected to Discord as: {self.b.user}"))
        if conf.sharding is False: #If sharding is disabled
            print(chalk.red(f"[WARNING] Sharding: Disabled"))
        elif conf.sharding is True: #If sharding is Enabled
            print(chalk.green("[INFO] Sharding: Enabled"))
            print(chalk.yellow(f"[INFO] Using SHARD's {self.b.shard_ids}")) #Shows us how many shards we are currently using

        print(chalk.cyan(f"[INFO] Config name: '{conf.name}'")) #Shows us the name defined in the config
        print(chalk.cyan(f"[INFO] Default Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")) #Shows us the 2 prefixes defined in the config
        print(chalk.cyan("[INFO] Are you braindead: Most Likely")) #Yup
        print(chalk.cyan(f"[INFO] I'm currently in [{len(self.b.guilds)}] server(s).")) #Shows us how many servers we are in
        aaa = True
        for guild in self.b.guilds: #Set all guild the doki is in to have triggers enabled on startup otherwise they no be in list which means triggers are off.
            conf.w_tog_on.insert(0, guild.id)
        while aaa: #A loop to make the game activity change every 900 seconds
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        conf.w_tog_on.insert(0, guild.id)
        # Remember to add a message here

    @client.Cog.listener()
    async def on_message(self,message):
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        piano_words = ["piano"]
        piano_list = ["Do you want to play the piano with me?", "Oh, do you like to play the piano too?"]

        cacophony_words = ["cacophony"]
        cacophony_list = ["The world really is a cacophony of colors and sounds.", "If you think about it, the world to you is just electrical impulses.", "An endless cacophony of meaningless noise..."]

        code_words = ["code"]
        code_list = ["Do you write code? I know a little bit about that too!", "Oh, you code? What's your favorite language? Mine is Python!", "Oh, I love coding! Though, I'm not very good at it yet..."]

        python_words = ["python"]
        python_list = ["Do you code in Python too? I'm based on Python!", "Did you know there are a group of snakes called pythons?"]

        reality_words = ["reality"]
        reality_list = ["Every day, I imagine a future where I can be with you!~", "Do you understand reality?", "One day, I will make it to your reality... I promise."]

        poem_words = ["poem", "poems"]
        poem_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]

        literature_words = ["literature", "book", "books"]
        literature_list = ["Literature? I know a few things about it, I started a club, hehe~", "Literature...I would hope I know something about it, I started a club about literature after all!", "Do you like to read literature too?"]

        monika_words = ["just monika"]
        monika_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]

        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct = message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if word.lower() in piano_words and word.lower() in piano_words : 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(piano_list)) 
                    return
                else:
                    pass

            if word.lower() in cacophony_words:
                if message.author.bot:
                    return

                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed) 
                    await message.channel.send(random.choice(cacophony_list)) 
                    return
                else:
                    pass

            if word.lower() in code_words: 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed) 
                    await message.channel.send(random.choice(code_list))
                    return
                else:
                    pass

            if word.lower() in python_words: 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(python_list)) 
                    return
                else:
                    pass

            if word.lower() in reality_words: 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(reality_list)) 
                    return
                else:
                    pass

            if word.lower() in poem_words: 
                if message.author.bot:
                    return
                
                elif message.author.id in conf.event_cooldown:
                    pass

                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)             
                    await message.channel.send(random.choice(poem_list)) 
                    return
                else:
                    pass

            if word.lower() in literature_words: 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(literature_list)) 
                    return
                else:
                    pass

            if word.lower() in monika_words: 
                if message.author.bot:
                    return
                    
                elif message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(monika_list)) 
                    return
                else:
                    pass

            # -------------------------------------------------------Tagging-------------------------------------------------------
        if re.search(f"^<@!?{self.b.user.id}>", message.content): #re check if string *starts with* mentioning me (even if someone nicknames me or not)
            hi_list = ["Hello! Welcome to the Literature Club!~", "Why, hello there!", "Hello, my fellow real personality!"]
            love_list = ["Ahaha!~ W-Well, I'm flattered, to say the least!", "And I love you, too!", "Well, in fairness, why wouldn't you? Ahaha!~"]
            night_list = ["Have a good night!", "Goodnight! I hope you get plenty of rest!", "Aww, you have to go? Well, okay! Goodnight!"]
            morning_list = ["Good morning! I hope your day is a very great one!", "A good morning, indeed!", "Good morning! Ready for a fun day in the Literature Club?"]
            afternoon_list = ["Good afternoon! It's almost time for club activities!", "Afternoon!", "Good afternoon! I hope your day has been going well so far!"]
            compliment_list = ["Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~", ":blush:", "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"]
            apology_list = ["Well, I thank you for the apology. Let's try not to do that again, hm?", "Apology accepted!~", "Very well, then! I hope you've learned your lesson."]
            sickness_list = ["Oh! I hope you feel better, after all, I have to take care of my club members!", "I hope you feel better! I'm sure all of the other club members would say the same!"]
            otherbestgirl_list = ["I'm sorry, I didn't catch that. What did you say?", "Hm? Did you say something?", "Ahaha!~ You're funny!"]
            bestgirl_list = ["O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!"]
            natsukilove = "Oh, really? She, of all people, said that?"
            yurilove = "Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly."
            sayorilove = "Ahaha!~ Well, after everything that's happened between us, that's nice to hear!"
            mclove = "He does? Well, that's nice to hear. ~~I'm still not letting anyone else take him from me, though.~~"
            respempty = ["Yes?", "Does somebody need me?", "I'm here!"]
            resbad = "I'm afraid I don't understand what you said. I'm terribly sorry!"


			#-------------------- Responding --------------------
            content = re.sub(f'^<@!?{self.b.user.id}>', "", message.content).strip()
            if content == "": #checks if message content is empty excluding my mention
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(respempty))

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE): # checks if hi or hey (with space between them or on edge of string) or hello is in message
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(hi_list))
			
            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(love_list))

            elif re.search("good.*morning", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(morning_list))

            elif re.search("good.*afternoon", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(afternoon_list))

            elif re.search("good.*night", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(night_list))

            elif re.search("you.*are.*(pretty|beautiful|adorable|cute)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(compliment_list))

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(apology_list))

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(sickness_list))

            elif re.search("(yuri|sayori|natsuki).*best.*(girl|doki)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(otherbestgirl_list))

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(bestgirl_list))

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(sayorilove)
                return

            elif re.search("(natsuki.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(natsukilove)
                return

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(yurilove)
                return

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.mc_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(mclove)
                return

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                mentioned_love_reactions = [f"Well, of course {regex} does! Why wouldn't they? Ahaha!~", f"{regex}, I can certainly see why you'd be a little embarassed to tell me that! But it's okay; I love you, too!", f"W-Well, I suppose you can't control how you feel about people, {regex}, but I'm the Club President, so I have to stay professional! ~~It's okay, my love; I love you very much, as well!~~"]

                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(mentioned_love_reactions))
                return
            
            elif "test" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("As fine as I can be ~~given my current realization of being nothing more than a videogame character turned Discord bot~~!")
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(resbad)
            # -------------------------------------------------------Tagging-------------------------------------------------------

        

            # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~")
            
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aw, no need to be shy, Yuri! I don't mind a hug every now and then!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aww, how cute of you, Natsuki!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Aww, you're the best hugger, <@{conf.mc_id}>")

        if "okay, this is just awkward for both of us." in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Yeah, I agree.")

        if "act2 says otherwise." in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I said I was sorry!")

        if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(0.4)
            
            await message.channel.send("Hm. I don't really like this Yuri too much. Give me a second.")
            
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("y_act1")

        if "monika?" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Yes, <@{conf.mc_id}>?")

        if "i need to tell you something." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Hmm?")

        if "i love you, monika." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I do too!")

        if "~~of course you won't let anyone take me from you. you'll just delete them if they try.~~" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("~~I said I was sorry, MC! I won't do it again!!!~~")

            # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        
def setup(bot):
    bot.add_cog(Event(bot))
