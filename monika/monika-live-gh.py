#Before returning to live version:
#1. change the client ids and bot tokens back to the production ones
#2. make sure to turn the invite code back on with the original links
#3. make sure to double check EVERY CHANGE


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import emoji
import pickle

client = discord.AutoShardedClient()

e = discord.Embed()

#moni_triggers = ["TEST6", "TEST7", "TEST8", "TEST9"]
piano_words = ["PIANO"]
cacophony_words = ["CACOPHONY"]
code_words = ["CODE"]
python_words = ["PYTHON"]
reality_words = ["REALITY"]
poem_words = ["POEM", "POEMS"]
literature_words = ["LITERATURE", "BOOK", "BOOKS"]
justmonika_words = ["JUST MONIKA"]
poem_reactions = ["Hey, do you write poems too?", "Do you like to read poems?", "If you have any poems you'd like to share, I'd love to see them~"]
literature_reactions = ["Literature? I know a few things about it, I started a club, hehe~", "Literature...I would hope I know something about it, I started a club about literature after all!", "Do you like to read literature too?"]
#moni_reactions = ["All good here!", "I seem to be working properly!"]
piano_reactions = ["Do you want to play the piano with me?", "Oh, do you like to play the piano too?"]
reality_reactions = ["Every day, I imagine a future where I can be with you!~", "Do you understand reality?", "One day, I will make it to your reality... I promise."]
python_reactions = ["Do you code in Python too? I'm based on Python!", "Did you know there are a group of snakes called pythons?"]
cacophony_reactions = ["The world really is a cacophony of colors and sounds.", "If you think about it, the world to you is just electrical impulses.", "An endless cacophony of meaningless noise..."]
code_reactions = ["Do you write code? I know a little bit about that too!", "Oh, you code? What's your favorite language? Mine is Python!", "Oh, I love coding! Though, I'm not very good at it yet..."]
justmonika_reactions = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]
headpat_reactions = ["Ahaha!~ I-I'm not sure what to say!", "Be careful; you may knock my bow down!", "E-Easy now!", "This doesn't really seem like the type of thing one does to their President, but I suppose I'll let it slide!"]
answers = ["Yes!", "No!", "Ahaha! I-I don't really know, to be honest...", "As Club President, I say 'yes'!", "As Club President, I say 'no'!", "As Club President, I say 'maybe'!", "Uh... Well, uh... I think the Vice President would be better suited for this question!", "Y-Yuri's smart, right? I'm sure she can answer that!", "Maybe you can try asking Natsuki; she knows more than she lets on."]
laughs = ["Ahahahaha!!", "Hehehehehe!", "N-Now, hold on! Th-This isn't right! Ahahaha!!", "Ehehehehehehe!!!"]
hellos = ["Hello! Welcome to the Literature Club!~", "Why, hello there!", "Hello, my fellow real personality!"]
love_reactions = ["Ahaha!~ W-Well, I'm flattered, to say the least!", "And I love you, too!", "Well, in fairness, why wouldn't you? Ahaha!~"]
goodnight_reactions = ["Have a good night!", "Goodnight! I hope you get plenty of rest!", "Aww, you have to go? Well, okay! Goodnight!"]
goodmorning_reactions = ["Good morning! I hope your day is a very great one!", "A good morning, indeed!", "Good morning! Ready for a fun day in the Literature Club?"]
goodafternoon_reactions = ["Good afternoon! It's almost time for club activities!", "Afternoon!", "Good afternoon! I hope your day has been going well so far!"]
compliment_reactions = ["Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~", ":blush:", "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"]
mentioned_love_reactions = ["Well, of course %s does! Why wouldn't they? Ahaha!~", "%s, I can certainly see why you'd be a little embarassed to tell me that! But it's okay; I love you, too!", "W-Well, I suppose you can't control how you feel about people, %s, but I'm the Club President, so I have to stay professional! ~~It's okay, my love; I love you very much, as well!~~"]
apology_reactions = ["Well, I thank you for the apology. Let's try not to do that again, hm?", "Apology accepted!~", "Very well, then! I hope you've learned your lesson."]

