import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import emoji
import pickle

client = commands.AutoShardedBot(command_prefix="y_")

e = discord.Embed()

cut_words = ["CUT", "CUTTING", "CUTS", "STAB", "STABBING", "STABS"]
knife_words = ["KNIFE", "KNIVES"]
pen_words = ["PEN", "PENS"]

answers = ["Y-yes.", "No...", "I'm not really sure.", "I don't believe so...", "I think that's a question best suited for Sayori.", "Perhaps Monika could be of better help?", "I-I don't know. I'm sorry...", "Natsuki might know.", "I believe so!"]
laughs = ["Oh! Hehehe!", "P-Please! Stop it! Ehehe!", "Hey, that tickles! Hahaha!", "HAHAHAHAHAHA! *snort*", "H-Hey! That's my ticklish spot!! :laughing:"]
headpat_reactions = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]
quotes = ["Here's a suggestion. Have you considered killing yourself? It would be beneficial to your mental health.", "After all, doesn't a hot cup of tea help you enjoy a good book?", "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?", "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment.", "Monika, please mind your own business for once. Or do you want to tell me there's something wrong with helping involve MC in club activities?", "Yes! I have terrible reading posture! So that's why we should sit on the floor.", "The thing is, I'm kind of into knives... They're just...so pretty...", "Just...for a little longer. It feels really nice...", "Sorry that my lifestyle is too much for someone of your mental age to comprehend!", "D-Did you just accuse me of cutting myself?? What the fuck is wrong with your head?!", "I love you so much that I even touch myself with the pen I stole from you.", "I just want to pull your skin open and crawl inside of you.", "Stagnating air is common foreshadowing that something terrible is about to happen..."]
name_reactions = ["Y-Yes...?", "Did you want to talk to me...?", "Hm?"]
love_reactions = ["O-Oh! W-W-Well, uhh... :flushed:", "I-I love you, too... :relaxed:", "R-Really? Why? I-I don't have anything worth loving...", "Uuu, why is my heart beating so fast right now??"]
goodnight_reactions = ["G-Goodnight, then.", "Until next time.", "I hope you have wonderful dreams!"]
goodmorning_reactions = ["It is a good morning, indeed.", "I hope you slept wonderfully!", "Good morning!"]
goodafternoon_reactions = ["Good afternoon.", "A truly beautiful afternoon, it is.", "Ah, it's times like this where I just want to sit outsite and read a good book."]
compliment_reactions = ["Y-You really think so...?", "Uuu... :flushed:", "T-Thank you. I needed to hear that...", ":blush:"]
mentioned_love_reactions = ["O-Oh, %s does...? W-Well, that's nice to hear.", "Uuu... I-I'm flattered, %s...", "R-Really? %s loves me...?", "W-Well... I-I think I love %s, too...!"]
apology_reactions = ["I don't think I fully understand why you're apologizing, but I accept it, anyway.", "It's alright; I forgive you.", "N-No, I'm the one who should be sorry; I mess up everything...", "Consider your apology accepted, then!"]
hellos = ["H-Hello there.", "...h-hi...", "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."]
cut_reactions = ["Uuu...!", "D-Did you have to say that word...?", "I-I'm sorry, I-I really don't like that word...", ":confounded:"]
knife_reactions = ["Y-You know, I'm a fan of knives...", "Do you like knives, as well?"]
pen_reactions = ["I-I get the feeling you're insulting me by mentioning pens...", "Uuu...! Why did Monika have to make me do...things...? Now I can't think of pens the same way again...!! :cold_sweat:", "I-I only use pens for writing, I swear!!"]

