import discord, random, asyncio, chalk
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self):
        print("\n")
        print(chalk.green(f"Connected to Discord as: {self.b.user}"))
        if conf.sharding is False:
            print(chalk.red(f"Sharding: Disabled"))
        elif conf.sharding is True:
            print(chalk.green("Sharding: Enabled"))
            print(chalk.yellow(f"Using SHARD's {self.b.shard_ids}"))

        print(chalk.cyan(f"Config name: '{conf.name}'"))
        print(chalk.cyan(f"Defualt Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'"))
        print(chalk.cyan("Are you braindead: Most Likely"))
        print(chalk.cyan("Do you eat chicken nuggets: Yes.Yes.Yes.Yes.Yes.Yes.Yes.Yes."))
        aaa = True
        for guild in self.b.guilds:
            conf.act1.insert(0, guild.id)
        while aaa:
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        for guild in guild:
            conf.act1.insert(0, guild.id)

    @client.Cog.listener()
    async def on_message(self,message):        
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

        if message.content.lower() in cut_words:
            if message.guild.id in conf.act1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(cut_list)) 

            elif message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(cut_list_act_2)) 
            
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuuu... Sorry about this but i have seemed to have been restarted, re-run `y_act1` to continue using me")   


        if message.content.lower() in knife_words:
            if message.guild.id in conf.act1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(knife_list)) 

            elif message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(knife_list_act2)) 

            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuuu... Sorry about this but i have seemed to have been restarted, re-run `y_act1` to continue using me")   


        if message.content.lower() in pen_words:
            if message.guild.id in conf.act1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(pen_list)) 

            elif message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(pen_list_act2)) 



            # -------------------------------------------------------Tagging-------------------------------------------------------
        elif message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):

            #-------------------- Act 1 --------------------
            if message.guild.id in conf.act1:
                if len(message.content.lower().split(" ")) == 1:
                    tag_react_list = ["Y-Yes...?", "Did you want to talk to me...?", "Hm?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(tag_react_list))

                else:
                    message1 = message.content.lower().split(" ")[1]

                    if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                        hello_list = ["H-Hello there.", "...h-hi...", "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(hello_list))

                    elif "test" in message.content.lower():
                        await message.channel.send("I-I believe I'm working properly... Oh, I hope I am...")

                    elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                        love_list = ["O-Oh! W-W-Well, uhh... :flushed:", "I-I love you, too... :relaxed:", "R-Really? Why? I-I don't have anything worth loving...", "Uuu, why is my heart beating so fast right now??"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_list))

                    elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                        goodnight_list = ["G-Goodnight, then.", "Until next time.", "I hope you have wonderful dreams!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodnight_list))

                    elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                        goodmorning_list = ["It is a good morning, indeed.", "I hope you slept wonderfully!", "Good morning!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodmorning_list))

                    elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                        goodafternoon_list = ["Good afternoon.", "A truly beautiful afternoon, it is.", "Ah, it's times like this where I just want to sit outsite and read a good book."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodafternoon_list))

                    elif "you are" in message.content.lower() or "you're" in message.content.lower():
                        if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower():   
                            compliment_list = ["Y-You really think so...?", "Uuu... :flushed:", "T-Thank you. I needed to hear that...", ":blush:"]
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(compliment_list))
                            

                    elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                        apology_list = ["I don't think I fully understand why you're apologizing, but I accept it, anyway.", "It's alright; I forgive you.", "N-No, I'm the one who should be sorry; I mess up everything...", "Consider your apology accepted, then!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(apology_list))

                    elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                        if message1 == "monika" or message1 == "Yuri" or message1 == "Sayori" or message1 == "<@425696108455657472>" or message1 == "<@436350586670153730>":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("W-Well, I suppose that's true; she's much better than I am...")
                        elif message1 == "is" or message1 == "<@433834936450023424>" or message1 == "you" or message1 == "you're":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("Oh! Uh... Well, I'm glad you think that!")
                            return
                        else:
                            pass
                
                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("I-I'm sorry, but I don't understand what you mean...")


            #-------------------- Act 2 --------------------
            elif message.guild.id in conf.act2:
                if len(message.content.lower().split(" ")) == 1:
                    tag_react_list = ["Yes, my love?", "Oh, did someone call for me?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(tag_react_list))

                else:
                    message1 = message.content.lower().split(" ")[1]

                    if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                        hello_list = ["Hello there.", "Hello, my beloved! Nice to see you!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(hello_list))

                    elif "test" in message.content.lower():
                        await message.channel.send("I'm working fine, I promise you! Can we just read already??")

                    elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                        love_list = ["I love you, too! I love you so much that I touch myself to you every night!", "I'm glad, because if you didn't, I'd be very, *very* upset...", ":smirk:", "...Ahahaha. Ahahahahahaha! Ahahahahahahahaha! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_list))

                    elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                        goodnight_list = ["Haha. No. You're not allowed to go.", "Goodnight! I'll be sure to watch over you very closely while you're resting...", "I hope you don't mind if I look at your chest move up and down while the beautiful, soft breathing noises come from your mouth. Ahaha..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodnight_list))

                    elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                        goodmorning_list = ["Good morning, my love!", "Oh, good! You're finally awake!", "Did you know you snore very loudly? Ahaha...", "Good morning! I can't wait to spend the day together! Just you and me, nobody else..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodmorning_list))

                    elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                        goodafternoon_list = ["Good afternoon! But who cares what time it is; we'll be together forever, right??", "A perfect afternoon for just staring at each other, telling what kind of dirty things we could do together..."]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(goodafternoon_list))

                    elif "you are" in message.content.lower() or "you're" in message.content.lower():
                        if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower():   
                            compliment_list = ["Ohoho, stop it, you! I'm nothing compared to you!", "But you're 10 times as amazing!", "no u", "Oh? Am I attractive enough for you to pleasure youself to the thought of me? Because I do it to the thought of you all the time!", "Oh, I love it when you tell me that!"]
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send(random.choice(compliment_list))
                            

                    elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                        apology_list = ["Ahaha. There's no need to be sorry. I honestly found it kinda hot...", "Well, if it'll make you feel better, I accept your apology.", "Uhuhu. You look so cute when you apologize like that!"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(apology_list))

                    elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                        if message1 == "monika" or message1 == "Yuri" or message1 == "Sayori" or message1 == "<@425696108455657472>" or message1 == "<@436350586670153730>":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("No, she's fucking not.")
                        elif message1 == "is" or message1 == "<@433834936450023424>" or message1 == "you" or message1 == "you're":
                            async with message.channel.typing():
                                await asyncio.sleep(conf.type_speed)  
                            await message.channel.send("AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
                            return
                        else:
                            pass
                
                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("I love you, but I have no clue what you just said.")
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuuu... Sorry about this but i have seemed to have been restarted, re-run `y_act1` to continue using me")   

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
                        

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: #Monika
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

        if "y_act1" in message.content.lower() and message.author.id == conf.monika_id:
            if message.guild.id in conf.act2:
                conf.act2.remove(message.guild.id) 
                conf.act1.insert(0, message.guild.id)
                await message.channel.send("O-Oh... Wh-What just happened? I feel funny...")
            else:
                conf.act1.insert(0, message.guild.id) 
                await message.channel.send("O-Oh... Wh-What just happened? I feel funny...")

            

        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------


def setup(bot):
    bot.add_cog(Event(bot))
