import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import emoji
import pickle

client = commands.AutoShardedBot(command_prefix="n_")

e = discord.Embed()

dad_words = ["DAD", "PAPA", "FATHER", "DADDY"]
cupcake_words = ["CUPCAKE"]
manga_words = ["MANGA"]

hellos = ["Hi, I guess...", "What, do I have to greet you back or something?", "Hey there, Dummy!"]
hugself_reactions = ["...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
answers = ["Yes.", "No.", "Maybe.", "How should I know, dummy?", "I guess so.", "Pfft. In your dreams!", "Eh. Probably not.", "Is manga literature?", "Yuri might know.", "If Sayori could get her head out of the clouds, she might be able to answer that for you.", "I don't know. Ask Monika if you want the answer that badly."]
laughs = ["H-hey! Cut that out!! Ahahahaha!!", "Hehehehe!!", "Ehehehe!", "STOP IT! STOP! EHEHEHEHE!!!", "I'm gonna break your ribs for this! Hehehe!"]
love_reactions = ["...I love you, too, okay??", "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!", "*urk!* :flushed:", "Shut up! You don't mean that!"]
goodnight_reactions = ["Goodnight, Dummy!", "Goodnight, then.", "You better get good rest or I'll punch you!", "Sleep well, baka!"]
goodmorning_reactions = ["Well, it's *A* morning, I guess...", "Good morning to everyone except my dad.", "Did you get a good night's sleep? Er, not that I really care!!"]
goodafternoon_reactions = ["Good afternoon, I guess.", "Afternoon.", "Yeah, so it's the afternoon. What's your point?"]
cute_reactions = ["***I'M NOT CUTE!!!***", "Hey! I'm not cute!", "Sh-shut up! I'm not cute!!", "Have you ever considered that maybe I want to be something other than cute?!"]
compliment_reactions = ["I... you... ***SHUT UP!!***", "You... really think so...?", "...same to you, I guess...", "I know you're just saying that to be nice, but thanks, anyway.", ":flushed:"]
mentioned_love_reactions = ["W-well, it's not like I love %s back or anything!", "Shut up! %s doesn't love me!", "%s loves me? Yeah, I'll believe that when they tell me that, themselves!"]
cupcake_reactions = ["What did you call me??", "Did someone mention me?", "Yes?"]
dad_reactions = ["W-what?? Is Papa here??", "Hey! Can you not say that word around me, you jerk??"]
apology_reactions = ["Hmph. I'll forgive you, but it's not like you deserve it!", "Fine. I guess I'll let it go...", "You better be sorry, you baka!"]
recipes = ["https://www.foodnetwork.com/recipes/giada-de-laurentiis/smore-brownie-bites-recipe-2125911", "https://www.foodnetwork.com/recipes/rich-nut-cookies-recipe-1913332", "https://www.foodnetwork.com/recipes/sandra-lee/chocolate-caramel-brownies-recipe-1924027", "https://www.foodnetwork.com/recipes/apple-muffins-recipe-1927541", "https://www.foodnetwork.com/recipes/claire-robinson/brown-butter-banana-muffins-recipe-1920734", "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/easy-sticky-buns-recipe-1924654", "https://www.foodnetwork.com/recipes/anne-thornton/nutella-banana-brioche-bread-pudding-recipe-1923849", "https://www.foodnetwork.com/recipes/ina-garten/fresh-peach-cake-recipe-1923148", "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/cookie-pizza-recipe-1924170", "https://www.foodnetwork.com/recipes/melissa-darabian/petite-orange-and-raspberry-pochettes-recipe-1973221", "https://www.foodnetwork.com/recipes/ina-garten/cinnamon-elephant-ears-recipe-1923543", "https://www.foodnetwork.com/recipes/claire-robinson/lemon-pie-cookies-recipe-1923177", "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/honey-cornbread-muffins-recipe-2013336", "https://www.foodnetwork.com/recipes/double-fudge-bread-pudding-with-chocolate-whipped-topping-recipe-1923356", "https://www.foodnetwork.com/recipes/giada-de-laurentiis/double-chocolate-and-mint-cookies-recipe-2010334", "https://www.foodnetwork.com/recipes/sandra-lee/milk-chocolate-cupcakes-with-dark-chocolate-icing-recipe-1923562", "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/zucchini-and-apple-bread-recipe-1924223", "https://www.foodnetwork.com/recipes/food-network-kitchen/vanilla-cupcakes-recipe2-2042539", "https://www.foodnetwork.com/recipes/sunny-anderson/open-faced-plum-tart-recipe2-1973744", "https://www.foodnetwork.com/recipes/marcela-valladolid/polvorones-ground-walnut-cookies-recipe-1960437", "https://www.foodnetwork.com/recipes/anne-thornton/mama-thorntons-peach-pie-recipe-2047258", "https://www.foodnetwork.com/recipes/pumpkin-spice-cupcakes-with-brown-butter-buttercream-recipe-1923349", "https://www.foodnetwork.com/recipes/chocolate-cupcakes-with-ganache-and-marshmallow-frosting-recipe-1923296", "https://www.foodnetwork.com/recipes/melissa-darabian/chocolate-sponge-puddings-recipe-2014543", "https://www.foodnetwork.com/recipes/bubbys-sour-cherry-pie-recipe-2200888"]
recipe_reactions = ["Oh, here's a really good one!", "This one's fun to make!", "Just wash your gross hands, first!", "This one's delicious!"]
motivations = ["I believe in you, you stupid sack of shit!", "C'mon, dummy! You can do it!", "*grabs shoulders* You've got this! I know you do!", "I'll bake you as many cupcakes as you want!", "You better do good or I'll shatter your shins!", "C'mon! Don't be a lazy goofball like Sayori!", "You better not act as dense as MC!", "DO IT! Just DO IT!!!", "Don't let your dreams be dreams!"]
mentioned_motivations = ["Hey, %s! I believe in you, you stupid sack of shit!", "C'mon, %s, you dummy! You can do it!", "*grabs %s's shoulders* You've got this! I know you do!", "Look, %s, I'll bake you as many cupcakes as you want!", "Hey, %s! You better do good or I'll shatter your shins!", "C'mon, %s! Don't be a lazy goofball like Sayori!", "Hey, %s! You better not act as dense as MC!", "DO IT, %s! Just DO IT!!!", "Don't let your dreams be dreams, %s!"]
headpat_reactions = ["Hey! Don't pat me so hard!", "Geez, you're gonna mess up my hair!", "...okay, I guess that kinda felt nice...", "What do I look like, a puppy??", "T-thanks, I guess..."]
manga_reactions = ["...!", "Did someone say manga...?", "***MANGA IS LITERATURE!***", "You like manga, too?? I-I mean, it's not like I like manga or anything...!"]


n_server_ids = []
n_toggle_true = []
n_toggle_false = []

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Type 'n_help' for help!"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Doki Doki Literature Club"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Don't Starve"))
        await asyncio.sleep(300)
        await client.change_presence(activity=discord.Game(name="Cooking Mama"))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    client.emojis()
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("I'm ready when you are, dummy!")

@client.event
async def on_message(message):
    global n_server_ids
    global n_toggle_true
    global n_toggle_false
    channel = message.channel
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in dad_words:
            ServerID = message.guild.id
            if ServerID in n_toggle_false:
                pass
            elif message.author.id == 433834936450023424:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(dad_reactions))
                return
        if word.upper() in cupcake_words:
            ServerID = message.guild.id
            if ServerID in n_toggle_false:
                pass
            elif message.author.id == 433834936450023424:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(cupcake_reactions))
                return
        if word.upper() in manga_words:
            ServerID = message.guild.id
            if ServerID in n_toggle_false:
                pass
            elif message.author.id == 433834936450023424:
                pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(manga_reactions))
                return


    if message.content.upper().startswith('N_HUG'):
        userID = message.author.id
        normal_hugs = ["F-fine, but only because I'll look like a jerk if I don't! *hugs <@%s>*", "I guess a quick hug never hurt anyone... *hugs <@%s>*"]
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(normal_hugs) % (userID))
        else:
            mentioned_hugs = ["F-fine, but only because I'll look like a jerk if I don't! *hugs %s*", "I guess a quick hug never hurt anyone... *hugs %s*"]
            member = message.content.split(" ")[1]
            if member == "Natsuki" or member == "yourself" or member == '<@433834936450023424>':
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(hugself_reactions))
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(mentioned_hugs) % (member))

    if message.content.upper().startswith('N_MOTIVATE'):
        member = message.content.split(" ")[1]
        if ('@everyone' or '@here') in message.content.lower():
            pass
        elif len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(motivations))
        elif member == 'y_act1' or member == 'y_act2':
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Nice try, baka.")
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(mentioned_motivations) % (member))

    if message.content.upper().startswith('N_HEADPAT'):
        if ('@everyone' or '@here') in message.content.lower():
            pass
        else:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(random.choice(headpat_reactions))

    if ('@everyone' or '@here') in message.content.lower() and message.content.upper().startswith("N_"):
        await message.delete()
        await channel.send("Hey! Do you **WANT** everyone to freak out in the chat?! Because I won't let you do that!")
        return

