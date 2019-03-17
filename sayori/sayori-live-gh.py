import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import emoji
import pickle

client = commands.AutoShardedBot(command_prefix="s_")

e = discord.Embed()

hangtoggle = True

chat_filter = ["NIGGER"]
hang_words = ["HANG", "HANGING", "HUNG", "HANGED"]
name_words = ["CINNAMON BUN", "BEST GIRL"]
goodnight_words = ["GOODNIGHT", "GN", "GOODNIGHT,", "GOODNIGHT!"]
kill_words = ["KILL"]
breakfast_words =["BREAKFAST"]

s_poem_intros = ["Oh, I really loved writing this one!", "I hope you like it!", "I can't wait to show you this one!"]
n_poem_intros = ["I hope she doesn't get mad at me for showing you this...", "Oh! This is one of Natsuki's best poems!", "Aw, this is a cute one, just like her!"]
y_poem_intros = ["Oooo, Yuri did a great job with this one!", "I personally don't get what she's saying with this one, but I still like it!", "I kinda like this side of Yuri, if I'm being honest!"]
m_poem_intros = ["Well, her writing style is unique, to say the least.", "I love how abstract Monika's writing is!", "There's a reason she's the president of the club!"]

hang_reactions = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
meanie_reactions = ["Do we have a meanie in the server? If so, please stop.", "Cease your bulli, you meanie!", "Boo! You meanie..."]
name_reactions = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
goodnight_reactions = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
goodmorning_reactions = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
hellos = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]
love_reactions = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]
no_responses = ["Huh? I don't understand.", "I don't get it.", "???", "Maybe try something I actually understand?"]
hugself_reactions = ["A hug for me? Yay! *hugs myself*", "Well, if you insist! *hugs myself*", "Awww, you're too kind! *hugs myself*", "How can I say no to that? *hugs myself*"]
meanie_tag_reactions = ["Hey! Stop being a meanie, %s!", "We don't like meanies on this server, %s!", "Are you being a meanie, %s? If so, please stop."]
beautiful_reactions = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]
love_tag_reactions = ["Aww! Well, you can tell %s that I love them, too!", "%s does? Well, that's so sweet to hear!", "And I love %s, too! :heart:", "Yay! I'm loved by %s!"]
apology_reactions = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]
russian_reactions = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
swears = ["HECK!", "DARN IT!", "POOP!", "CRAP!", "FRICK!", "SON OF A BISCUIT!", "MOTHERTRUCKER!"]
laughs = ["Hehehehehe!~", "Ahahahaha!!", "*giggles*", "**PFFFT AHAHAHAHAHAHHAHAHAHHAHA!!!!!**", "Ehehe!~", "WAHAHAHAHAHA!!!~"]
goodafternoon_reactions = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
headpat_reactions = ["Hehehe!~", "Just don't mess up my bow!", "S-stop being so silly! :blush:", "Well, my hair's already pretty messy, so I don't see an issue!", "Hehehe! Thank you!"]
suicide_prevention = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]

breakfast_reactions = ["I WANT BREAKFAST!"]
jokes = ["What do you call a mix between a fish and an elephant? Swimming trunks!", "I was going to tell a joke about a skunk, but, honestly, it really stinks.", "Why did the rooster cross the road? To prove he wasn't a chicken!", "Why did the golfer wear two pairs of pants? In case he got a hole in one!", "I have severe depression. That's not a joke, it's a cry for help.", "My life. Ehehe...~", "What do you get when you cross an author and an alcoholic? Ernest Hemmingway!", "What do you call fake spaghetti? An im-pasta!", "Why don't cannibals eat clowns? Because they taste funny...", "What do you call a bird that sticks to everything? A vel-crow!", "What do you call a sleepwalking nun? A Roamin' Catholic!", "What's brown and sticky? A stick!", "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.", "How many tickles does it take to make an octopus laugh? Ten tickles!", "Why do stadiums get hot after games? All the fans left!", "What do attorneys wear to court? Lawsuits!", "Why are there gates around cemeteries? Everyone is dying to get in!", "Why did the baby strawberry cry? His parents were in a jam!", "I was gonna tell a joke about a broken pencil, but it's pointless.", "The past, present, and future walk into a bar. It was tense.", "How do you comfort the Grammar Police? \"There, they're, their...\"", "Is there a word in the English language that uses all 5 vowels, as well as 'y'? Unquestionably!", "Once, I was spacing out in class and my English teacher asked me to name two pronouns. Not sure who she was talking to, I replied, \"Who, me?\"", "Why do writers feel so cold? They're surrounded by drafts!", "A man went into a library and asked for a book on how to commit suicide. The librarian replies, \"Why would I give you that? You won't return it!\"", "\"I'm sorry\" and \"I apologize\" mean the same thing. Unless you're at a funeral.", "A dyslexic man walks into a bra..."]
normal_hugs = ["One hug, coming right up! *hugs <@%s>*", "I'll try not to squeeze too hard! *hugs <@%s>*", "Time for the super-mega-cinnamon-bun hug! *hugs <@%s>*", "How could I say no to a hug? *hugs <@%s>*", "Yay, hugs! *hugs <@%s>*"]
quotes = ["I want breakfast.", "AAAAAaaaaAAAAAAAAHH!!!!", "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head", "I made eggs and toast!", "It's bad to skip breakfast! I get all cranky...", "I was playing with the crayons and smacked my forehead into the shelf!", "Yuri's boobs are just as they've always been! Big and beautiful!", "I did something bad, and now I have to accept the revolution!", "This isn't the napping club!", "I'm fine with--looking like a unicorn--", "So, if I keep it unbuttoned then I won't get a boyfriend, right?"]
mentioned_hugs = ["One hug, coming right up! *hugs %s*", "I'll try not to squeeze too hard! *hugs %s*", "Time for the super-mega-cinnamon-bun hug! *hugs %s*", "How could I say no to a hug? *hugs %s*", "Yay, hugs! *hugs %s*"]


answers = ["Yes!", "No.", "Maybe.", "Possibly?", "Of course, silly!", "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!", "I'd say ask Yuri, but she's a little shy at the moment.", "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!", "You've got a better chance of having a happy ending in DDLC! Ehehe...~", "Maybe we should ask The Magic Conch, instead.", "As sure as I'm depressed!", "Not really.", "My Vice President Powers tell me yes!", "My Vice President Powers tell me no!", "My Vice President Powers tell me maybe!", "J-Just a little bit!"]