act2_cut_reactions = ["Oooo, yes. Say that again, please.", "Hahaha! I love your twisted sense of humor! It makes me so wet...", "Oh, I love it when you say that word... it makes me want to cut you and lick all the blood off."]
act2_knife_reactions = ["Ahahaha! Did someone mention knives...?!", "Oh, I love knives! The way the sharp blade slides along skin is just beautiful!", "Oh, just hearing that word makes me feel so... Ahaha..."]
act2_pen_reactions = ["I still have the pen I stole from MC... I even still use it from time to time...", "Hahaha. Are you expecting me to do something naughty with a pen? Because I just might if you ask nicely...", "Oh... Oh...! OH!!! YES, YES, YESYESYES!!!"]
act2_answers = ["Yes.", "I don't know, and I don't care. I just want to look at you...", "No.", "Possibly, but who knows?", "Meet me in the closet and we'll find out... :kissing_closed_eyes:", "Ahaha! You're so silly to ask such a question!", "I'm not sure... I'll think about it while I'm touching myself to you tonight."]
act2_laughs = ["Ahahaha! Yes, just like that!", "HEHEHEHEHEHEHE!!!", "Hahahahahaha!!!"]
act2_headpat_reactions = ["Oh, only my head is being pat? Shame.", "Huhuhu. I love it when you do cute things like that to me!", "Mmm... You know what would be better? If you moved that hand somewhere else...", "Oh, am I your dog or something? That's okay. I'll be anything you want me to be, my love."]
act2_name_reactions = ["Yes, my love?", "Oh, did someone call for me?"]
act2_hellos = ["Hello there.", "Hello, my beloved! Nice to see you!"]
act2_love_reactions = ["I love you, too! I love you so much that I touch myself to you every night!", "I'm glad, because if you didn't, I'd be very, *very* upset...", ":smirk:", "...Ahahaha. Ahahahahahaha! Ahahahahahahahaha! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"]
act2_goodnight_reactions = ["Haha. No. You're not allowed to go.", "Goodnight! I'll be sure to watch over you very closely while you're resting...", "I hope you don't mind if I look at your chest move up and down while the beautiful, soft breathing noises come from your mouth. Ahaha..."]
act2_goodmorning_reactions = ["Good morning, my love!", "Oh, good! You're finally awake!", "Did you know you snore very loudly? Ahaha...", "Good morning! I can't wait to spend the day together! Just you and me, nobody else..."]
act2_goodafternoon_reactions = ["Good afternoon! But who cares what time it is; we'll be together forever, right??", "A perfect afternoon for just staring at each other, telling what kind of dirty things we could do together..."]
act2_compliment_reactions = ["Ohoho, stop it, you! I'm nothing compared to you!", "But you're 10 times as amazing!", "no u", "Oh? Am I attractive enough for you to pleasure youself to the thought of me? Because I do it to the thought of you all the time!", "Oh, I love it when you tell me that!"]
act2_mentioned_love_reactions = ["Ohoho, well I think it's safe to say that %s doesn't love me as much as you do.", "%s does, do they? Well, I beg to differ.", "I'm sorry, %s, but I already have a lover, and they belong to me and me alone.", "Well, I suppose I could touch myself to %s, as well..."]
act2_apology_reactions = ["Ahaha. There's no need to be sorry. I honestly found it kinda hot...", "Well, if it'll make you feel better, I accept your apology.", "Uhuhu. You look so cute when you apologize like that!"]

y_server_ids = []
y_toggle_true = []
y_toggle_false = []
y_act_servers = []
y_act1 = []
y_act2 = []

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Type 'y_help' for help!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Doki Doki Literature Club"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="with knives!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Everlasting Summer"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Yandere Simulator"))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    client.emojis()
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("I-I'm ready...")