# @Natsuki Responses

    if message.content.upper().startswith('<@433834936450023424>'):
        userID = message.author.id
        if len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Yes?")
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
                await channel.send("I'm working just fine.")
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
            elif "you are cute" in message.content.lower() or "you're cute" in message.content.lower() or "you are so cute" in message.content.lower() or "you're so cute" in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send(random.choice(cute_reactions))
                return
            elif "you are" in message.content.lower() or "you're" in message.content.lower():
                if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "adorable" in message.content.lower():
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
                    await channel.send("S-shut up! No she doesn't!")
                    return
                elif member == '<@436350586670153730>': #Yuri
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("W-Well it's not like I love her back or anything!!")
                elif member == '<@436351740787294208>': #Monika
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Act 2 says otherwise.")
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
                if member == "Monika" or member == "Yuri" or member == "Sayori" or member == "<@425696108455657472>" or member == "<@436350586670153730>":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Pfft! As if!")
                    return
                elif member == "is" or member == "<@433834936450023424>" or member == "you" or member == "you're":
                    await asyncio.sleep(1)
                    await channel.trigger_typing()
                    await asyncio.sleep(1)
                    await channel.send("Ha! Of course I am!")
                    return
                else:
                    pass
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Uh... What?")
                return

    if message.content.upper().startswith('N_QUOTE'):
        quotes = ["MANGA IS LITERATURE!", "I'M NOT CUTE!", "Well, you know what?! I wasn't the one whose boobs magically grew a size bigger as soon as MC started showing up!!", "Whoa, be careful or you might cut yourself on that edge, Yuri. Oh, my bad... You already do, don't you?", "Freaking Monika!", "***fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm***", "You really shouldn't do that kind of thing to girls...unless you really like them...", "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--", "You really need to...beat...the crap out of it!", "If you really just came for the cupcakes, I would be super pissed."]
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(quotes))

    if message.content.upper().startswith('N_ASK'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(answers))

    if message.content.upper().startswith('N_TICKLE'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(laughs))

    if message.content.upper().startswith('N_RECIPE'):
        await asyncio.sleep(1)
        await channel.trigger_typing()
        await asyncio.sleep(1)
        await channel.send(random.choice(recipe_reactions))
        await channel.send(random.choice(recipes))