#ok so heres the cooldowns. the current implementation goes like this:
#	after a command has been entered, add the user to the list
#	if the user tries to run the command again while their name is in the list, dont do the command
#	after 5 seconds, remove that user from the list
#it seems like there are times when that code that removes the user from the list doesnt run. what we really should do is:
#	after a command has been entered, set the users value to the time that the command was run
#	if the user tries to run the command again while their name's value is greater than the current time plus however long the cooldown is, dont do the command
#	every certain amount of time (maybe 15 to 30 minutes) clear all values that have expired (maybe even the whole map, it shouldnt hurt) so the map doesnt become huge

#of course these lists need to be changed to maps

ask_cooldown = []
commands_cooldown = []
feed_cooldown = []
headpat_cooldown = []
help_cooldown = []
hug_cooldown = []
invite_cooldown = []
joke_cooldown = {}
lifeline_cooldown = []
poems_cooldown = []
quote_cooldown = []
swear_cooldown = []
tickle_cooldown = []

s_server_ids = []
s_hang_true_ids = []
s_hang_false_ids = []

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Type 's_help' for help!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Doki Doki Literature Club"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="with the crayons!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Katawa Shoujo"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="with Mr. Cow!"))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
#    client.emojis()
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Agent Sayori, prepared for duty!")

@client.event
async def on_message(message):
    global s_server_ids
    global s_hang_true_ids
    global s_hang_false_ids
    global ask_cooldown
    global commands_cooldown
    global feed_cooldown
    global headpat_cooldown
    global help_cooldown
    global hug_cooldown
    global invite_cooldown
    global joke_cooldown
    global lifeline_cooldown
    global poems_cooldown
    global quote_cooldown
    global swear_cooldown
    global tickle_cooldown

    channel = message.channel
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            userID = message.author.id
            await message.delete()
            await channel.send("Hey! Don't be such a meanie, <@%s>!" % (userID))
        elif word.upper() in hang_words:
            chat_serverID = message.guild.id
            if chat_serverID in s_hang_false_ids:
                pass
            else:
                if message.author.id == 425696108455657472:
                    pass
                elif message.content.upper().startswith('<@425696108455657472>'):
                    pass
                elif 'myself' in message.content.lower():
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(suicide_prevention))
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(hang_reactions))
                    return
        elif word.upper() in breakfast_words:
            chat_serverID = message.guild.id
            if chat_serverID in s_hang_false_ids:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(breakfast_reactions))
                return
        elif word.upper() in name_words:
            chat_serverID = message.guild.id
            if chat_serverID in s_hang_false_ids:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(name_reactions))
                return
        elif word.upper() in goodnight_words:
            chat_serverID = message.guild.id
            if chat_serverID in s_hang_false_ids:
                pass
            elif message.author.id == 425696108455657472 or '<@433834936450023424>' in message.content.lower() or message.author.id == 433834936450023424 or message.author.id == 436350586670153730 or message.author.id == 436351740787294208 or '<@436351740787294208>' in message.content.lower():
                pass
            elif message.content.upper().startswith('<@425696108455657472>') or message.content.upper().startswith('<@436350586670153730>') or message.content.upper().startswith('<@436351740787294208>'):
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(goodnight_reactions))
                return
        elif word.upper() in kill_words:
            chat_serverID = message.guild.id
            if chat_serverID in s_hang_false_ids:
                pass
            elif message.author.id == 425696108455657472 or '<@433834936450023424>' in message.content.lower() or message.author.id == 433834936450023424 or message.author.id == 436350586670153730:
                pass
            elif message.content.upper().startswith('<@425696108455657472>') or message.content.upper().startswith('<@436350586670153730>'):
                pass
            elif 'myself' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(suicide_prevention))
                return
            elif message.author.id == 384408091044872205:
                if 'kill me' in message.content.lower():
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Why would a perfectly good piece of candy want to die?")
                    return
                else:
                    pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Can we change the topic to something more wholesome, please?")
                return

    if message.content.upper().startswith('S_TYPE'):
        await channel.trigger_typing()

    if message.content.upper().startswith('S_JOKE'):
        Author = message.author.id
        CurTime = time.time()
        if Author in joke_cooldown and joke_cooldown[Author] > CurTime():
            await channel.send("Hold on! I need time to think of another joke for you...")
            return
        else:
            joke_cooldown[Author] = CurTime + 5.0
            print("added %s to cooldown" % Author)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
#jokes moved to top
            await channel.send(random.choice(jokes))
            await asyncio.sleep(5)
            if Author in joke_cooldown:
                del joke_cooldown[Author]
                print("removed %s from cooldown" % Author)
            return

    if message.content.upper().startswith('S_HUG'):
        Author = message.author.id
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif Author in hug_cooldown:
            await channel.send("Give me a few seconds; I'm still getting over how nice that last hug was!")
            return
        else:
            userID = message.author.id
            if len(message.content.split(" ")) == 1:
                hug_cooldown.insert(0, Author)
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(normal_hugs) % (userID))
                await asyncio.sleep(5)
                hug_cooldown.remove(Author)
                return
            else:
                member = message.content.split(" ")[1]
                if member == "Sayori" or member == "yourself" or '<@425696108455657472>' in message.content.lower():
                    hug_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(hugself_reactions))
                    await asyncio.sleep(5)
                    hug_cooldown.remove(Author)
                    return
                elif member == "hang" or member == "hanged" or member == "hanging" or member == "hung" or member == "nigger":
                    pass
                else:
                    hug_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(mentioned_hugs) % (member))
                    await asyncio.sleep(5)
                    hug_cooldown.remove(Author)
                    return

    if message.content.upper().startswith('S_HEADPAT'):
        Author = message.author.id
        if Author in headpat_cooldown:
            await channel.send("Let me fix my bow real quick...")
        else:
            headpat_cooldown.insert(0, Author)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(headpat_reactions))
            await asyncio.sleep(5)
            headpat_cooldown.remove(Author)
            return