@client.event
async def on_message(message):
    global y_server_ids
    global y_toggle_true
    global y_toggle_false
    global y_act_servers
    global y_act1
    global y_act2
    global ServerID
    channel = message.channel
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in cut_words:
            ServerID = message.guild.id
            if ServerID in y_toggle_false:
                pass
            elif message.author.id == 436350586670153730 or message.author.id == 433834936450023424 or message.author.id == 425696108455657472:
                pass
            elif ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(act2_cut_reactions))
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(cut_reactions))
                return
        elif word.upper() in knife_words:
            ServerID = message.guild.id
            if ServerID in y_toggle_false:
                pass
            elif message.author.id == 436350586670153730 or message.author.id == 433834936450023424 or message.author.id == 425696108455657472:
                pass
            elif ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(act2_knife_reactions))
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(knife_reactions))
                return
        elif word.upper() in pen_words:
            ServerID = message.guild.id
            if ServerID in y_toggle_false:
                pass
            elif message.author.id == 436350586670153730 or message.author.id == 433834936450023424 or message.author.id == 425696108455657472:
                pass
            elif ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(act2_pen_reactions))
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(pen_reactions))
                return

    if ('@everyone' or '@here') in message.content.lower() and message.content.upper().startswith("Y_"):
        ServerID = message.guild.id
        await message.delete()
        if ServerID in y_act2:
            await channel.send("Oh, but why would I want everyone to listen when we can just stay together with no disturbances?")
            return
        else:
            await channel.send("I-I'm sorry, but I don't want everyone to hear me...")
            return

    if message.content.upper().startswith('Y_HUG'):
        ServerID = message.guild.id
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif ServerID in y_act2:
            userID = message.author.id
            act2_normal_hugs = ["*hugs <@%s>* Ahaha... I could hug you forever...!", "Oh, you have no idea how long I've been waiting for you to say that!! *hugs <@%s>*", "*hugs <@%s>* Mmm... You smell so wonderful! I wish I could smell this smell forever!", "Uhuhu... You can even grab my ass while we hug if you wanted. I don't mind ;) *hugs <@%s>*", "*hugs <@%s>* Oh, you're pressing hard against my chest. I must say, I really, really love it!"]
            if len(message.content.split(" ")) == 1:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(act2_normal_hugs) % (userID))
            else:
                userID = message.author.id
                act2_mentioned_hugs = ["No. I refuse to hug anyone other than you."]
                act2_hugself_reactions = ["But I don't ***want*** to hug myself! I want to hug ***YOU!!!***"]
                member = message.content.split(" ")[1]
                if member == "Yuri" or member == "yourself" or member == '<@436350586670153730>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_hugself_reactions))
                elif member == "<@{}>".format(userID):
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_normal_hugs) % (userID))
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_mentioned_hugs))
        else:
            userID = message.author.id
            normal_hugs = ["Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs <@%s>*", "Just let me know if this is too much for you... *hugs <@%s>*", "*hugs <@%s>* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
            if len(message.content.split(" ")) == 1:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(normal_hugs) % (userID))
            else:
                mentioned_hugs = ["Y-you want me to hug them? Well, o-okay, I guess I can do that for you... *hugs %s*", "Just let me know if this is too much for you... *hugs %s*", "*hugs %s* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                hugself_reactions = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
                member = message.content.split(" ")[1]
                if member == "Yuri" or member == "yourself" or member == '<@436350586670153730>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(hugself_reactions))
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(mentioned_hugs) % (member))

    if message.content.upper().startswith('Y_ASK'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(act2_answers))
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(answers))

    if message.content.upper().startswith('Y_TICKLE'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(act2_laughs))
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(laughs))

    if message.content.upper().startswith('Y_HEADPAT'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(act2_headpat_reactions))
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(headpat_reactions))

    if message.content.upper().startswith('Y_QUOTE'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(quotes))

    if message.content.upper().startswith('Y_INVITE'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            embed = discord.Embed(title="My invite link!", description="Ahahaha! I suppose I could visit other servers, but you're all I need!", color=0x8524c8)
            embed.add_field(name="Still, here you are!", value="https://discordbots.org/bot/436350586670153730", inline=True)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="My invite link!", description="Uuu, I don't know about this. W-What if they don't like me?", color=0x8524c8)
            embed.add_field(name="O-Oh, well... Here goes nothing...", value="https://discordbots.org/bot/436350586670153730", inline=True)
            await channel.send(embed=embed)

    if message.content.upper().startswith('Y_LOOP'):
        client.loop.create_task(status_task())
        return