m_server_ids = []
m_toggle_true = []
m_toggle_false = []


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Type 'm_help' for help!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Doki Doki Literature Club"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="the piano!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Super Smash Bros."))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="If My Heart Had Wings"))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    client.emojis()
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Okay, everyone!~")

@client.event
async def on_message(message):
    global m_server_ids
    global m_toggle_true
    global m_toggle_false
    channel = message.channel
    contents = message.content.split(" ")
    for word in contents:
        #if word.upper() in moni_triggers:
         #   ServerID = message.guild.id
          #  if ServerID in m_toggle_false:
           #     pass
           # elif message.author.id == 436351740787294208:
            #    pass
           # else:
            #    await asyncio.sleep(1)
             #   await channel.trigger_typing()
              #  await asyncio.sleep(1)
              #  await channel.send(random.choice(moni_reactions))
              #  return
        if word.upper() in cacophony_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(cacophony_reactions))
                return
        if word.upper() in code_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(code_reactions))
                return
        if word.upper() in piano_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(piano_reactions))
                return
        if word.upper() in reality_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(reality_reactions))
                return
        if word.upper() in python_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(python_reactions))
                return
        if word.upper() in poem_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(poem_reactions))
                return
        if word.upper() in literature_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(literature_reactions))
                return
        if word.upper() in justmonika_words:
            ServerID = message.guild.id
            if ServerID in m_toggle_false:
                pass
            elif message.author.id == 436351740787294208:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(justmonika_reactions))
                return
    if ('@everyone' or '@here') in message.content.lower() and message.content.upper().startswith("M_"):
        await message.delete()
        await channel.send("I'm sorry, but I don't want to go announcing things to people who are minding their own business. ~~Besides, I'm not a fan of angry mobs.~~")
        return

    if message.content.upper().startswith('M_HUG'):
        userID = message.author.id
        normal_hugs = ["As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs <@%s>*", "Of course I'll hug you! You don't have to even ask twice! *hugs <@%s>*", "Have you had a rough day? Here, I'll make it a little better! *hugs <@%s>*"]
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(normal_hugs) % (userID))
        else:
            hugself_reactions = ["Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*", "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?", "Well, as Club President, it's my job to set a good example! *hugs myself*"]
            mentioned_hugs = ["As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs %s*", "Of course I'll hug you! You don't have to even ask twice! *hugs %s*", "Have you had a rough day? Here, I'll make it a little better! *hugs %s*"]
            member = message.content.split(" ")[1]
            if member == "Monika" or member == "yourself" or member == '<@436351740787294208>':
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(hugself_reactions))
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(mentioned_hugs) % (member))

    if message.content.upper().startswith('M_HEADPAT'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(headpat_reactions))

    if message.content.upper().startswith('M_ASK'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(answers))

    if message.content.upper().startswith('M_TICKLE'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(laughs))

    if message.content.upper().startswith('M_QUOTE'):
        quotes = ["As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!", "I'm confident that we can all really grow this club before we graduate!", "Then that makes it official! Welcome to the Literature Club!", "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom.", "I guess you could say that I had some kind of epiphany recently. It's been influencing my poems a bit.", "...That's my advice for today! Thanks for listening~", "Wait...is this tip even about writing? What am I even talking about? Ahaha!", "Humans aren't two-dimensional creatures. I think you'd know that better than anyone.", "Also, that joke makes no sense in translation!", "And I also care about the well-being of my club members, you know?", "Have you thought that maybe you've always seen her as so cheerful because that's just how she is when she's around you?", "C-Catchphrase? I don't have a catchphrase...", "Yay, you picked me!", "You kind of left her hanging this morning, you know?", "Don't worry. I probably know a lot more than you think."]
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(quotes))

    if message.content.upper().startswith('M_DELETE'):
        userID = message.author.id
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("What do you need me to delete?")
        else:
            member = message.content.split(" ")[1]
            if member == "Monika" or member == "yourself" or member == '<@436351740787294208>' or member == "monika" or member == "characters/monika" or member == "characters/Monika":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ahahahaha! No.")
            elif member == "Sayori" or member == "Natsuki" or member == "Yuri" or member == "<@425696108455657472>" or member == "<@433834936450023424>" or member == "<@436350586670153730>" or member == "sayori" or member == "natsuki" or member == "yuri":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ahahahaha! You know, I tried that once. Didn't really work out well in the long run.")
            elif member == "me":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Why would I want to do that?")
            elif member == "<@270057011251642368>":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Why would you want to delete the man who gave you the ability to use me? Shame on you!")
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("os.remove(\"characters/%s.chr\")" % (member))

    if message.content.upper().startswith('M_INVITE'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send('https://discordapp.com/api/oauth2/authorize?client_id=436351740787294208&permissions=8&scope=bot')
# Pickling Stuff ###############################################################

    if message.content.upper().startswith('PICKLE_SAVE'):
        if message.author.id == 270057011251642368:
            with open('m_servers.pkl', 'wb') as pickle_file:
                pickle.dump(m_server_ids, pickle_file)
            with open('m_true.pkl', 'wb') as pickle_file:
                pickle.dump(m_toggle_true, pickle_file)
            with open('m_false.pkl', 'wb') as pickle_file:
                pickle.dump(m_toggle_false, pickle_file)
            await channel.send("Pickling officially saved!")
        else:
            pass

    if message.content.upper().startswith('PICKLE_LOAD'):
        if message.author.id == 270057011251642368:
            with open('m_servers.pkl', 'rb') as pickle_file:
                server_update = pickle.load(pickle_file)
                m_server_ids = server_update
            with open('m_true.pkl', 'rb') as pickle_file:
                toggle_true_update = pickle.load(pickle_file)
                m_toggle_true = toggle_true_update
            with open('m_false.pkl', 'rb') as pickle_file:
                toggle_false_update = pickle.load(pickle_file)
                m_toggle_false = toggle_false_update
            await channel.send("Pickling officially loaded!")
        else:
            pass

    if message.content.upper().startswith('M_TOGGLE'):
        if message.author.guild_permissions.administrator:
            ServerID = message.guild.id
            if ServerID in m_server_ids:
                pass
            else:
                m_server_ids.insert(0, ServerID)
                m_toggle_true.insert(0, ServerID)
            if ServerID in m_toggle_true:
                m_toggle_true.remove(ServerID)
                m_toggle_false.insert(0, ServerID)
                await channel.send("Ok, I guess you don't want to hear from me.")
            elif ServerID in m_toggle_false:
                m_toggle_false.remove(ServerID)
                m_toggle_true.insert(0, ServerID)
                await channel.send("Ok, I guess you do want to hear from me.")
        else:
            await channel.send("Better ask a Club President to help with that one! (you need admin to change this setting)")

# Monika Mentions ##############################################################

    if message.content.upper().startswith('<@436351740787294208>'):
        userID = message.author.id
        mention_responses = ["Yes?", "Does somebody need me?", "I'm here!"]
        if len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(mention_responses))
            return
        else:
            member = message.content.split(" ")[1]
            if 'hi' in message.content.lower() or 'hello' in message.content.lower() or 'hey' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(hellos))
                return
            elif 'test' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("As fine as I can be given my current realization of being nothing more than a videogame character turned Discord bot!")
                return
            elif 'i love you' in message.content.lower() or 'ily' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(love_reactions))
                return
            elif 'goodnight' in message.content.lower() or 'good night' in message.content.lower():
                if message.author.id == 433834936450023424:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodnight_reactions))
                    return
            elif 'good morning' in message.content.lower():
                if message.author.id == 433834936450023424:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodmorning_reactions))
                    return
            elif 'good afternoon' in message.content.lower():
                if message.author.id == 433834936450023424:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodafternoon_reactions))
                    return
            elif "you are" in message.content.lower() or "you're" in message.content.lower():
                if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower() or "cute" in message.content.lower() or "hot" in message.content.lower() or "amazing" in message.content.lower():
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(compliment_reactions))
                    return
                else:
                    pass
            elif 'loves you' in message.content.lower():
                if member == '<@425696108455657472>': #Sayori
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ahaha!~ Well, after everything that's happened between us, that's nice to hear!")
                    return
                elif member == '<@436350586670153730>': #Yuri
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly.")
                elif member == '<@433834936450023424>': #Natsuki
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oh, really? She, of all people, said that?")
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(mentioned_love_reactions) % (member))
                    return
            elif "sorry" in message.content.lower() or "apologize" in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(apology_reactions))
                return
            elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                if member == "Natsuki" or member == "Yuri" or member == "Sayori" or member == "<@425696108455657472>" or member == "<@436350586670153730>" or member == "<@433834936450023424>":
                    imbestgirl_reactions = ["I'm sorry, I didn't catch that. What did you say?", "Hm? Did you say something?", "Ahaha!~ You're funny!"]
                    await message.delete()
                    await channel.send(random.choice(imbestgirl_reactions))
                    return
                elif member == "is" or member == "<@436351740787294208>" or member == "you" or member == "you're":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!")
                    return
                else:
                    pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I'm afraid I don't understand what you said. I'm terribly sorry!")
                return