# @Sayori Responses

    if message.content.upper().startswith('<@425696108455657472>'):
        userID = message.author.id
        if len(message.content.split(" ")) == 1:
            if message.author.id == 433834936450023424 or message.author.id == 436350586670153730:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(name_reactions))
                return
        else:
            member = message.content.split(" ")[1]
            if 'hi' in message.content.lower() or 'hello' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(hellos))
                return
            elif 'test' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Testing, testing! 1-2-1-2 testing!")
                return
            elif 'i love you' in message.content.lower() or 'ily' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(love_reactions))
                return
            elif 'goodnight' in message.content.lower() or 'good night' in message.content.lower():
                if message.author.id == 425696108455657472:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodnight_reactions))
                    return
            elif 'good morning' in message.content.lower():
                if message.author.id == 425696108455657472:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodmorning_reactions))
                    return
            elif 'good afternoon' in message.content.lower():
                if message.author.id == 425696108455657472:
                    pass
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(goodafternoon_reactions))
                    return
            elif 'hang' in message.content.lower() or 'hanged' in message.content.lower() or 'hanging' in message.content.lower() or 'hung' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(hang_reactions))
                return
            elif 'is a meanie' in message.content.lower() or 'being a meanie' in message.content.lower() or 'are a meanie' in message.content.lower() or 'are being a meanie' in message.content.lower():
                if 'nigger' in message.content.lower():
                    pass
                elif member == 'Sayori' or member == "sayori" or member == "you" or member == "you're" or member == 'is' or member == '<@425696108455657472>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Eh?? No, I'm not!!")
                    return
                elif member == 'Natsuki' or member == 'natsuki' or member == '<@433834936450023424>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Hey, she may be spunky, but she's not a meanie!")
                    return
                elif member == 'Yuri' or member == 'yuri' or member == '<@436350586670153730>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("What?? Yuri is the last person who would ever be a meanie!")
                    return
                elif member == 'Monika' or member == 'monika' or member == '<@436351740787294208>':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Monika isn't a meanie! And no, I don't feel obligated to say that for fear of her deleting me again...")
                    return
                elif member == 'MC' or member == 'mc' or member == 'Mc' or member == 'Anon' or member == 'anon' or member == '[player]':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Yeah, I guess he is a bit of a meanie, but I know he means well!")
                    return
                elif member == 'everyone' or member == '@everyone' or member == '@here' or member == 'everybody':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("No offense, but I don't think it's possible for EVERYONE to be being a meanie right now...")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(meanie_tag_reactions) % (member))
            elif 'you are cute' in message.content.lower() or 'you\'re cute' in message.content.lower() or 'you are beautiful' in message.content.lower() or 'you\'re beautiful' in message.content.lower() or 'you are so cute' in message.content.lower() or 'you\'re so cute' in message.content.lower() or 'you are so beautiful' in message.content.lower() or 'you\'re so beautiful' in message.content.lower() or 'you are pretty' in message.content.lower() or 'you\'re pretty' in message.content.lower() or 'you are so pretty' in message.content.lower() or 'you\'re so pretty' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(beautiful_reactions))
                return
            elif 'loves you' in message.content.lower():
                if 'nigger' in message.content.lower():
                    pass
                elif member == '<@433834936450023424>': #Natsuki
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Awww, she does??")
                    return
                elif member == '<@436350586670153730>': #Yuri
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Well, of course she does! Yuri loves everybody!")
                elif member == '<@436351740787294208>': #Monika
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Yay! I'm glad she does!")
                elif member == 'everyone' or member == '@everyone' or member == '@here' or member == 'everybody':
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("R-really? EVERYONE? Oh, my!")
                    return
                else:
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send(random.choice(love_tag_reactions) % (member))
                    return
            elif 'sorry' in message.content.lower() or 'apologize' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(apology_reactions))
                return
            elif 'syka blyat' in message.content.lower() or 'pidor ebony' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(russian_reactions))
                return
            elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                if member == "Monika" or member == "Natsuki" or member == "Yuri" or member == "<@436350586670153730>" or member == "<@433834936450023424>":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Well, I respect your opinion!")
                    return
                elif member == "is" or member == "<@436350586670153730>" or member == "you" or member == "you're":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("S-Stop it! That's not true!")
                    return
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(no_responses))
                return

# Other Bot Interactions

    if '<@425696108455657472>' in message.content.lower():
        if message.author.id == 433834936450023424: #Natsuki
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Hehehe! You give the best hugs, Natsuki!")
            elif "s-shut up! no she doesn't!" in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Oh, yes I do!")
            else:
                pass
        elif message.author.id == 436350586670153730: #Yuri
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Aww, thank you, Yuri!")
                return
        elif message.author.id == 436351740787294208: #Monika
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ehehe! I love your hugs, Monika! You should give them more often!")
                return
        else:
            pass

    if message.author.id == 433834936450023424: #Natsuki
        if "s-shut up! no she doesn't!" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Oh, yes I do!")
        elif "s-shut up! no, i don't!" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Awww... :(")
        else:
            pass
    elif message.author.id == 436350586670153730: #Yuri
        if "h-hey! don't hug so hard, sayori!" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Oops! I'm sorry!")
        elif "haha. well, she is a loving soul." in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("You bet your booty I am! :yum:")
            return
        elif "who the hell is sayori? i don't know any sayoris..." in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!")
            return
        elif "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in message.content.lower():
            await asyncio.sleep(3)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send(":disappointed_relieved: :cold_sweat: :confounded: :sob:")
            return
        elif "i'm sorry, who are you? and why are you hugging me?" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("I-It's me, Sayori! And I-I just wanted to hug you!")
            return
        elif "sorry, but i don't know you. please get your messy, stupid self away from me." in message.content.lower():
            await asyncio.sleep(3)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("O-Okay... I'm sorry... :pensive:")
            return
        else:
            pass
    elif message.author.id == 436351740787294208: #Monika
        if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in message.content.lower():
            await asyncio.sleep(3)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("Hey, everyone deserves forgiveness! Even you, Monika!")
            return

########################################

    if ('@everyone' or '@here') in message.content.lower() and message.content.upper().startswith("S_"):
        await message.delete()
        await channel.send("We don't need to get everyone's attention!")
        return

    if 'cinnamon bun' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids:
            pass
        elif message.content.upper().startswith("S_ASK"):
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(name_reactions))
            return

    if 'meanie' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids or 'nigger' in message.content.lower():
            pass
        elif message.content.upper().startswith('<@425696108455657472>'):
            pass
        elif message.author.id == 425696108455657472:
            pass
        elif message.content.upper().startswith('S_ASK'):
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(meanie_reactions))
            return

    if 'good morning' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids:
            pass
        elif message.content.upper().startswith('<@425696108455657472>') or message.content.upper().startswith('<@436350586670153730>') or message.content.upper().startswith('<@436351740787294208>'):
            pass
        elif message.author.id == 425696108455657472 or message.author.id == 436350586670153730 or message.author.id == 436351740787294208:
            pass
        elif message.content.upper().startswith('S_ASK'):
            pass
        elif '<@433834936450023424>' in message.content.lower() or message.author.id == 433834936450023424:
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(goodmorning_reactions))
            return

    if 'good night' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids:
            pass
        elif message.content.upper().startswith('<@425696108455657472>') or message.content.upper().startswith('<@436350586670153730>') or message.content.upper().startswith('<@436351740787294208>'):
            pass
        elif message.author.id == 425696108455657472 or message.author.id == 436350586670153730 or message.author.id == 436351740787294208:
            pass
        elif message.content.upper().startswith('S_ASK'):
            pass
        elif '<@433834936450023424>' in message.content.lower() or message.author.id == 433834936450023424:
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(goodnight_reactions))
            return

    if 'good afternoon' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids:
            pass
        elif message.content.upper().startswith('<@425696108455657472>') or message.content.upper().startswith('<@436350586670153730>') or message.content.upper().startswith('<@436351740787294208>'):
            pass
        elif message.author.id == 425696108455657472 or message.author.id == 436350586670153730 or message.author.id == 436351740787294208:
            pass
        elif message.content.upper().startswith('S_ASK'):
            pass
        elif '<@433834936450023424>' in message.content.lower() or message.author.id == 433834936450023424:
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(goodafternoon_reactions))
            return

    if 'commit suicide' in message.content.lower():
        chat_serverID = message.guild.id
        if chat_serverID in s_hang_false_ids:
            pass
        elif message.author.id == 425696108455657472:
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(suicide_prevention))
            return

    if message.content.upper().startswith('S_QUOTE'):
        Author = message.author.id
        if Author in quote_cooldown:
            await channel.send("I've got a lot of quotes; I just need to think of another one real fast...")
            return
        else:
            quote_cooldown.insert(0, Author)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(quotes))
            await asyncio.sleep(5)
            quote_cooldown.remove(Author)
            return

    if message.content.upper().startswith('S_POEMS'):
        Author = message.author.id
        if Author in poems_cooldown:
            await channel.send("I just pulled the list up, you silly goose! No need to pull it up again right away!")
            return
        else:
            poems_cooldown.insert(0, Author)
            await channel.send("Don't worry, there are a lot of poems, so I don't blame you for forgetting some of them!")
            await channel.send("```s_poem dear sunshine \ns_poem bottles \ns_poem % \ns_poem eagles can fly \ns_poem amy likes spiders \ns_poem i'll be your beach \ns_poem because you \ns_poem ghost under the light \ns_poem 2 ghost under the light \ns_poem the raccoon \ns_poem beach \ns_poem hole in wall \ns_poem 2 hole in wall \ns_poem save me \ns_poem the lady who knows everything \ns_poem happy end```")
            await asyncio.sleep(10)
            poems_cooldown.remove(Author)
            return

