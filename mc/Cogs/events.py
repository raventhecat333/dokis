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
            # TODO: Complete TODOs in this section.
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
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send("...")
                    return 

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():                
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send("Um... Good night, I guess.")
                    return

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():                
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(":zzz: Huh- morning already?")
                    return

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))
                    return

                elif "you are cute" in message.content.lower() or "you're cute" in message.content.lower() or "you are beautiful" in message.content.lower() or "you're beautiful" in message.content.lower():                   
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send("No I’m not.")
                    return

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower() or "i apologize" in message.content.lower():                  
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send("I-It’s ok.")
                    return 

                elif 'loves you' in message.content.lower():
                    member = message.content.split(" ")[1]
                    if 'nigger' in message.content.lower():
                        return

                    elif member == "loves":
                        await message.channel.send("Ehh?")
                        return

                    # TODO: Replace these responses.
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
                        await message.channel.send("Um… what?")
                        return
                    
                elif "i'm sick" in message.content.lower() or "puke" in message.content.lower() or "not feeling good" in message.content.lower() or "not feeling great" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send("I’m not one for that stuff, maybe ask Monika.")
                    return 

                elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                    if message1 == "Monika" or message1 == "Natsuki" or message1 == "Yuri" or message1 == "<@436350586670153730>" or message1 == "<@433834936450023424>":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("I’ll have to agree with you there.")
                        return 
                    # TODO: Also replace this response.
                    elif message1 == "is" or message1 == f"<@{conf.mc_id}>" or message1 == "you" or message1 == "you're":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("Who? Me? How?")
                        return

                elif "test" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Testing, testing! 1-2-1-2 testing!")

                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Eh?")

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
            await asyncio.sleep(1)
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("y_act1")

        if f"that's right <@{conf.mc_id}>, let me feel your pulsating cock on my pussy." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh hell no...")

        if f"ah! you scared me, <@{conf.mc_id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry, I'm a dumbass.")

        if "os.remove" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Not this shit again, Monika.")

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

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.author.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Augh!")

        if "yes?" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I love you, Sayori.")

        if "i-i do too! *hugs mc*" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs back*")

        if f"yes, <@{conf.mc_id}>?" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I need to tell you something.")

        if "hmm?" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I love you, Monika.")

        if "*tackle hugs mc*" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs back*")

        if f"i love you too, you sexy <@{self.b.user.id}>! now fuck me!!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh hell no!")

        if "what do you want, dummy?" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I love you, Natsuki...")

        if "well, i-i do too..." in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs Natsuki*")
    
        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        
def setup(bot):
    bot.add_cog(Event(bot))
