import discord, random, asyncio, chalk
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog):

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
        print(chalk.cyan(f"[INFO] Defualt Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")) #Shows us the 2 prefixes defined in the config
        print(chalk.cyan("[INFO] Are you braindead: Most Likely")) #Yup
        print(chalk.cyan(f"[INFO] I'm currently in [{len(self.b.guilds)}] server(s).")) #Shows us how many servers we are in
        aaa = True
        for guild in self.b.guilds: #Set all guild the doki is in to have triggers enabled on startup otherwise they no be in list which means triggers are off.
            conf.w_tog_on.insert(0, guild.id)
            conf.act1.insert(0,guild.id)
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
        if message.author.id == self.b.user.id:
            pass
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        cut_words = ["cut", "cutting", "cuts", "stab", "stabbing", "stabs"]
        cut_list = ["Uuu...!", "D-Did you have to say that word...?", "I-I'm sorry, I-I really don't like that word...", ":confounded:"]
        cut_list_act_2 = ["Oooo, yes. Say that again, please.", "Hahaha! I love your twisted sense of humor! It makes me so wet...", "Oh, I love it when you say that word... it makes me want to cut you and lick all the blood off."]

        knife_words = ["knife", "knifes"]
        knife_list = ["Y-You know, I'm a fan of knives...", "Do you like knives, as well?"]
        knife_list_act2 = ["Ahahaha! Did someone mention knives...?!", "Oh, I love knives! The way the sharp blade slides along skin is just beautiful!", "Oh, just hearing that word makes me feel so... Ahaha..."]

        pen_words = ["pen", "pens"]
        pen_list = ["I-I get the feeling you're insulting me by mentioning pens...", "Uuu...! Why did Monika have to make me do...things...? Now I can't think of pens the same way again...!! :cold_sweat:", "I-I only use pens for writing, I swear!!"]
        pen_list_act2 = ["I still have the pen I stole from MC... I even still use it from time to time...", "Hahaha. Are you expecting me to do something naughty with a pen? Because I just might if you ask nicely...", "Oh... Oh...! OH!!! YES, YES, YESYESYES!!!"]
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct = message.content.lower().split(" ") # (MCT | Meesage Contents) 
        for word in mct:
            if word.lower() in cut_words: #Cut trigger words
                if message.guild.id in conf.w_tog_on:
                    if message.author.bot:
                        return

                    if message.guild.id not in conf.act2: #This is incase the guild that this command was used in is set to act1
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(cut_list)) 
                        return 

                    elif message.guild.id in conf.act2:  #This is incase the guild that this command was used in is set to act2
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(cut_list_act_2)) 
                        return

                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(cut_list)) 
                        return 

                else:
                    pass

            if word.lower() in knife_words:
                if message.guild.id in conf.w_tog_on:
                    if message.author.bot:
                        return

                    if message.guild.id not in conf.act2: #This is incase the guild that this command was used in is set to act1
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(knife_list)) 
                        return

                    elif message.guild.id in conf.act2: #This is incase the guild that this command was used in is set to act2
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(knife_list_act2)) 
                        return

                    else: #Just incase the user is in a PM
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(knife_list)) 
                        return

                else:
                    pass

            if word.lower() in pen_words: #Pen word trigger words
                if message.guild.id in conf.w_tog_on:
                    if message.author.bot:
                        return

                    if message.guild.id not in conf.act2: #This is incase the guild that this command was used in is set to act1
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(pen_list)) 
                        return

                    elif message.guild.id in conf.act2: #This is incase the guild that this command was used in is set to act2
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(pen_list_act2)) 
                        return
                    
                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send(random.choice(pen_list)) 
                        return

                else:   
                    pass


            # -------------------------------------------------------Tagging-------------------------------------------------------
        if message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):

            #-------------------- Act 1 --------------------
            if message.guild.id not in conf.act2: 
                if len(message.content.lower().split(" ")) == 1:
                    tag_react_list1 = ["Y-Yes...?", "Did you want to talk to me...?", "Hm?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(tag_react_list1))
                    return

                else:
                    message1 = message.content.lower().split(" ")[1]

                    if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                        hello_list1 = ["H-Hello there.", "...h-hi...", "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(hello_list1))
                        return

                    elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                        love_list1 = ["O-Oh! W-W-Well, uhh... :flushed:", "I-I love you, too... :relaxed:", "R-Really? Why? I-I don't have anything worth loving...", "Uuu, why is my heart beating so fast right now??"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_list1))
                        return

                    elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                        goodnight_list1 = ["G-Goodnight, then.", "Until next time.", "I hope you have wonderful dreams!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodnight_list1))
                        return

                    elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                        goodmorning_list1 = ["It is a good morning, indeed.", "I hope you slept wonderfully!", "Good morning!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodmorning_list1))
                        return

                    elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                        goodafternoon_list1 = ["Good afternoon.", "A truly beautiful afternoon, it is.", "Ah, it's times like this where I just want to sit outsite and read a good book."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodafternoon_list1))
                        return

                    elif "you are" in message.content.lower() or "you're" in message.content.lower():
                        if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower():   
                            compliment_list1 = ["Y-You really think so...?", "Uuu... :flushed:", "T-Thank you. I needed to hear that...", ":blush:"]
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(compliment_list1))
                            return    

                    elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                        apology_list1 = ["I don't think I fully understand why you're apologizing, but I accept it, anyway.", "It's alright; I forgive you.", "N-No, I'm the one who should be sorry; I mess up everything...", "Consider your apology accepted, then!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(apology_list1))
                        return

                    elif "i'm sick" in message.content.lower() or "puke" in message.content.lower() or "not feeling good" in message.content.lower() or "not feeling great" in message.content.lower():
                        gwell_list1 = ["O-Oh... I hope y-you feel better soon.", "Oh... please do feel better."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(gwell_list1))
                        return

                    elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                        if "monika" in message1.lower() or "natsuki" in message1.lower() or "sayori" in message1.lower() or message1 == f"<@{conf.monika_id}>" or message1 == f"<@{conf.natsuki_id}>" or message1 == f"<@{conf.sayori_id}>":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("W-Well, I suppose that's true; she's much better than I am...")
                            return

                        elif message1 == "is" or message1 == f"<@{conf.yuri_id}>" or message1 == "you" or message1 == "you're":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("Oh! Uh... Well, I'm glad you think that!")
                            return
                        else:
                            pass

                    elif "test" in message.content.lower():
                        await message.channel.send("I-I believe I'm working properly... Oh, I hope I am...")
                        return

                    elif 'loves you' in message.content.lower():
                        member = message.content.split(" ")[1]
                        love_tag_list = [f"O-Oh, {member} does...? W-Well, that's nice to hear.", f"Uuu... I-I'm flattered, {member}...", f"R-Really? {member} loves me...?", f"W-Well... I-I think I love {member}, too...!"]
                        if 'nigger' in message.content.lower():
                            return

                        elif member == "everyone" or member == "@everyone" or member == "@here" or member == "everybody": #as seen in original
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("E-E-E-E-Everyone? :confounded:")
                            return

                        elif member == "loves":
                            await message.channel.send("Ehh?")
                            return

                        elif member.lower() == f'<@{conf.sayori_id}>': #Sayori
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("Haha. Well, she is a loving soul.")
                            return

                        elif member.lower() == f'<@{conf.natsuki_id}>': #Natsuki
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("Sh-She does?")
                            return

                        elif member.lower() == f'<@{conf.monika_id}>': #Monika
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("Ahaha... I-I'm glad that I have a friend like Monika who loves me... :blush:")
                            return

                        elif member.lower() == f'<@{conf.mc_id}>': #MC
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("Oh, d-does he now? Uhhhh...")
                            return

                        else:
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(love_tag_list))
                            return

                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf)
                        await message.channel.send("I-I'm sorry, but I don't understand what you mean...")
                        pass


            #-------------------- Act 2 --------------------
            elif message.guild.id in conf.act2:
                if len(message.content.lower().split(" ")) == 1:
                    tag_react_list2 = ["Yes, my love?", "Oh, did someone call for me?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(tag_react_list2))
                    return

                else:
                    message1 = message.content.lower().split(" ")[1]

                    if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                        hello_list2 = ["Hello there.", "Hello, my beloved! Nice to see you!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(hello_list2))
                        return

                    elif "test" in message.content.lower():
                        await message.channel.send("I'm working fine, I promise you! Can we just read already??")
                        return

                    elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                        love_list2 = ["I love you, too! I love you so much that I touch myself to you every night!", "I'm glad, because if you didn't, I'd be very, *very* upset...", ":smirk:", "...Ahahaha. Ahahahahahaha! Ahahahahahahahaha! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_list2))
                        return

                    elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                        goodnight_list2 = ["Haha. No. You're not allowed to go.", "Goodnight! I'll be sure to watch over you very closely while you're resting...", "I hope you don't mind if I look at your chest move up and down while the beautiful, soft breathing noises come from your mouth. Ahaha..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodnight_list2))
                        return

                    elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                        goodmorning_list2 = ["Good morning, my love!", "Oh, good! You're finally awake!", "Did you know you snore very loudly? Ahaha...", "Good morning! I can't wait to spend the day together! Just you and me, nobody else..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodmorning_list2))
                        return

                    elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                        goodafternoon_list2 = ["Good afternoon! But who cares what time it is; we'll be together forever, right??", "A perfect afternoon for just staring at each other, telling what kind of dirty things we could do together..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodafternoon_list2))
                        return

                    elif "you are" in message.content.lower() or "you're" in message.content.lower():
                        if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower():   
                            compliment_list2 = ["Ohoho, stop it, you! I'm nothing compared to you!", "But you're 10 times as amazing!", "no u", "Oh? Am I attractive enough for you to pleasure yourself to the thought of me? Because I do it to the thought of you all the time!", "Oh, I love it when you tell me that!"]
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(compliment_list2))
                            return    

                    elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                        apology_list2 = ["Ahaha. There's no need to be sorry. I honestly found it kinda hot...", "Well, if it'll make you feel better, I accept your apology.", "Uhuhu. You look so cute when you apologize like that!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(apology_list2))
                        return

                    elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                        if "monika" in message1.lower() or "natsuki" in message1.lower() or "sayori" in message1.lower() or message1 == f"<@{conf.monika_id}>" or message1 == f"<@{conf.natsuki_id}>" or message1 == f"<@{conf.sayori_id}>":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("No, she's fucking not.")
                            return

                        elif message1 == "is" or message1 == "<@{conf.yuri_id}>" or message1 == "you" or message1 == "you're":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
                            return
                        else:
                            pass

                    elif 'loves you' in message.content.lower():
                        member = message.content.split(" ")[1]
                        love_tag_list = [f"Ohoho, well I think it's safe to say that {member} doesn't love me as much as you do.", f"{member} does, do they? Well, I beg to differ.", f"I'm sorry, {member}, but I already have a lover, and they belong to me and me alone.", f"Well, I suppose I could touch myself to {member}, as well..."]
                        if 'nigger' in message.content.lower():
                            return

                        elif member == "everyone" or member == "@everyone" or member == "@here" or member == "everybody": #as seen in original
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("I bet everyone does, but not as much as I love you, you sexy thing!")
                            return

                        elif member == "loves":
                            await message.channel.send("Ehh?")
                            return

                        elif member.lower() == f'<@{conf.sayori_id}>': #Sayori
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("Who the hell is Sayori? I don't know any Sayoris...")
                            return

                        elif member.lower() == f'<@{conf.natsuki_id}>': #Natsuki
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("Pfft. As if. That immature brat doesn't love anyone but herself.")
                            return

                        elif member.lower() == f'<@{conf.monika_id}>': #Monika
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("I'll believe that when that bitch says it to my face!")
                            return

                        elif member.lower() == f'<@{conf.mc_id}>': #MC
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)
                            await message.channel.send("He better love me. I touch myself to him so often, I sometimes think my pen is his cock. :smirk:")
                            return

                        else:
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(love_tag_list))
                            return
                
                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("I love you, but I have no clue what you just said.")
                        pass
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("This could be a bug, but i'm not sure. What i do know is that this is an ELSE statement which is not usually meant to happen, try re-running y_act1 and see if that solves this. Sorry!")   
                return
            # -------------------------------------------------------Tagging-------------------------------------------------------



        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: #Monika
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Get your fucking hands off of me!!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh! Well, that was certainly unexpected!")

        
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id: #Monika
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Get your dirty, selfish hands off of me before I kill you and take your spot as President!!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("O-Oh! Well, uh, thank you, Monika.")
                        

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: #Sayori
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I'm sorry, who are you? And why are you hugging me?")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("H-Hey! Don't hug so hard, Sayori!")


        if "geez, yuri! don't make it all awkward!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I'm sorry...")

        if "w-well it's not like i love her back or anything!!" in message.content.lower() and message.author.id == conf.natsuki_id:  
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No shocker there, you selfish bitch!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh... I see...")
                    

        if "what the hell?? yuri, why would you say something so mean??" in message.content.lower() and message.author.id == conf.natsuki_id:  
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Because it's the fucking truth, you little bitch!!")
            

        if "aww thank you, yuri!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Y-You're welcome, Sayori.")


        if "well, of course she does! yuri loves everybody!" in message.content.lower() and message.author.id == conf.sayori_id:   
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No, I don't. In fact, I hate most people.")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("S-Sayori! You didn't have to say it like that...")
                

        if "yuri, it's me! sayori! your friend and vice president of the literature club!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("What the fuck?? ***I'M*** the Vice President, you stupid bitch! And I'm no friend of yours!!")

        if "i-it's me, sayori! and i-i just wanted to hug you!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry, but I don't know you. Please get your messy, stupid self away from me.")
            

        if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower() and message.author.id == conf.monika_id:   
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Except that I don't love you, sooo...")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuu... :flushed:")    

        if "y_act1" in message.content.lower() and (message.author.id == conf.monika_id or message.author.id == conf.mc_id):
            if message.guild.id in conf.act2:
                conf.act2.remove(message.guild.id) 
                await message.channel.send("O-Oh... Wh-What just happened? I feel funny...")
            else:
                await message.channel.send("Oh snap! You encountered a bug! Please report this to the developers if you're seeing this message!")
                pass

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message.guild.id in conf.act2:
                await message.channel.send(f"That's right <@{conf.mc_id}>, let me feel your pulsating cock on my pussy.")
            else:
                await message.channel.send("Augh!")

        if "fuck no, get away from me, yuri." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Then I'll stab you and crawl in your skin.")

        if "i-i love you, yuri." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message.guild.id in conf.act2:
                await message.channel.send(f"I love you too, you sexy <@{conf.mc_id}>! Now fuck me!!! :smirk:")
            else:
                await message.channel.send("*tackle hugs MC*")

        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------


def setup(bot):
    bot.add_cog(Event(bot))