# Feed Yuri ####################################################################

    if message.content.upper().startswith('Y_FEED'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            if len(message.content.split(" ")) == 1:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I'll eat anything you like, Darling. Anything.")
            else:
                member = message.content.split(" ")[1]
                # Alcohol
                if member == u"\U0001F37A" or member == u"\U0001F37B" or member == u"\U0001F378" or member == u"\U0001F379" or member == u"\U0001F37E" or member == u"\U0001F376" or member == u"\U0001F942" or member == u"\U0001F943" or member == u"\U0001F377":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I'm too young for this, but I'll drink it because you want me to! *chugs*")
                # Baby Bottle
                elif member == u"\U0001F37C":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, are you into that kind of thing? Well, I'll happily play along for you. Wah! Waah!")
                # Egg
                elif member == u"\U0001F95A":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Uhuhuhu! Raw eggs? Now you're just being silly, but I'll still accept!")
                # Silverware
                elif member == u"\U0001F374" or member == u"\U0001F37D" or member == u"\U0001F944":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Well, I'll admit that it wasn't as disgusting as I had originally assumed!")
                # Birthday Cake
                elif member == u"\U0001F382":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("It's not my birthday, but I'll still eat this cake!")
                # Eggplant
                elif member == u"\U0001F346":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Mmmm.... I wish this was your long, hard cock... :smirk: I can shove it all the way down my throat, if you'd like...")
                # Peach
                elif member == 	u"\U0001F351":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("It's so sweet and juicy... I just wanna lick all the juices up!")
                # Pens
                elif member == u"\U0001F58A" or member == u"\U0001F58B":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, I do believe this is the one with my juices on it. *licks* Mmm... Tasty...")
                # Knife
                elif member == u"\U0001F52A":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Mmmm.... I just wanna rub the blade across my tongue and taste the blood... Maybe I could let you taste it, as well...")
                # Not Food
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("*munch munch munch* Does that please you, my beloved?")
        else:
            if len(message.content.split(" ")) == 1:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
            else:
                member = message.content.split(" ")[1]
                # Cookie
                if member == u"\U0001F36A":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, the chocolate chips just melt in my mouth!")
                # Pizza
                elif member == u"\U0001F355":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("A slice of pizza never hurt, right...?")
                # Burger
                elif member == u"\U0001F354":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Fast food? I-I suppose that'll do.")
                # Cold Foods
                elif member == u"\U0001F367" or member == u"\U0001F366" or member == u"\U0001F368":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
                # Japanese Foods
                elif member == u"\U0001F363" or member == u"\U0001F371" or member == u"\U0001F35B" or member == u"\U0001F359" or member == u"\U0001F35A" or member == u"\U0001F358" or member == u"\U0001F35C" or member == u"\U0001F362" or member == u"\U0001F361" or member == u"\U0001F365":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...")
                # Alcohol
                elif member == u"\U0001F37A" or member == u"\U0001F37B" or member == u"\U0001F378" or member == u"\U0001F379" or member == u"\U0001F37E" or member == u"\U0001F376" or member == u"\U0001F942" or member == u"\U0001F943":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("T-Thank you, but I'll have to kindly decline.")
                # Wine
                elif member == u"\U0001F377":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Uuu... I already got in trouble once for trying to bring wine into the clubroom, and I don't want to get Monika mad.")
                # Coffee
                elif member == u"\u2615":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I-I'm more of a tea drinker. I'm sorry...")
                # Tea
                elif member == u"\U0001F375":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ah, thank you so much. All I need now is a good book.")
                # Bread
                elif member == u"\U0001F35E" or member == u"\U0001F956":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Hm... I suppose I need more ingredients than this, don't you think?")
                # Hot Pepper
                elif member == u"\U0001F336":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("O-Oh! Oh my goodness! That has quite a kick!!")
                # Cooking
                elif member == u"\U0001F373":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, I didn't know you knew how to cook eggs!")
                # Mexican Food
                elif member == u"\U0001F32E" or member == u"\U0001F32F":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
                # Sweets
                elif member == u"\U0001F370" or member == u"\U0001F36E" or member == u"\U0001F36C" or member == u"\U0001F369" or member == u"\U0001F36D":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I suppose a sweet wouldn't be such a bad idea...")
                # Chocolate
                elif member == 	u"\U0001F36B":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh! This brings up some... memories... with MC...")
                # Popcorn
                elif member == u"\U0001F37F":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("*crunch crunch crunch*")
                # Baby Bottle
                elif member == u"\U0001F37C":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
                # Egg
                elif member == u"\U0001F95A":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, is it hard-boiled? Oh... no, it's not...")
                # Silverware
                elif member == u"\U0001F374" or member == u"\U0001F37D" or member == u"\U0001F944":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ah, I'm generally used to chopsticks, but silverware will suffice.")
                # Milk
                elif member == u"\U0001F95B":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Th-Thank you. I love a nice glass of milk.")
                # Birthday Cake
                elif member == u"\U0001F382":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
                # Misc.
                elif member == u"\U0001F34E" or member == u"\U0001F34F" or member == u"\U0001F350" or member == u"\U0001F34A" or member == u"\U0001F34B" or member == u"\U0001F34C" or member == u"\U0001F349" or member == u"\U0001F347" or member == u"\U0001F353" or member == u"\U0001F348" or member == u"\U0001F352" or member == u"\U0001F351" or member == u"\U0001F34D" or member == u"\U0001F345" or member == u"\U0001F346" or member == u"\U0001F33D" or member == u"\U0001F360" or member == u"\U0001F36F" or member == u"\U0001F357" or member == u"\U0001F356" or member == u"\U0001F364" or member == u"\U0001F35F" or member == u"\U0001F32D" or member == u"\U0001F35D" or member == u"\U0001F950" or member == u"\U0001F951" or member == u"\U0001F952" or member == u"\U0001F953" or member == u"\U0001F954" or member == u"\U0001F955" or member == u"\U0001F957" or member == u"\U0001F958" or member == u"\U0001F959" or member == u"\U0001F95C" or member == u"\U0001F95D" or member == u"\U0001F95E" or member == u"\U0001F9C0":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, you didn't really have to, but thank you so much. *munch munch*")
                # Not Food
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Uuuu!! Th-that's not food!")

################################################################################

# @Yuri Mentions ###############################################################

    if message.content.upper().startswith('<@436350586670153730>'):
        userID = message.author.id
        ServerID = message.guild.id
        if len(message.content.split(" ")) == 1:
            if message.author.id == 433834936450023424 or message.author.id == 425696108455657472:
                pass
            elif ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(act2_name_reactions))
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(name_reactions))
                return
        else:
            member = message.content.split(" ")[1]
            ServerID = message.guild.id
            if 'hi' in message.content.lower() or 'hello' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_hellos))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(hellos))
                    return
            elif 'test' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I'm working fine, I promise you! Can we just read already??")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I-I believe I'm working properly... Oh, I hope I am...")
                    return
            elif 'i love you' in message.content.lower() or 'ily' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_love_reactions))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(love_reactions))
                    return
            elif 'goodnight' in message.content.lower() or 'good night' in message.content.lower():
                if message.author.id == 425696108455657472 or message.author.id == 425696108455657472:
                    pass
                elif ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_goodnight_reactions))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodnight_reactions))
                    return
            elif 'good morning' in message.content.lower():
                if message.author.id == 425696108455657472 or message.author.id == 425696108455657472:
                    pass
                elif ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_goodmorning_reactions))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodmorning_reactions))
                    return
            elif 'good afternoon' in message.content.lower():
                if message.author.id == 425696108455657472 or message.author.id == 425696108455657472:
                    pass
                elif ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_goodafternoon_reactions))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodafternoon_reactions))
                    return
            elif "you are" in message.content.lower() or "you're" in message.content.lower():
                if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower():
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send(random.choice(act2_compliment_reactions))
                        return
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send(random.choice(compliment_reactions))
                        return
                else:
                    pass
            elif 'loves you' in message.content.lower():
                if member == '<@425696108455657472>': #Sayori
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Who the hell is Sayori? I don't know any Sayoris...")
                        return
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Haha. Well, she is a loving soul.")
                        return
                elif member == '<@433834936450023424>': #Natsuki
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Pfft. As if. That immature brat doesn't love anyone but herself.")
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Sh-She does?")
                elif member == '<@436351740787294208>': #Monika
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("I'll believe that when that bitch says it to my face!")
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Ahaha... I-I'm glad that I have a friend like Monika who loves me... :blush:")
                else:
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send(random.choice(act2_mentioned_love_reactions) % (member))
                        return
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send(random.choice(mentioned_love_reactions) % (member))
                        return
            elif "sorry" in message.content.lower() or "apologize" in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(act2_apology_reactions))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(apology_reactions))
                    return
            elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                if member == "Monika" or member == "Natsuki" or member == "Sayori" or member == "<@425696108455657472>" or member == "<@433834936450023424>":
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("No, she's fucking not.")
                        return
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("W-Well, I suppose that's true; she's much better than I am...")
                        return
                elif member == "is" or member == "<@436350586670153730>" or member == "you" or member == "you\'re":
                    if ServerID in y_act2:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
                        return
                    else:
                        await asyncio.sleep(1)
                        await channel.trigger_typing()
                        await asyncio.sleep(1)
                        await channel.send("Oh! Uh... Well, I'm glad you think that!")
                        return
                else:
                    pass
            else:
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I love you, but I have no clue what you just said.")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I-I'm sorry, but I don't understand what you mean...")
                    return