# Other Bot Interactions

    if '<@433834936450023424>' in message.content.lower():
        if message.author.id == 425696108455657472: #Sayori
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("H-hey! Let me go, Sayori!!")
                return
        elif message.author.id == 436350586670153730: #Yuri
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Geez, Yuri! Don't make it all awkward!")
                return
        elif message.author.id == 436351740787294208: #Monika
            if 'hugs' in message.content.lower():
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Okay, this is just awkward for both of us.")
                return

    if message.author.id == 425696108455657472: #Sayori
        if "awww, she does??" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("S-shut up! No, I don't!")
            return
        else:
            pass
    elif message.author.id == 436350586670153730: #Yuri
        if "oh... i see..." in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("...great, now I look like the bad guy!")
            return
        elif "sh-she does?" in message.content.lower():
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("Urk! N-No! Not like that!!")
            return
        elif "pfft. as if. that immature brat doesn't love anyone but herself." in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send("What the hell?? Yuri, why would you say something so mean??")
            return
        elif "because it's the fucking truth, you little bitch!!" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send(":rage: :rage: :rage:")
            return
        elif "get your fucking hands off of me!!" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(2)
            await channel.send(":angry:")
            return
        elif "no shocker there, you selfish bitch!" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send(":angry:")
            return
        else:
            pass
    elif message.author.id == 436351740787294208: #Monika
        if "oh, really? she, of all people, said that?" in message.content.lower():
            await asyncio.sleep(2)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("***NO!!!*** I never said that!!")
            return

