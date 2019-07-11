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

        print(chalk.cyan(f"Config name: '{conf.name}''"))
        print(chalk.cyan(f"Defualt Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'"))
        print(chalk.cyan(f"I'm currently in [{len(self.b.guilds)}] server(s)."))
        for guild in self.b.guilds:
            conf.w_tog_on.insert(0, guild.id)
        aaa = True
        while aaa:
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    
    @client.Cog.listener()
    async def on_message(self,message):
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        trigger_words = ["rope", "poetry"]

        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct =  message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if message.content.lower() in trigger_words:
                if message.author.bot:
                    pass

                else:
                    if message.guild.id in conf.w_tog_on:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        if word == trigger_words[0]:
                            await message.channel.send("NO!")
                        else:
                            await message.channel.send("Oh... you make poems too, cool.")
                        return
                    else:
                        pass
                        
            # -------------------------------------------------------Tagging-------------------------------------------------------
            # TODO: Change Sayori's responses with MC's.
        if message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):
            if len(message.content.lower().split(" ")) == 1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Yes?")
                return

            else:
                message1 = message.content.lower().split(" ")[1]

                if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                    hello_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(hello_list))
                    return

                elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                    love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(love_list))
                    return 

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodnight_list))
                    return

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                    goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodmorning_list))
                    return

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))
                    return

                elif "you are cute" in message.content.lower() or "you're cute" in message.content.lower() or "you are beautiful" in message.content.lower() or "you're beautiful" in message.content.lower():
                    cute_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(cute_list))
                    return

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower() or "i apologize" in message.content.lower():
                    apology_list = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(apology_list))
                    return 

                elif 'loves you' in message.content.lower():
                    member = message.content.split(" ")[1]
                    love_tag_list = [f"Aww! Well, you can tell {member} that I love them, too!", f"{member} does? Well, that's so sweet to hear!", f"And I love {member}, too! :heart:", f"Yay! I'm loved by {member}!"]
                    if 'nigger' in message.content.lower():
                        return

                    elif member == "loves":
                        await message.channel.send("Ehh?")
                        return

                    elif message.content.lower() == f'<@{conf.natsuki_id}>': #Natsuki
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Awww, she does??")
                        return
                        
                    elif message.content.lower() == f'<@{conf.yuri_id}>': #Yuri
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Well, of course she does! Yuri loves everybody!")
                        return
                    elif message.content.lower() == f'<@{conf.monika_id}>': #Monika
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Yay! I'm glad she does!")
                        return

                    elif message.content.lower() == 'everyone' or message.content.lower() == '@everyone' or message.content.lower() == '@here' or message.content.lower() == 'everybody':
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("R-really? EVERYONE? Oh, my!")
                        return

                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_tag_list))
                        return

                elif "syka blyat" in message.content.lower() or "pidor ebony" in message.content.lower():
                    russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(russian_list))
                    return 
                    
                elif "i'm sick" in message.content.lower() or "puke" in message.content.lower() or "not feeling good" in message.content.lower() or "not feeling great" in message.content.lower():
                    gwell_list = ["Don't worry! I'm sure you'll feel better soon!", "Aww... get plenty of rest, and eat a lot of healthy foods!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(gwell_list))
                    return 

                elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                    if message1 == "Monika" or message1 == "Natsuki" or message1 == "Yuri" or message1 == "<@436350586670153730>" or message1 == "<@433834936450023424>":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("Well, I respect your opinion!")
                        return 

                    elif message1 == "is" or message1 == "<@436350586670153730>" or message1 == "you" or message1 == "you're":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("S-Stop it! That's not true!")
                        return

                elif "test" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Testing, testing! 1-2-1-2 testing!")

                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(confused_list))

            # -------------------------------------------------------Tagging-------------------------------------------------------



        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        if f"aww, you're the best hugger, <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("No I'm not...")

        if f"aww you're such a sweetheart, <@{conf.mc_id}>" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("You will always be my closest friend, Sayori.")

        if "augh!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry...")

        if f"hey <@{conf.mc_id}>, get your sexy body over here and fuck me~" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Fuck no, get away from me, Yuri.")

        if "then i'll stab you and crawl in your skin." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Yeah, fuck no.")
            asyncio.sleep(1)
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("y_act1")

        if "that's right <@{conf.mc_id}>, let me feel your pulsating cock on my pussy." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh hell no...")

        if f"ah! you scared me, <@{conf.mc_id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry, I'm a dumbass.")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*muffled screaming*")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Finnnnnnne, Sayori.")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("No, it's fine...")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natuski_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.author.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Augh!")
    
        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------







        
def setup(bot):
    bot.add_cog(Event(bot))