################################################################################

# Other Bot Interactions #######################################################

    if '<@436350586670153730>' in message.content.lower():
        ServerID = message.guild.id
        if message.author.id == 433834936450023424: #Natsuki
            if 'hugs' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Get your fucking hands off of me!!")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh! Well, that was certainly unexpected!")
                    return
        elif message.author.id == 425696108455657472: #Sayori
            if 'hugs' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I'm sorry, who are you? And why are you hugging me?")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("H-Hey! Don't hug so hard, Sayori!")
                    return
        elif message.author.id == 436351740787294208: #Monika
            if 'hugs' in message.content.lower():
                if ServerID in y_act2:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Get your dirty, selfish hands off of me before I kill you and take your spot as President!!")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("O-Oh! Well, uh, thank you, Monika.")
                    return

    if message.author.id == 433834936450023424: #Natsuki
        ServerID = message.guild.id
        if "geez, yuri! don't make it all awkward!" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("I'm sorry...")
            return
        elif "w-well it's not like i love her back or anything!!" in message.content.lower():
            if ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("No shocker there, you selfish bitch!")
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Oh... I see...")
                return
        elif "what the hell?? yuri, why would you say something so mean??" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("Because it's the fucking truth, you little bitch!!")
            return

    elif message.author.id == 425696108455657472: #Sayori
        ServerID = message.guild.id
        if "aww, thank you, yuri!" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Y-You're welcome, Sayori.")
            return
        elif "well, of course she does! yuri loves everybody!" in message.content.lower():
            if ServerID in y_act2:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("No, I don't. In fact, I hate most people.")
                return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("S-Sayori! You didn't have to say it like that...")
                return
        elif "yuri, it's me! sayori! your friend and vice president of the literature club!" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(3)
            await channel.send("What the fuck?? ***I'M*** the Vice President, you stupid bitch! And I'm no friend of yours!!")
            return
        elif "i-it's me, sayori! and i-i just wanted to hug you!" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("Sorry, but I don't know you. Please get your messy, stupid self away from me.")
            return

    elif message.author.id == 436351740787294208: #Monika
        ServerID == message.guild.id
        if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower():
            if ServerID in y_act2:
                await asyncio.sleep(2)
                await channel.trigger_typing()
                await asyncio.sleep(2)
                await channel.send("Except that I don't love you, sooo...")
                return
            else:
                await asyncio.sleep(2)
                await channel.trigger_typing()
                await asyncio.sleep(2)
                await channel.send("Uuu... :flushed:")
                return
    else:
        pass