# Feed Natsuki

    if message.content.upper().startswith('N_FEED'):
        if len(message.content.split(" ")) == 1:
            await asyncio.sleep(1)
            await channel.trigger_typing()
            await asyncio.sleep(1)
            await channel.send("H-hey! Don't feel like you have to feed me anything! I'm okay!")
        else:
            member = message.content.split(" ")[1]
            # Cookie
            if member == u"\U0001F36A":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I suppose a cookie couldn't hurt.")
            # Pizza
            elif member == u"\U0001F355":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("F-fine, I'll have a slice.")
            # Burger
            elif member == u"\U0001F354":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("...only because there's cheese on it...")
            # Cold Foods
            elif member == u"\U0001F367" or member == u"\U0001F366" or member == u"\U0001F368":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Thanks, I guess. I was actually feeling a bit warm.")
            # Japanese Foods
            elif member == u"\U0001F363" or member == u"\U0001F371" or member == u"\U0001F35B" or member == u"\U0001F359" or member == u"\U0001F35A" or member == u"\U0001F358" or member == u"\U0001F35C" or member == u"\U0001F362" or member == u"\U0001F361" or member == u"\U0001F365":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Ah, this is a more familiar meal.")
            # Alcohol
            elif member == u"\U0001F37A" or member == u"\U0001F37B" or member == u"\U0001F377" or member == u"\U0001F378" or member == u"\U0001F379" or member == u"\U0001F37E" or member == u"\U0001F376" or member == u"\U0001F942" or member == u"\U0001F943":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Hey, what's the idea?? You trying to get me drunk??")
            # Coffee
            elif member == u"\u2615":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I don't really like coffee that much, but thanks, anyway.")
            # Tea
            elif member == u"\U0001F375":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("*sips* Just the right temperature. I guess you're not inconsiderate, after all!")
            # Bread
            elif member == u"\U0001F35E" or member == u"\U0001F956":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Well, it's more than Papa gives me...")
            # Hot Pepper
            elif member == u"\U0001F336":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("H-Hey!! My freaking mouth is on fire!!!")
            # Cooking
            elif member == u"\U0001F373":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Sunny-side up? How did you know that's how I liked them?")
            # Mexican Food
            elif member == u"\U0001F32E" or member == u"\U0001F32F":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Mexican, huh? Not my first choice, but it's still pretty good...")
            # Sweets
            elif member == u"\U0001F370" or member == u"\U0001F36E" or member == u"\U0001F36C" or member == u"\U0001F36B" or member == u"\U0001F369":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Well, I suppose it would be nice to eat a sweet that I didn't bake, for once.")
            # Popcorn
            elif member == u"\U0001F37F":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("*crunch crunch crunch*")
            # Baby Bottle
            elif member == u"\U0001F37C" or member == u"\U0001F36D":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I feel like there's a loli joke to be made here...")
            # Egg
            elif member == u"\U0001F95A":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I'm not so hungry that I'll eat a raw egg! Er, I mean I'm not hungry!")
            # Silverware
            elif member == u"\U0001F374" or member == u"\U0001F37D" or member == u"\U0001F944":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("I'd prefer actual food here, please! N-not that you have to give me any or anything...")
            # Milk
            elif member == u"\U0001F95B":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("What, you didn't have strawberry milk?? Ah, whatever. I guess this is fine...")
            # Birthday Cake
            elif member == u"\U0001F382":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Huh? It's not my birthday!")
            # Misc.
            elif member == u"\U0001F34E" or member == u"\U0001F34F" or member == u"\U0001F350" or member == u"\U0001F34A" or member == u"\U0001F34B" or member == u"\U0001F34C" or member == u"\U0001F349" or member == u"\U0001F347" or member == u"\U0001F353" or member == u"\U0001F348" or member == u"\U0001F352" or member == u"\U0001F351" or member == u"\U0001F34D" or member == u"\U0001F345" or member == u"\U0001F346" or member == u"\U0001F33D" or member == u"\U0001F360" or member == u"\U0001F36F" or member == u"\U0001F357" or member == u"\U0001F356" or member == u"\U0001F364" or member == u"\U0001F35F" or member == u"\U0001F32D" or member == u"\U0001F35D" or member == u"\U0001F950" or member == u"\U0001F951" or member == u"\U0001F952" or member == u"\U0001F953" or member == u"\U0001F954" or member == u"\U0001F955" or member == u"\U0001F957" or member == u"\U0001F958" or member == u"\U0001F959" or member == u"\U0001F95C" or member == u"\U0001F95D" or member == u"\U0001F95E" or member == u"\U0001F9C0":
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("...t-thank you. *slowly eats*")
            # Not Food
            else:
                await asyncio.sleep(1)
                await channel.trigger_typing()
                await asyncio.sleep(1)
                await channel.send("Are you trying to kill me?? That's not food!")

    if message.content.upper().startswith('N_INVITE'):
        embed = discord.Embed(title="My invite link!", description="F-fine! I guess I can join someone else's server, too... but I probably won't like it!", color=0xff42e2)
        embed.add_field(name="Here goes...", value="https://discordbots.org/bot/433834936450023424", inline=True)
        await channel.send(embed=embed)