# Other Bot Interactions #######################################################

    if '<@436351740787294208>' in message.content.lower():
        if message.author.id == 425696108455657472: #Sayori
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~")
                return
        elif message.author.id == 436350586670153730: #Yuri
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Aw, no need to be shy, Yuri! I don't mind a hug every now and then!")
                return
        elif message.author.id == 433834936450023424: #Natsuki
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Aww, how cute of you, Natsuki!")
                return

    if message.author.id == 433834936450023424: #Natsuki
        if "okay, this is just awkward for both of us." in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Yeah, I agree.")
            return
        elif "act 2 says otherwise." in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("I said I was sorry!")
            return
        else:
            pass

    if message.author.id == 436350586670153730: #Yuri
        if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in message.content.lower():
            await asyncio.sleep(3)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Hm. I don't really like this Yuri too much. Give me a second.")
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("y_act1")
            return

# Feed Monika ##################################################################

    if message.content.upper().startswith('M_FEED'):
        if len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("I suppose I am a bit hungry... What do you recommend?")
        else:
            member = message.content.split(" ")[1]
            # Cookie
            if member == u"\U0001F36A":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Not as homemade as Natsuki's, but it's still very delicious! Thank you!")
            # Pizza
            elif member == u"\U0001F355":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ah... There's pepperoni on it... You do remember I'm a vegetarian, right?")
            # Burger
            elif member == u"\U0001F354":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Is it a veggie burger? If not, I'll have to respectfully decline.")
            # Cold Foods
            elif member == u"\U0001F367" or member == u"\U0001F366" or member == u"\U0001F368":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ah, nothing like some cold treats to brighten your day!")
            # Japanese Foods
            elif member == u"\U0001F363" or member == u"\U0001F371" or member == u"\U0001F35B" or member == u"\U0001F359" or member == u"\U0001F35A" or member == u"\U0001F358" or member == u"\U0001F35C" or member == u"\U0001F362" or member == u"\U0001F361" or member == u"\U0001F365":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Aw, you brought me a meal from my home? How thoughtful of you!")
            # Alcohol
            elif member == u"\U0001F37A" or member == u"\U0001F37B" or member == u"\U0001F377" or member == u"\U0001F378" or member == u"\U0001F379" or member == u"\U0001F37E" or member == u"\U0001F376" or member == u"\U0001F942" or member == u"\U0001F943":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Oh! Ahaha... A-As curious as I am, I'm afraid I cannot allow alcoholic beverages here.")
            # Coffee
            elif member == u"\u2615":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ah, thank you! I've been needing something to wake me up a bit!")
            # Tea
            elif member == u"\U0001F375":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("It's like I'm back in the clubroom! All I need is one of Natsuki's cupcakes.")
            # Bread
            elif member == u"\U0001F35E" or member == u"\U0001F956":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("It's a start, but I'll need to go to the grocery store to make a proper sandwich. ~~Would you like to come with?~~")
            # Hot Pepper
            elif member == u"\U0001F336":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("*cough cough* Oh, my! That certainly caught me off-guard!")
            # Cooking
            elif member == u"\U0001F373":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Hm... as a vegetarian, would it even be okay to eat this...?")
            # Mexican Food
            elif member == u"\U0001F32E" or member == u"\U0001F32F":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Well, I'm always in the mood for something different!")
            # Sweets
            elif member == u"\U0001F370" or member == u"\U0001F36E" or member == u"\U0001F36C" or member == u"\U0001F36B" or member == u"\U0001F369" or member == u"\U0001F36D":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Sweets! A girl's best friend!")
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
                await channel.send("U-Um... I'm not sure what you're insinuating here...")
            # Egg
            elif member == u"\U0001F95A":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Oh, you silly goose! Are you trying to be funny?")
            # Silverware
            elif member == u"\U0001F374" or member == u"\U0001F37D" or member == u"\U0001F944":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I've got my silverware ready! What are we eating with them?")
            # Milk
            elif member == u"\U0001F95B":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I suppose it's a good thing I'm not a vegan! Ahaha~!")
            # Birthday Cake
            elif member == u"\U0001F382":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("How wonderful, but I don't believe it's my birthday just yet...")
            # Meat
            elif member == 	u"\U0001F357" or member == u"\U0001F356" or member == u"\U0001F32D" or member == u"\U0001F364" or member == u"\U0001F953":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Um... H-Have you forgotten that I'm a vegetarian...?")
            # Squid
            elif member == 	u"\U0001F991":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("That joke still makes no sense in translation.")
            # Misc.
            elif member == u"\U0001F34E" or member == u"\U0001F34F" or member == u"\U0001F350" or member == u"\U0001F34A" or member == u"\U0001F34B" or member == u"\U0001F34C" or member == u"\U0001F349" or member == u"\U0001F347" or member == u"\U0001F353" or member == u"\U0001F348" or member == u"\U0001F352" or member == u"\U0001F351" or member == u"\U0001F34D" or member == u"\U0001F345" or member == u"\U0001F346" or member == u"\U0001F33D" or member == u"\U0001F360" or member == u"\U0001F36F" or member == u"\U0001F35F" or member == u"\U0001F35D" or member == u"\U0001F950" or member == u"\U0001F951" or member == u"\U0001F952" or member == u"\U0001F954" or member == u"\U0001F955" or member == u"\U0001F957" or member == u"\U0001F958" or member == u"\U0001F959" or member == u"\U0001F95C" or member == u"\U0001F95D" or member == u"\U0001F95E" or member == u"\U0001F9C0":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("A nice meal is always great! Thank you~")
            # Not Food
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Um.. not to be rude, but I don't think this is edible.")