# Pickling Stuff ###############################################################

    if message.content.upper().startswith('PICKLE_SAVE'):
        if message.author.id == 270057011251642368:
            with open('y_servers.pkl', 'wb') as pickle_file:
                pickle.dump(y_server_ids, pickle_file)
            with open('y_true.pkl', 'wb') as pickle_file:
                pickle.dump(y_toggle_true, pickle_file)
            with open('y_false.pkl', 'wb') as pickle_file:
                pickle.dump(y_toggle_false, pickle_file)
            with open('y_act_servers.pkl', 'wb') as pickle_file:
                pickle.dump(y_act_servers, pickle_file)
            with open('y_act1.pkl', 'wb') as pickle_file:
                pickle.dump(y_act1, pickle_file)
            with open('y_act2.pkl', 'wb') as pickle_file:
                pickle.dump(y_act2, pickle_file)
            await channel.send("Pickling officially saved!")
        else:
            pass

    if message.content.upper().startswith('PICKLE_LOAD'):
        if message.author.id == 270057011251642368:
            with open('y_servers.pkl', 'rb') as pickle_file:
                server_update = pickle.load(pickle_file)
                y_server_ids = server_update
            with open('y_true.pkl', 'rb') as pickle_file:
                toggle_true_update = pickle.load(pickle_file)
                y_toggle_true = toggle_true_update
            with open('y_false.pkl', 'rb') as pickle_file:
                toggle_false_update = pickle.load(pickle_file)
                y_toggle_false = toggle_false_update
            with open('y_act_servers.pkl', 'rb') as pickle_file:
                act_server_update = pickle.load(pickle_file)
                y_act_servers = act_server_update
            with open('y_act1.pkl', 'rb') as pickle_file:
                act1_update = pickle.load(pickle_file)
                y_act1 = act1_update
            with open('y_act2.pkl', 'rb') as pickle_file:
                act2_update = pickle.load(pickle_file)
                y_act2 = act2_update
            await channel.send("Pickling officially loaded!")
        else:
            pass

    if message.content.upper().startswith('Y_TOGGLE'):
        if message.author.guild_permissions.administrator:
            ServerID = message.guild.id
            if ServerID in y_server_ids:
                pass
            else:
                y_server_ids.insert(0, ServerID)
                y_toggle_true.insert(0, ServerID)
            if ServerID in y_toggle_true:
                y_toggle_true.remove(ServerID)
                y_toggle_false.insert(0, ServerID)
                await channel.send("O-Okay, I won't react to chat triggers...")
            elif ServerID in y_toggle_false:
                y_toggle_false.remove(ServerID)
                y_toggle_true.insert(0, ServerID)
                await channel.send("O-Okay, I'll react to chat triggers...")
        else:
            await channel.send("I-I'm terribly sorry, but you don't seem to be able to use this command...")

    if message.content.upper().startswith('Y_ACT1'):
        ServerID = message.guild.id
        if message.author.guild_permissions.administrator:
            if ServerID in y_act_servers:
                pass
            else:
                y_act_servers.insert(0, ServerID)
                y_act1.insert(0, ServerID)
            if ServerID in y_act1:
                await channel.send("I'm already in my 'Act 1' mode. And I'd prefer if it stayed that way...")
            elif ServerID in y_act2:
                y_act2.remove(ServerID)
                y_act1.insert(0, ServerID)
                await channel.send("O-Oh... Wh-What just happened? I feel funny...")
        else:
            if ServerID in y_act2:
                await channel.send("Oh, I'm terribly sorry, but I'm afraid that only the ones who are administrators can use that command!")
            else:
                await channel.send("I-I'm terribly sorry, but you don't seem to be able to use this command...")

    if message.content.upper().startswith('Y_ACT2'):
        if message.author.guild_permissions.administrator:
            ServerID = message.guild.id
            if ServerID in y_act_servers:
                pass
            else:
                y_act_servers.insert(0, ServerID)
                y_act1.insert(0, ServerID)
            if ServerID in y_act1:
                y_act1.remove(ServerID)
                y_act2.insert(0, ServerID)
                await channel.send("Ha. Haha. HAHAHAHAHHAHAHA!!!!")
            elif ServerID in y_act2:
                await channel.send("Oh, you little cutie! I'm already in Act 2 mode! Ahaha!!")
        else:
            if ServerID in y_act2:
                await channel.send("Oh, I'm terribly sorry, but I'm afraid that only the ones who are administrators can use that command!")
            else:
                await channel.send("I-I'm terribly sorry, but you don't seem to be able to use this command...")