# Pickling Stuff ###############################################################

    if message.content.upper().startswith('PICKLE_SAVE'):
        if message.author.id == 270057011251642368:
            with open('n_servers.pkl', 'wb') as pickle_file:
                pickle.dump(n_server_ids, pickle_file)
            with open('n_true.pkl', 'wb') as pickle_file:
                pickle.dump(n_toggle_true, pickle_file)
            with open('n_false.pkl', 'wb') as pickle_file:
                pickle.dump(n_toggle_false, pickle_file)
            await channel.send("Pickling officially saved!")
        else:
            pass

    if message.content.upper().startswith('PICKLE_LOAD'):
        if message.author.id == 270057011251642368:
            with open('n_servers.pkl', 'rb') as pickle_file:
                server_update = pickle.load(pickle_file)
                n_server_ids = server_update
            with open('n_true.pkl', 'rb') as pickle_file:
                toggle_true_update = pickle.load(pickle_file)
                n_toggle_true = toggle_true_update
            with open('n_false.pkl', 'rb') as pickle_file:
                toggle_false_update = pickle.load(pickle_file)
                n_toggle_false = toggle_false_update
            await channel.send("Pickling officially loaded!")
        else:
            pass

    if message.content.upper().startswith('N_TOGGLE'):
        if message.author.guild_permissions.administrator:
            ServerID = message.guild.id
            if ServerID in n_server_ids:
                pass
            else:
                n_server_ids.insert(0, ServerID)
                n_toggle_true.insert(0, ServerID)
            if ServerID in n_toggle_true:
                n_toggle_true.remove(ServerID)
                n_toggle_false.insert(0, ServerID)
                await channel.send("Fine, I won't react to chat triggers.")
            elif ServerID in n_toggle_false:
                n_toggle_false.remove(ServerID)
                n_toggle_true.insert(0, ServerID)
                await channel.send("Fine, I'll react to chat triggers.")
        else:
            await channel.send("Whoa there, Dummy! Only an admin can use that command!")

################################################################################

# Help

    if message.content.upper().startswith('N_HELP'):
        embed = discord.Embed(title="Hey, it's me, Natsuki.", description="Freaking Cole decided to turn my .chr file into a file that lets me be on this Discord server. It's not like I'm here because I want to be or anything, you dummies! A-anyway, here are the things I can do:", color=0xff42e2)
        embed.add_field(name="n_ask", value="You can ask me any yes-or-no question with this. But don't get mad if I don't know the answer or if I give the wrong answer!", inline=True)
        embed.add_field(name="n_feed", value="Y-you don't have to or anything, but I guess you could feed me some food i-if you really wanted to... *(Format like this: 'n_feed :food_emoji:')*", inline=True)
        embed.add_field(name="n_headpat", value="You can use this to pat me on the head, but why any normal person would want to, I have no clue...", inline=True)
        embed.add_field(name="n_hug", value="Ugh. Hugs are gross, but if you want me to hug you or anyone on the server, I guess I can do that for you... Just leave it blank if you want me to hug you or @mention someone to have me hug them. *(Format like this: n_hug @mention)*", inline=True)
        embed.add_field(name="n_invite", value="You can use this to show the link to invite me to other servers. But don't think that I'll enjoy it, you dummy!", inline=True)
        embed.add_field(name="n_motivate", value="I-it's not like I want to, but if you need motivation or encouragement, I'll try to help you out, I guess.", inline=True)
        embed.add_field(name="n_quote", value="You can use this to make me say one of my quotes from the game.", inline=True)
        embed.add_field(name="n_recipe", value="Do you like baking, like me? Well, I've got a few recipes in my cookbook; feel free to check them out!", inline=True)
        embed.add_field(name="n_tickle", value="You can use this to... TICKLE ME?? Oh, don't you dare use that unless you want a trip to the hospital!", inline=True)
        embed.add_field(name="@Natsuki", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say!", inline=True)
        embed.add_field(name="I guess that's it...", value="Cole will make me do more stuff soon, but I'm not looking forward to it! If you want, you can go visit his Support Server and give him a piece of my mind! Anyway, see you later, ~~bakas~~ everyone!", inline=True)
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await channel.send(embed=embed)

client.run("REDACTED")
