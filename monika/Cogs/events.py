import discord, random, asyncio, chalk, re
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

        print(chalk.cyan(f"Config name: '{conf.name}''"))
        print(chalk.cyan(f"Defualt Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'"))
        print(chalk.cyan("Are you braindead: Most Likely"))
        print(chalk.cyan(f"I'm currently in [{len(self.b.guilds)}] server(s)."))
        for guild in self.b.guilds:
            conf.w_tog_on.insert(0, guild.id)
        aaa = True
        while aaa:
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        e = discord.Embed(title="Hi! I'm Monika!",description="I DON'T KNOW WHAT KINDA DESC TO PUT IN HERE IM A DEVELOPER NOT A WRITER!!!!!!!!1111",color=conf.norm)
        await guild.owner.send(embed=e)
        print("Test")

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
        mct = message.content.lower().split(" ") # (MCT | Meesage Contents)
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

        if message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):
            if len(message.content.lower().split(" ")) == 1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Yes?")
                return

            else:
                message1 = message.content.lower().split(" ")[1]

                if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                    hello_list = ["Hello! Welcome to the Literature Club!~", "Why, hello there!", "Hello, my fellow real personality!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(hello_list))
                    return

                elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                    love_list = ["Ahaha!~ W-Well, I'm flattered, to say the least!", "And I love you, too!", "Well, in fairness, why wouldn't you? Ahaha!~"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(love_list))
                    return

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                    goodnight_list = ["Have a good night!", "Goodnight! I hope you get plenty of rest!", "Aww, you have to go? Well, okay! Goodnight!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodnight_list))
                    return

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                    goodmorning_list = ["Good morning! I hope your day is a very great one!", "A good morning, indeed!", "Good morning! Ready for a fun day in the Literature Club?"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodmorning_list))
                    return

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon! It's almost time for club activities!", "Afternoon!", "Good afternoon! I hope your day has been going well so far!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))
                    return

                elif "you are" in message.content.lower() or "you're" in message.content.lower():
                    if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower() or "hot" in message.content.lower() or "amazing" in message.content.lower():
                        compliment_list = ["Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~", ":blush:", "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"]
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(compliment_list))
                        return

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower():
                    apology_list = ["Well, I thank you for the apology. Let's try not to do that again, hm?", "Apology accepted!~", "Very well, then! I hope you've learned your lesson."]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(apology_list))
                    return

                elif "i'm sick'" in message.content.lower() or "puke" in message.content.lower() or "not feeling good" in message.content.lower() or "not feeling great" in message.content.lower():
                    gwell_list = ["Oh! I hope you feel better, after all, I have to take care of my club members!", "I hope you feel better! I'm sure all of the other club members would say the same!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(gwell_list))
                    return

                elif 'loves you' in message.content.lower():
                    member = message.content.split(" ")[1]
                    love_tag_list = [f"Aww! Well, you can tell {member} that I love them, too!", f"{member} does? Well, that's so sweet to hear!", f"And I love {member}, too! :heart:", f"Yay! I'm loved by {member}!"]
                    if 'nigger' in message.content.lower():
                        return

                    elif member == "loves":
                        await message.channel.send("Ehh?")
                        return

                    elif message.content.lower() == f'<@{conf.sayori_id}>': #Sayori
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Ahaha!~ Well, after everything that's happened between us, that's nice to hear!")
                        return

                    elif message.content.lower() == f'<@{conf.yuri_id}>': #Yuri
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly.")
                        return

                    elif message.content.lower() == f'<@{conf.natsuki_id}>': #Natsuki
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Oh, really? She, of all people, said that?")
                        return

                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_tag_list))
                        return



                elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                    if message1 == "Yuri" or message1 == "Sayori" or message1 == "<@425696108455657472>" or message1 == "<@436350586670153730>":
                        imbestgirl_list = ["I'm sorry, I didn't catch that. What did you say?", "Hm? Did you say something?", "Ahaha!~ You're funny!"]
                        await message.delete()
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(imbestgirl_list))
                        return

                    elif message1 == "is" or message1 == f"<@{conf.monika_id}>" or message1 == "you" or message1 == "you're":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!")
                        return
                    else:
                        pass
            



            # -------------------------------------------------------Tagging-------------------------------------------------------





            # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("Easy now, Sayori! I Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~")
            

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aw, no need to be shy, Yuri! I don't mind a hug every now and then!")


        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aww, how cute of you, Natsuki!")


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
            # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------












        
def setup(bot):
    bot.add_cog(Event(bot))