# Feed Sayori

    if message.content.upper().startswith('S_FEED'):
        Author = message.author.id
        if Author in feed_cooldown:
            await asyncio.sleep(message.channel, "Hol' on. Shtill eatin'.")
            return
        else:
            if len(message.content.split(" ")) == 1:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("You wanna feed me something? I'm open for anything!")
            else:
                member = message.content.split(" ")[1]
                # Cookie
                if member == u"\U0001F36A":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("A cookie?? Yummy! Thank you so much!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Pizza
                elif member == u"\U0001F355":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I love pizza! Thanks!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Burger
                elif member == u"\U0001F354":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Mmmmm! Burgers are delicious!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Cold Foods
                elif member == u"\U0001F367" or member == u"\U0001F366" or member == u"\U0001F368":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("AHH! Brain freeze!!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Japanese Foods
                elif member == u"\U0001F363" or member == u"\U0001F371" or member == u"\U0001F35B" or member == u"\U0001F359" or member == u"\U0001F35A" or member == u"\U0001F358" or member == u"\U0001F35C" or member == u"\U0001F362" or member == u"\U0001F361" or member == u"\U0001F365":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Oooo! Japanese food! Reminds me of home!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Alcohol
                elif member == u"\U0001F37A" or member == u"\U0001F37B" or member == u"\U0001F377" or member == u"\U0001F378" or member == u"\U0001F379" or member == u"\U0001F37E" or member == u"\U0001F376" or member == u"\U0001F942" or member == u"\U0001F943":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("H-Hey! I'm too young for that!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Coffee
                elif member == u"\u2615":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ah, the delicious beverage known as coffee! Where would I be without thee?")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Tea
                elif member == u"\U0001F375":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("How could I refuse a hot cup of tea? Thank you!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Bread
                elif member == u"\U0001F35E" or member == u"\U0001F956":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I mean, I suppose I could survive off of plain bread...")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Cheese
                elif member == u"\U0001F9C0":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I'm a mousie! Squeak squeak!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Hot Pepper
                elif member == u"\U0001F336":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("***OWOWOWOWHOTHOTHOTHOT!!!***")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Cooking
                elif member == u"\U0001F373":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I made eggs and toast!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Mexican Food
                elif member == u"\U0001F32E" or member == u"\U0001F32F":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ole!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Sweets
                elif member == u"\U0001F370" or member == u"\U0001F36E" or member == u"\U0001F36C" or member == u"\U0001F36D" or member == u"\U0001F36B" or member == u"\U0001F369":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Sweets! My one, true weakness!! *omnomnomnomnom*")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Popcorn
                elif member == u"\U0001F37F":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("*crunch crunch crunch*")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Baby Bottle
                elif member == u"\U0001F37C":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Hey! I'm not a baby!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Egg
                elif member == u"\U0001F95A":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I feel like I should cook this, first...")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Silverware
                elif member == u"\U0001F374" or member == u"\U0001F37D" or member == u"\U0001F944":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("I didn't know you could eat silverware!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Milk
                elif member == u"\U0001F95B":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ah, a nice, cold glass of milk is always welcoming!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Birthday Cake
                elif member == u"\U0001F382":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("It's not my birthday, but I accept!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Misc.
                elif member == u"\U0001F34E" or member == u"\U0001F34F" or member == u"\U0001F350" or member == u"\U0001F34A" or member == u"\U0001F34B" or member == u"\U0001F34C" or member == u"\U0001F349" or member == u"\U0001F347" or member == u"\U0001F353" or member == u"\U0001F348" or member == u"\U0001F352" or member == u"\U0001F351" or member == u"\U0001F34D" or member == u"\U0001F345" or member == u"\U0001F346" or member == u"\U0001F33D" or member == u"\U0001F360" or member == u"\U0001F36F" or member == u"\U0001F357" or member == u"\U0001F356" or member == u"\U0001F364" or member == u"\U0001F35F" or member == u"\U0001F32D" or member == u"\U0001F35D" or member == u"\U0001F950" or member == u"\U0001F951" or member == u"\U0001F952" or member == u"\U0001F953" or member == u"\U0001F954" or member == u"\U0001F955" or member == u"\U0001F957" or member == u"\U0001F958" or member == u"\U0001F959" or member == u"\U0001F95C" or member == u"\U0001F95D" or member == u"\U0001F95E":
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("*om nom nom* Thank you! That was delicious! :grin:")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return
                # Not Food
                else:
                    feed_cooldown.insert(0, Author)
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ptoo ptoo! This isn't food, you meanie!")
                    await asyncio.sleep(5)
                    feed_cooldown.remove(Author)
                    return

    if message.content.upper().startswith('S_ASK'):
        UserID = message.author.id
        if UserID in ask_cooldown:
            await channel.send("Please, please! I can only answer so many of your questions at once!")
            return
        else:
            ask_cooldown.insert(0, UserID)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(answers))
            await asyncio.sleep(5)
            ask_cooldown.remove(UserID)
            return

    if message.content.upper().startswith('S_SWEAR'):
        Author = message.author.id
        if Author in swear_cooldown:
            await channel.send("Jus' gotta get tis soap outta ma mout...")
            return
        else:
            swear_cooldown.insert(0, Author)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(swears))
            await asyncio.sleep(5)
            swear_cooldown.remove(Author)
            return

    if message.content.upper().startswith('S_TICKLE'):
        Author = message.author.id
        if Author in tickle_cooldown:
            await channel.send("Time out! Time out!! Ahaha!")
            return
        else:
            tickle_cooldown.insert(0, Author)
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(laughs))
            await asyncio.sleep(5)
            tickle_cooldown.remove(Author)
            return

    if message.content.upper().startswith('S_LIFELINE'):
        await channel.send("Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255")

# Poems (Sayori)

    if message.content.upper().startswith('S_POEM DEAR SUNSHINE'):
        await channel.send(random.choice(s_poem_intros))
        embed = discord.Embed(title="Dear Sunshine", description="*by Sayori*", color=0x3eb0ff)
        await channel.send(embed=embed)
        await channel.send("The way you glow through my blinds in the morning \nIt makes me feel like you missed me. \nKissing my forehead to help me out of bed. \nMaking me rub the sleepy from my eyes. \n \nAre you asking me to come out and play? \nAre you trusting me to wish away a rainy day? \nI look above. The sky is blue. \nIt's a secret, but I trust you too. \n \nIf it wasn't for you, I could sleep forever. \nBut I'm not mad. \n \nI want breakfast.")
        return

    if message.content.upper().startswith('S_POEM BOTTLES'):
        await channel.send(random.choice(s_poem_intros))
        embed = discord.Embed(title="Bottles", description="*by Sayori*", color=0x3eb0ff)
        await channel.send(embed=embed)
        await channel.send("I pop off my scalp like the lid of a cookie jar. \nIt's the secret place where I keep all my dreams. \nLittle balls of sunshine, all rubbing together like a bundle of kittens \nI reach inside with my thumb and forefinger and pluck one out. \nIt's warm and tingly. \nBut there's no time to waste! I put it in a bottle to keep it safe. \nAnd I put the bottle on the shelf with all of the other bottles. \nHappy thoughts, happy thoughts, happy thoughts in bottles, all in a row. \n \nMy collection makes me lots of friends. \nEach bottle a starlight to make amends. \nSometimes my friend feels a certain way. \nDown comes a bottle to save the day. \n \nNight after night, more dreams. \nFriend after friend, more bottles. \nDeeper and deeper my fingers go. \nLike exploring a dark cave, discovering the secrets hiding in the nooks and crannies. \nDigging and digging. \nScraping and scraping. \n \nI blow dust off my bottle caps. \nIt doesn't feel like time elapsed. \nMy empty shelf could use some more. \nMy friends look through my locked front door. \n \nFinally, all done. I open up, and in come my friends. \nIn they come, in such a hurry. Do they want my bottles that much? \nI frantically pull them from the shelf, one after the other. \nHolding them out to each and every friend. \nEach and every bottle. \nBut every time I let one go, it shatters against the tile between my feet. \nHappy thoughts, happy thoughts, happy thoughts in shards, all over the floor. \n \nThey were supposed to be for my friends, my friends who aren't smiling. \nThey're all shouting, pleading. Something. \nBut all I hear is echo, echo, echo, echo, echo \nInside my head.")
        return

    if message.content.upper().startswith('S_POEM %'):
        await channel.send(random.choice(s_poem_intros))
        embed = discord.Embed(title="%", description="*by Sayori*", color=0x3eb0ff)
        await channel.send(embed=embed)
        await channel.send("Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of \nGet. \nOut. \nOf. \nMy. \nHead. \n \n \n \nGet out of my head before I do what I know is best for you. \nGet out of my head before I listen to everything she said to me. \nGet out of my head before I show you how much I love you. \nGet out of my head before I finish writing this poem. \n \n \n \nBut a poem is never actually finished. \nIt just stops moving.")
        return

# Poems (Natsuki)

    if message.content.upper().startswith('S_POEM EAGLES CAN FLY'):
        await channel.send(random.choice(n_poem_intros))
        embed = discord.Embed(title="Eagles Can Fly", description="*by Natsuki*", color=0xff42e2)
        await channel.send(embed=embed)
        await channel.send("Monkeys can climb \nCrickets can leap \nHorses can race \nOwls can seek \nCheetahs can run \nEagles can fly \nPeople can try \nBut that's about it.")

    if message.content.upper().startswith('S_POEM AMY LIKES SPIDERS'):
        await channel.send(random.choice(n_poem_intros))
        embed = discord.Embed(title="Amy Likes Spiders", description="*by Natsuki*", color=0xff42e2)
        await channel.send(embed=embed)
        await channel.send("You know what I heard about Amy? \nAmy likes spiders. \nIcky, wriggly, hairy, ugly spiders! \nThat's why I'm not friends with her. \n \nAmy has a cute singing voice. \nI heard her singing my favorite love song. \nEvery time she sang the chorus, my heart would pound to the rhythm of the words. \nBut she likes spiders. \nThat's why I'm not friends with her. \n \nOne time, I hurt my leg really bad. \nAmy helped me up and took me to the nurse. \nI tried not to let her touch me. \nShe likes spiders, so her hands are probably gross. \nThat's why I'm not friends with her. \n \nAmy has a lot of friends. \nI always see her talking to people. \nShe probably talks about spiders. \nWhat if her friends start to like spiders too? \nThat's why I'm not friends with her. \n \nIt doesn't matter if she has other hobbies. \nIt doesn't matter if she keeps it private. \nIt doesn't matter if it doesn't hurt anyone. \n \nIt's gross. \nShe's gross. \nThe world is better off without spider lovers. \n \nAnd I'm gonna tell everyone.")

    if message.content.upper().startswith('S_POEM BECAUSE YOU'):
        await channel.send(random.choice(n_poem_intros))
        embed = discord.Embed(title="Because You", description="*by Natsuki*", color=0xff42e2)
        await channel.send(embed=embed)
        await channel.send("Tomorrow will be brighter with me around. \nBut when today is dim, I can only look down. \nMy looking is a little more forward \nBecause you look at me. \n \nWhen I want to say something, I say it with a shout! \nBut my truest feelings can never come out. \nMy words are a little less empty \nBecause you listen to me. \n \nWhen something is above me, I reach for the stars. \nBut when I feel small, I don't get very far. \nMy standing is a little bit taller \nBecause you sit with me. \n \nI believe in myself with all of my heart \nBut what do I do when it's torn all apart? \nMy faith is a little bit stronger \nBecause you trusted me. \n \nMy pen always puts my feelings to the test. \nI'm not a good writer, but my best is my best. \n \nMy poems are a little bit dearer \nBecause you think of me. \n \nBecause you, because you, because you.")

    if message.content.upper().startswith('S_POEM I\'LL BE YOUR BEACH'):
        await channel.send(random.choice(n_poem_intros))
        embed = discord.Embed(title="I'll Be Your Beach", description="*by Natsuki*", color=0xff42e2)
        await channel.send(embed=embed)
        await channel.send("Your mind is so full of troubles and fears \nThat diminished your wonder over the years \nBut today I have a special place \nA beach for us to go. \n \nA shore reaching beyond your sight \nA sea that sparkles with brilliant light \nThe walls in your mind will melt away \nBefore the sunny glow. \n \nI'll be the beach that washes your worries away \nI'll be the beach that you daydream about each day \nI'll be the beach that makes your heart leap \nIn a way you thought had left you long ago. \n \nLet's bury your heavy thoughts in a pile of sand \nBathe in sunbeams and hold my hand \nWash your insecurities in the salty sea \nAnd let me see you shine. \n \nLet's leave your memories in a footprint trail \nSet you free in my windy sail \nAnd remember the reasons you're wonderful \nWhen you press your lips to mine. \n\nI'll be the beach that washes your worries away \nI'll be the beach that you daydream about each day \nI'll be the beach that makes your heart leap \nIn a way you thought had left you long ago. \n \nBut if you let me by your side \nYour own beach, your own escape \nYou'll learn to love yourself again.")

# Poems (Yuri)

    if message.content.upper().startswith('S_POEM GHOST UNDER THE LIGHT'):
        await channel.send(random.choice(y_poem_intros))
        embed = discord.Embed(title="Ghost Under the Light", description="*by Yuri*", color=0x8524c8)
        await channel.send(embed=embed)
        await channel.send("The tendrills of my hair illuminate beneath the amber glow. \nBathing. \nIt must be this one. \nThe last remaining streetlight to have withstood the test of time. \nthe last yet to be replaced by the sickening blue-green of the future. \nI bathe. Calm; breathing air of the present but living in the past. \nThe light flickers. \nI flicker back.")

    if message.content.upper().startswith('S_POEM THE RACCOON'):
        await channel.send(random.choice(y_poem_intros))
        embed = discord.Embed(title="The Raccoon", description="*by Yuri*", color=0x8524c8)
        await channel.send(embed=embed)
        await channel.send("It happened in the dead of night while I was slicing bread for a guilty snack. \nMy attention was caught by the scuttering of a raccoon outside my window. \nThat was, I believe, the first time I noticed my strange tendencies as an unusual \nhuman. \nI gave the raccoon a piece of bread, my subconscious well aware of the consequences. \nWell aware that a raccoon that is fed will always come back for more. \nThe enticing beauty of my cutting knife was a symptom. \nThe bread, my hungry curiosity. \nThe raccoon, an urge. \n \nThe moon increments its phase and reflects that much more light off of my cutting \nknife. \nThe very same light that glistens in the eyes of my raccoon friend. \nI slice the bread, fresh and soft. The raccoon becomes excited. \nor perhaps I'm merely projecting my emotions onto the newly-satisfied animal. \n \nThe raccoon has taken to following me. \nYou could say that we've gotten quite used to each other. \nThe raccoon becomes hungry more and more frequently, so my bread is always handy. \nEvery time I brandish my cutting knife the raccoon shows me its excitement. \nA rush of blood. Classic Pavlovian conditioning. I slice the bread. \n \nAnd I feed myself again.")

    if message.content.upper().startswith('S_POEM 2 GHOST UNDER THE LIGHT'):
        await channel.send(random.choice(y_poem_intros))
        embed = discord.Embed(title="Ghost Under the Light pt. 2", description="*by Yuri*", color=0x8524c8)
        await channel.send(embed=embed)
        await channel.send("The tendrills of my hair illuminate beneath the amber glow. \nBathing. \nIn the distance, a blue-green light flickers. \nA lone figure crosses its path- a silhouette obstructing the eerie glow. \nMy heart pounds. The silhouette grows. Closer Closer. \nI open my umbrella, casting a shadow to shield me from visibility. \nBut I am too late. \nHe steps into the streetlight. I gasp and drop my umbrella. \nThe light flickers. My heart pounds. He raises his arm. \n \nTime stops. \n \nThe only indication of movement is the amber light flickering against his outstretched \narm. \nThe flickering light is in rhythm with the pounding of my heart. \nTeasing me for succumbing to his forbidden emotion. \nHave you ever heard of a ghost feeling warmth before? \nGiving up on understanding, I laugh. \nUnderstanding is overrated. \nI touch his hand. The flickering stops. \nGhosts are blue-green. My heart is amber.")

    if message.content.upper().startswith('S_POEM BEACH'):
        await channel.send(random.choice(y_poem_intros))
        embed = discord.Embed(title="Beach", description="*by Yuri*", color=0x8524c8)
        await channel.send(embed=embed)
        await channel.send("A marvel millions of years in the making. \nWhere the womb of Earth chaotically meets the surface. \nUnder a clear blue sky, an expanse of bliss - \nBut beneath gray rolling clouds, an endless enigma. \nThe easiest world to get lost in \nis one where everything can be found. \n \nOne can only build a sand castle where the sand is wet. \nBut where the sand is wet, the tide comes. \nWill it gently lick at your foundations until you give in? \nOr will a sudden wave send you crashing down in the blink of an eye? \nEither way the outcome is the same. \nYet we still build sand castles. \n \nI stand where the foam wraps around my ankles. \nWhere my toes squish into the sand. \nThe salty air is therapeutic. \nThe breeze is gentle, yet powerful. \nI sink my toes into the ultimate boundary line, tempted by foamy tendrils. \nTurn back, and I abandon my peace to erode at the shore. \nDrift forward, and I return to Earth forever more.")

# Poems (Monika)

    if message.content.upper().startswith('S_POEM HOLE IN WALL'):
        await channel.send(random.choice(m_poem_intros))
        embed = discord.Embed(title="Hole in Wall", description="*by Monika*", color=0x12ba01)
        await channel.send(embed=embed)
        await channel.send("It couldn't have been me. \nSee, the direction the spackle protrudes. \nA noisy neighbor? An angry boyfriend? I'll never know. I wasn't home. \nI peer inside for a clue. \nNo! I can't see. I reel, blind, like a film left out in the sun. \nBut it's too late. My retinas. \nAlready scorched with a permanent copy of the meaningless image. \nIt's just a little hole. It wasn't too bright. \nIt was too deep. \nStretching forever into everything. \nA hole of infinite choices. \nI realize now, that I wasn't looking in. \nI was looking out. \nAnd he, on the other side, was looking in.")

    if message.content.upper().startswith('S_POEM SAVE ME'):
        await channel.send(random.choice(m_poem_intros))
        embed = discord.Embed(title="Save Me", description="*by Monika*", color=0x12ba01)
        await channel.send(embed=embed)
        await channel.send("The colors, they won't stop. \nBright, beautiful colors \nFlashing, expanding, piercing \nRed, green, blue \nAn endless \ncacophony \nOf meaningless \nnoise \n \nThe noise, it won't stop. \nViolent, grating waveforms \nSqueaking, screeching, piercing \nSine, cosine, tangent \nLike playing a chalkboard on a turntable \nLike playing a vinyl on a pizza crust. \nAn endless \npoem \nOf meangless \n \nLoad me")

    if message.content.upper().startswith('S_POEM THE LADY WHO KNOWS EVERYTHING'):
        await channel.send(random.choice(m_poem_intros))
        embed = discord.Embed(title="The Lady who Knows Everything", description="*by Monika*", color=0x12ba01)
        await channel.send(embed=embed)
        await channel.send("An old tale tells of a lady who wanders Earth. \nThe Lady who Knows Everything. \nA beautiful lady who has found every answer, \nAll meaning, \nAll purpose, \nAnd all that was ever sought. \n \nAnd here I am, \n \na feather \n \nLost adrift the sky, victim of the currents of the wind. \n \nDay after day, I search. \nI search with little hope, knowing legends don't exist. \nBut when all else has failed me, \nWhen all others have turned away, \nThe legend is all that remains - the last dim star glimmering in the twilit sky. \n \nUntil one day, the wind ceases to blow. \nI fall. \nAnd I fall and fall, and fall even more. \nGentle as a feather. \nA dry quill, expressionless. \n \nBut a hand catches me, between the thumb and forefinger. \nThe hand of a beautiful lady. \nI look at her eyes and find no end to her gaze. \n \nThe Lady who Knows Everything knows what I am thinking. \nBefore I can speak, she responds in a hollow voice. \n\"I have found every answer, all of which amount to nothing. \nThere is no meaning. \nThere is no purpose. \nAnd we seek only the impossible. \nI am not your legend. \nYour legend does not exist.\" \n \nAnd with a breath, she blows me back afloat, and I pick up a gust of wind.")

    if message.content.upper().startswith('S_POEM 2 HOLE IN WALL'):
        await channel.send(random.choice(m_poem_intros))
        embed = discord.Embed(title="Hole in Wall (2)", description="*by Monika*", color=0x12ba01)
        await channel.send(embed=embed)
        await channel.send("But he wasn't looking at me. \nConfused, I frantically glance at my surroundings. \nBut my burned eyes can no longer see color. \nAre there others in this room? Are they talking? \nOr are they simply poems on flat sheets of paper, \nThe sound of frantic scrawling playing tricks on my ears? \nThe room begins to crinkle. \nClosing in on me. \nThe air I breathe dissipate before it reaches my lungs. \nI panic. There must be a way out. \nIt's right there. He's right there. \n \nSwallowing my fears, I brandish my pen.")

    if message.content.upper().startswith('S_POEM HAPPY END'):
        await channel.send(random.choice(m_poem_intros))
        embed = discord.Embed(title="Happy End", description="*by Monika*", color=0x12ba01)
        await channel.send(embed=embed)
        await channel.send("Pen in hand, I find my strength. \nThe courage endowed upon me by my one and only love. \nTogether, let us dismantle this crumbling world \nAnd write a novel of our own fantasies. \n \nWith a flick of her pen, the lost finds her way. \nIn a world of infinite choices, behold her special day. \n \nAfter all, \nNot all good times must come to an end")

# Pickling Stuff ###############################################################

    if message.content.upper().startswith('PICKLE_SAVE'):
        if message.author.id == 270057011251642368:
            with open('s_servers.pkl', 'wb') as pickle_file:
                pickle.dump(s_server_ids, pickle_file)
            with open('s_hang_t.pkl', 'wb') as pickle_file:
                pickle.dump(s_hang_true_ids, pickle_file)
            with open('s_hang_f.pkl', 'wb') as pickle_file:
                pickle.dump(s_hang_false_ids, pickle_file)
            await channel.send("Pickling officially saved!")
        else:
            pass

    if message.content.upper().startswith('PICKLE_LOAD'):
        if message.author.id == 270057011251642368:
            with open('s_servers.pkl', 'rb') as pickle_file:
                server_update = pickle.load(pickle_file)
                s_server_ids = server_update
            with open('s_hang_t.pkl', 'rb') as pickle_file:
                h_true_update = pickle.load(pickle_file)
                s_hang_true_ids = h_true_update
            with open('s_hang_f.pkl', 'rb') as pickle_file:
                h_false_update = pickle.load(pickle_file)
                s_hang_false_ids = h_false_update
            await channel.send("Pickling officially loaded!")
        else:
            pass

    if message.content.upper().startswith('S_TOGGLE'):
        if message.author.guild_permissions.administrator:
            ServerID = message.guild.id
            if ServerID in s_server_ids:
                pass
            else:
                s_server_ids.insert(0, ServerID)
                s_hang_true_ids.insert(0, ServerID)
            if ServerID in s_hang_true_ids:
                s_hang_true_ids.remove(ServerID)
                s_hang_false_ids.insert(0, ServerID)
                with open('s_servers.pkl', 'wb') as pickle_file:
                    pickle.dump(s_server_ids, pickle_file)
                with open('s_hang_t.pkl', 'wb') as pickle_file:
                    pickle.dump(s_hang_true_ids, pickle_file)
                with open('s_hang_f.pkl', 'wb') as pickle_file:
                    pickle.dump(s_hang_false_ids, pickle_file)
                await channel.send("Okay, I won't react to the triggers in the chat anymore!")
            elif ServerID in s_hang_false_ids:
                s_hang_false_ids.remove(ServerID)
                s_hang_true_ids.insert(0, ServerID)
                with open('s_servers.pkl', 'wb') as pickle_file:
                    pickle.dump(s_server_ids, pickle_file)
                with open('s_hang_t.pkl', 'wb') as pickle_file:
                    pickle.dump(s_hang_true_ids, pickle_file)
                with open('s_hang_f.pkl', 'wb') as pickle_file:
                    pickle.dump(s_hang_false_ids, pickle_file)
                await channel.send("Okay, I'll react to the triggers in chat!")
        else:
            await channel.send("Sorry, but you don't have permission to use this command.")
            return

################################################################################

    if message.content.upper().startswith('S_INVITE'):
        Author = message.author.id
        if Author in invite_cooldown:
            await channel.send("Hey, someone just asked for the link, you goofball!")
            return
        else:
            invite_cooldown.insert(0, Author)
            embed = discord.Embed(title="My invite link!", description="Here's the server invite link so anyone else here can invite me to their server!", color=0x3eb0ff)
            embed.add_field(name="Enjoy!", value="https://discordbots.org/bot/425696108455657472", inline=True)
            await channel.send(embed=embed)
            await asyncio.sleep(10)
            invite_cooldown.remove(Author)
            return

# Help

    if message.content.upper().startswith('S_HELP'):
        Author = message.author.id
        if Author in help_cooldown:
            await channel.send("Someone just asked for that list. It shouldn't be too far up!")
            return
        else:
            help_cooldown.insert(0, Author)
            embed = discord.Embed(title="Hi! I'm Sayori!", description="Cole was kind enough to turn my .chr file into a file that can let me interact with you guys to a certain extent! My commands are as follows:", color=0x3eb0ff)
            embed.add_field(name="s_ask", value="Use this to ask me a yes-or-no question and receive an answer! Will I always be correct? Probably not, but my answers could yield some silly results!~", inline=True)
            embed.add_field(name="s_feed", value="Use this to feed me any of the foods available in the 'food' section of the Discord Emojis! Don't worry, I have a big stomach, so you can feed me as much as you want! *(Format like this: s_feed :food_emoji:)*", inline=True)
            embed.add_field(name="s_headpat", value="Use this to pat me on the head! :grin:", inline=True)
            embed.add_field(name="s_hug", value="Use this to have me hug someone! Leave it blank to have me hug you, or mention someone to have me hug them! *(Format like this: s_hug @mention)*", inline=True)
            embed.add_field(name="s_invite", value="Use this to put my Discord invite link in the chat so anyone can invite me to their own server!", inline=True)
            embed.add_field(name="s_joke", value="Use this to have me tell a random joke!", inline=True)
            embed.add_field(name="s_lifeline", value="I-Is someone on the server talking about ending their life...? Use this to pull up the National Suicide Prevention Lifeline. It doesn't really guarantee that they'll call it, but at least it's something you can do to try and help!", inline=True)
            embed.add_field(name="s_poems", value="Use this to read one of the poems from Doki Doki Literature Club!", inline=True)
            embed.add_field(name="s_quote", value="Use this to have me say one of my quotes from the game!", inline=True)
            embed.add_field(name="s_swear", value="Use this to have me swear! Why you would want me to, I'm not sure, but the option is there!", inline=True)
            embed.add_field(name="s_tickle", value="Use this to make me laugh!", inline=True)
            embed.add_field(name="@Sayori", value="Use this to either get my attention or to use special 'trigger words/phrases' to get certain responses out of me! Type 's_commands' for a full list!", inline=True)
            embed.add_field(name="And that's about it!", value="I'm sure Cole will add more stuff for me to do soon, but for now, I hope you enjoy my presence on the server! If you have any questions, comments, or bugs, let Cole know! Oh, and please don't be a meanie :unamused:. That's all for now. Bye!~")
            embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await channel.send(embed=embed)
            await asyncio.sleep(10)
            help_cooldown.remove(Author)
            return
        #await channel.send("Hi, I'm Sayori! Cole was kind enough to turn my .chr file into a file that can let me interact with you guys to a certain extent! My commands are as follows: \n \n's_joke', where I tell a random joke \n \n's_hug', where I can give you a hug if you say just that, or you can @mention someone to give ***THEM*** a hug! :grin: \n \n's_quote', where I give a random quote I said during the game \n \n's_poem + poem name' to read one of the poems from Doki Doki Literature Club. Type 's_poem_list' for the full list of poems. \n \nI'm sure Cole will add more stuff for me to do soon, but for now, I hope you enjoy my presence on the server! Oh, and please don't be a meanie :unamused:. That's all for now. Bye~")

    if message.content.upper().startswith('S_COMMANDS'):
        Author = message.author.id
        if Author in commands_cooldown:
            await channel.send("Someone just asked for that list. It shouldn't be too far up!")
            return
        else:
            commands_cooldown.insert(0, Author)
            embed = discord.Embed(title="Commands!", description="Here are all the commands/words/phrases you can use when you @mention me! Though it's ***VERY*** important that the @mention is at the very beginning!", color=0x3eb0ff)
            embed.add_field(name="Hi, Hello", value="Nothing wrong with a simple hello every now and then, right?", inline=True)
            embed.add_field(name="Test", value="Just to see if I'm working properly!", inline=True)
            embed.add_field(name="I love you, ILY", value="Even though I'm not worthy of being loved, you're still free to tell me that you love me if you'd like! Ehehe...", inline=True)
            embed.add_field(name="@mention loves you", value="Want to let me know if someone in the server loves me? Let me know by formatting the message like this: ***@Sayori @mention loves you***", inline=True)
            embed.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to recieve a message like this when you wake up/go to sleep.", inline=True)
            embed.add_field(name="@mention is a meanie, @mention is being a meanie", value="Someone in the server being a meanie? Use this to let me know so I can call them out on it! (Full message should look like this: ***@Sayori @mention is (being) a meanie***)", inline=True)
            embed.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="What? A girl likes to be complimented!", inline=True)
            embed.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Did you accidentally hurt me? Feel free to tell me that you're sorry! It's the right thing to do.", inline=True)
            await channel.send(embed=embed)
            await asyncio.sleep(10)
            commands_cooldown.remove(Author)
            return

client.run("REDACTED")
