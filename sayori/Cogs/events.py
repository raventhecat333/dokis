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
        name_words = ["cinnamon bun", "best girl"]
        name_list = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]

        goodmorning_words = ["goodmorning", "goodmorning,", "goodmorning!", "good morning", "Good Morning", "Good morning"]
        goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]

        goodafternoon_words = ["goodafternoon", "goodafternoon,", "goodafternoon!", "good afternoon", "Good Afternoon", "Good afternoon"]
        goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]

        goodnight_words = ["goodnight", "gn", "goodnight,", "goodnight!", "good night", "Good Night", "Good night"]
        goodnight_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]

        breakfast_words = ["breakfast", "b2"]
        breakfast_list = ["I want breakfast"]

        hang_words = ["hang", "hanging", "hung", "hanged"]
        hang_list = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
        suicide_list = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]

        kill_words = ["kill"]

        meanie_words = ["meanie"]
        meanie_list = ["Do we have a meanie in the server? If so, please stop.", "Cease your bulli, you meanie!", "Boo! You meanie..."]

        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct =  message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if message.content.lower() in name_words:
                if message.author.bot:
                    pass

                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(name_list)) 
                        return
                    else:
                        pass

            if word.lower() in breakfast_words:
                if message.author.bot:
                    return
                    
                if message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed) 
                    await message.channel.send(random.choice(breakfast_list)) 
                    return
                else:
                    pass

            if word.lower() in goodmorning_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodmorning_list)) 
                        return
                    else:
                        pass

            if word.lower() in goodafternoon_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodafternoon_list)) 
                        return
                    else:
                        pass

            if word.lower() in goodnight_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodnight_list)) 
                        return
                    else:
                        pass

            if word.lower() in meanie_words:
                if message.author.bot:
                    pass
                elif message.content.startswith(f"<@{self.b.user.id}>") or message.content.startswith(f"<@!{self.b.user.id}>"):
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(meanie_list)) 
                        return
                    else:
                        pass


            if word.lower() in hang_words:
                if message.guild.id not in conf.w_tog_on:
                    pass

                if message.author.bot:
                    pass

                elif message.content.upper().startswith(f"<@{self.b.user.id}>"):
                    pass

                elif "myself" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(suicide_list))
                    return
                    
                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(hang_list))
                    return

            if word.lower() in kill_words:
                if (message.guild.id not in conf.w_tog_on) or (message.author.id is (conf.natsuki_id or conf.yuri_id)):
                    return

                elif message.content.upper().startswith(f"<@{self.b.user.id}>"):
                    pass

                elif "myself" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(suicide_list))
                    return

                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Can we change the topic to something more wholesome please?")
                    return
                        
            # -------------------------------------------------------Tagging-------------------------------------------------------
        if re.search(f"^<@!?{self.b.user.id}>", message.content): #re check if string *starts with* mentioning me (even if someone nicknames me or not)
            content = re.sub(f'^<@!?{self.b.user.id}>', "", message.content).strip()


            hi_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]   
            love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]
            night_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
            morning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
            afternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
            compliment_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]
            apology_list = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]
            sickness_list = ["Don't worry! I'm sure you'll feel better soon!", "Aww... get plenty of rest, and eat a lot of healthy foods!"]
            russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
            otherbestgirl = "Well, I respect your opinion!"
            bestgirl = "S-Stop it! That's not true!"
            natsukilove = "Awww, she does??"
            yurilove = "Well, of course she does! Yuri loves everybody!"
            monikalove = "Yay! I'm glad she does!"
            mclove = "Yay! My best friend loves me!!! :heart:"
            #Meanie list is located in the meanie trigger due to issues with variables and such, sorry!
            respempty = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
            resbad = ["Huh? I don't understand.", "I don't get it.", "???", "Maybe try something I actually understand?"]


			#-------------------- Responding --------------------
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
                await message.channel.send(otherbestgirl)

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(bestgirl)

            elif re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(monikalove)
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

            elif re.search("cyka.*blyat", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(russian_list))

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                love_tag_reactions = [f"Aww! Well, you can tell {regex} that I love them, too!", f"{regex} does? Well, that's so sweet to hear!", f"And I love {regex}, too! :heart:", f"Yay! I'm loved by {regex}!"]

                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(love_tag_reactions))
                return

            elif re.search("(monika.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Monika isn't a meanie! And no, I don't feel obligated to say that for fear of her deleting me again...")
                return

            elif re.search("(natsuki.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Hey, she may be spunky, but she's not a meanie!")
                return

            elif re.search("(yuri.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("What?? Yuri is the last person who would ever be a meanie!")
                return

            elif re.search("(sayori.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Eh?? No, I'm not!!")
                return

            elif re.search(r".+\s.*(are|is).*meanie", message.content, re.IGNORECASE):

                regex = re.search(r"(.+)\s(are|is).*meanie", content).group(1)
                meanie_list = [f"Hey! Stop being a meanie, {regex}!", f"We don't like meanies on this server, {regex}!", f"Are you being a meanie, {regex}? If so, please stop."]
                
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(meanie_list))

            elif "test" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Testing, testing! 1-2-1-2 testing!")
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(resbad))
            # -------------------------------------------------------Tagging-------------------------------------------------------



        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Hehehe! You give the best hugs, Natsuki!")

        if "s-shut up! no she doesn't!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh, yes I do!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aww, thank you, Yuri!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Ehehe! I love your hugs, Monika! You should give them more often!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Aww you're such a sweetheart, <@{conf.mc_id}>")

        if "s-shut up! no i don't!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Awww... :(")

        if "h-hey! Don't hug so hard, Sayori!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oops! I'm sorry!")

        if "haha. well, she is a loving soul." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("You bet your booty I am! :yum:")
                
        if "who the hell is sayori? i don't know any sayoris..." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!")
            
        if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(":disappointed_relieved: :cold_sweat: :confounded: :sob:")
                
        if "i'm sorry, who are you? and why are you hugging me?" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-It's me, Sayori! And I-I just wanted to hug you!")
                
        if "sorry, but i don't know you. please get your messy, stupid self away from me." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("O-Okay... I'm sorry... :pensive:")

        if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Hey, everyone deserves forgiveness! Even you, Monika!")

        if "finnnnnnne, sayori." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"YAY! *keeps hugging <@{conf.mc_id}>*")

        if "hey, sayori?" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Yes, <@{conf.mc_id}>?")

        if "i-i love you, sayori" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I do too! *hugs MC*")
    
        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------







        
def setup(bot):
    bot.add_cog(Event(bot))