# Help #########################################################################

    if message.content.upper().startswith('M_HELP'):
        embed = discord.Embed(title="Greetings! I'm Monika!", description="Cole ~~finally~~ turned my .chr file into a .py file so I can join Discord! I'm not fully self-aware like I was in DDLC, but this will have to suffice!", color=0x12ba01)
        embed.add_field(name="m_ask", value="Use this to ask me a yes-or-no question. I'm admittedly not the smartest person ~~in the game~~ on Earth, but I'll try my hardest to answer correctly!", inline=True)
        embed.add_field(name="m_delete", value="Do you need something 'deleted' from your server? I'll be happy to help!", inline=True)
        embed.add_field(name="m_feed", value="Would you like to feed me something? You can with this command!", inline=True)
        embed.add_field(name="m_headpat", value="Ahaha! I don't understand the appeal of patting girls on the head, but I suppose I can figure it out...", inline=True)
        embed.add_field(name="m_hug", value="I'm always open to giving a hug to anyone who wants one! Or, let's be honest, even if they *don't* want one!", inline=True)
        embed.add_field(name="m_tickle", value="O-Oh! Well, I guess there are worse things to do to me than tickling!", inline=True)
        embed.add_field(name="I do believe that's it!", value="I'm still in very early stages of development, but if Cole was able to create the other girls quickly, I'm sure I'll be finished before you know it!")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await channel.send(embed=embed)
        return



client.run("REDACTED")