################################################################################

################################################################################

    if message.content.upper().startswith('Y_HELP'):
        ServerID = message.guild.id
        if ServerID in y_act2:
            embed = discord.Embed(title="Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I just know that being with you will be the best thing to ever happen to both of us, ahaha! Here are all the things we can do together:", color=0x8524c8)
            embed.add_field(name="y_act1/y_act2", value="You can use this to toggle between my Act 1 personality and my Act 2 one. This can only be used by server administrators. Honestly, I love you either way, so I don't care which one I'm one!", inline=True)
            embed.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, and I'll try my hardest to answer it for you!", inline=True)
            embed.add_field(name="y_feed", value="You can use this to feed me any of emojis available. Any of them. *(Format like this: 'y_feed :emoji:')*", inline=True)
            embed.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
            embed.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you, I'll happily do it. It would be the best thing to ever happen in my life!", inline=True)
            embed.add_field(name="y_invite", value="You can use this to have me give you the invite link to let me join other servers. But why would you want that when it can be just us forever?", inline=True)
            embed.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club.", inline=True)
            embed.add_field(name="y_tickle", value="You can use this to tickle me, which is so hot and sexy...", inline=True)
            embed.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. If he doesn't add new things soon, I'm afraid he might not be breathing for too much longer... Feel free to visit Cole's Support Server to let him know that I'm counting on him to make me do anything possible to spend time with you.", inline=True)
            embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="H-Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I-I hope I don't become an inconvenience to you... A-Anyway, here are the things I can do:", color=0x8524c8)
            embed.add_field(name="y_act1/y_act2", value="Y-You can use this to toggle my Act 1 and Act 2 personalities, b-but this can only be done by a server administrator... Uu, could you please keep me on Act 1, though? I-I'm not proud of how I behave in Act 2 mode...", inline=True)
            embed.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, but please don't be disappointed if I don't know the answer or even give an incorrect one...", inline=True)
            embed.add_field(name="y_feed", value="You can use this to feed me any of the food emojis available. *(Format like this: 'y_feed :food_emoji:')*", inline=True)
            embed.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
            embed.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you or someone else on the server, then I suppose I can do that. Simply leave it blank if you want me to hug you, or @mention someone immediately after to have me hug them.", inline=True)
            embed.add_field(name="y_invite", value="Y-You can use this to have me post my invite link so I can visit other servers. A-Although, I don't see why anyone would want that. I'm so useless...", inline=True)
            embed.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club, although some of them, I'm not proud to admit that I said... Uu...", inline=True)
            embed.add_field(name="y_tickle", value="You can use this to tickle me, although I should warn you that I tend to have embarassing laughs...", inline=True)
            embed.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. I hope you enjoy my presence on your Discord server, and if you have any questions, comments, or suggestions, feel free to visit Cole's Support Server. Thank you.", inline=True)
            embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await channel.send(embed=embed)

client.run("REDACTED")
