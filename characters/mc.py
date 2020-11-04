import random, re, rstr

class mc():

    def __init__(self):
        self.color = "0xdb7915"
        self.description = "MC is the main character in the game Doki Doki Literature Club, he is the newest member of the Literature Club and along with his club members he spends his time after school in the club and is the neighbor of Sayori"
        self.id = 606721454297448448
        self.token = "NjA2NzIxNDU0Mjk3NDQ4NDQ4.XqMmVQ.5n--3UKFFynYT1s7vnVd87L0_Lg"
        self.prefix = "(M(C|c)|mc)_"
        self.rename = True
        self.help = {
            "commands": {
                "ask [question]": "Ask MC anything you want to ask.",
                "changelog": "See the latest changes. (alias: log)",
                "confess [person]": "Let MC confess his love.",
                "debug": "View MC's statistics.",
                "feed [emote]": "Give MC food. (alias: eat)",
                "headpat": "Headpat MC. (alias: pat)",
                "help [about]": "Help about MC. (alias: manual)",
                "hug [person]": "Let MC hug someone.",
                "invite": "Invite MC to your server.",
                "ping": "Get MC's heartbeat. (alias: doki)",
                "poems [poem name]": "Get MC's poems from the game. (alias: poem)",
                "quotes": "Get MC's quotes from the game. (alias: quote)",
                "rename [name]": "rename MC (requires perms to edit nicknames).",
                "shard": "Check which shard are you on for MC.",
                "tamper": "Mess up or fix MC's personality.",
                "tickle": "Tickle MC.",
                "trigger": "Set triggers for MC on/off. (alias: triggers)"
            },
            "phrases": {
                "Hello": "Say hello to MC.",
                "Love": "Tell MC you or someone else loves him",
                "Good Morning": "Greet MC with a good morning.",
                "Good Night": "Greet MC with a good night.",
                "Good Afternoon": "Greet MC with a good afternoon.",
                "Compliment": "Give MC a compliment.",
                "Apologize": "Apologize to MC.",
                "Sick": "Tell MC when you are sick.",
                "Best Girl": "Tell MC who's the best girl."
            },
            "triggers": ["rope", "poetry"]
        }

    def playing(self):
        return [
            "Type 'mc_help' for help!",
            "Doki Doki Literature Club",
            "with a shoe lace",
            "aloof",
            "in a dark void"
        ]

    def ask(self, tamper=False, nothing=False):
        if not tamper:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"Ye[hs], I (guess|think)[\.;]( I don't care either way\.)?"),
                    "I don't know why you're asking me, go ask Sayori.",
                    "Maybe? Monika would know.",
                    "Yuri can help you.",
                    "What about asking Natsuki?",
                    rstr.xeger(r"(Yeh|Nah)\."),
                    "No, just no."
                ])
            else:
                return "I can't answer a non-existent question."
        else:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"Ye[hs], I (guess|think)[\.;]( I don't care either way\.)?"),
                    "I don't know why you're asking me, go ask Sayori.",
                    "Maybe? Monika would know.",
                    "Yuri can help you.",
                    "What about asking Natsuki?",
                    rstr.xeger(r"(Yeh|Nah)\."),
                    "No, just no."
                ])
            else:
                return "I can't answer a non-existent question."
        return

    def confess(self, target="", targetName=""):
        if target == "monika":
            return f"{targetName}"
        elif target == "sayori":
            return f"{targetName}"
        elif target == "yuri":
            return f"I-I love you, Yuri."
        elif target == "natsuki":
            return f"H-Hey, Natsuki?"
        else:
            return f"*starts to blush* Ok, I'll admit it {targetName}, I love you!"

    def everyone(self):
        return "Did you try to make me ping everyone? Well, uhh... Nice try, I suppose."

    def feed(self, tamper=False, food=[], user=""):
        if not tamper:
            if not food:
                return "It's fine, I brought my own food..."
            elif "cookie" in food:
                return "I mean, it's not made by Natsuki but I'll eat it."
            elif "cupcake" in food:
                return "*munch munch* It's tasty but, it's not that full of favor comparing to Natsuki's cupcakes."
            elif "japanese" in food:
                return "I mean, it's from my homeland. *eats happily*"
            elif "takeout" in food:
                return "Ah, I love having one of those boxes, while I'm watching anime."
            elif "pizza" in food:
                return "Yay, pizza!"
            elif "burger" in food:
                return "Yay, I love hamburgers!"
            elif "falafel" in food:
                return "No thanks, I'm not really a fan of whatever that is."
            elif "ice" in food:
                return "What am I supposed to do with this Ice? Because I'm pretty sure you're not trying to feed me that."
            elif "cold" in food:
                return "Burr, cold."
            elif "cold_drink" in food:
                return "A cold drink is the answer to most of my problems."
            elif "canned" in food:
                return "Thanks I guess... ~~I hope it contains beans though.~~"
            elif "alcohol" in food:
                return "What the fuck? I'm not drinking alcohol!"
            elif "coffee" in food:
                return "Time to start the day..."
            elif "tea" in food:
                return "Time to start the day..."
            elif "bread" in food:
                return "Thanks, though I would've preferred a sandwich, a slice of bread is also fine."
            elif "sandwich" in food:
                return "As I always say \"Enjoy every sandwich\"."
            elif "waffle" in food:
                return "Why are you giving me this? Waffles are just pancakes with abs."
            elif "croissant" in food:
                return "Wow thanks, do you have any butter to go with this?"
            elif "pastries" in food:
                return "Ah, pastries my old friend"
            elif "butter" in food:
                return "Butter?? Why though?"
            elif "pepper" in food:
                return "***HOTHOTHOTHOTHOT!!!***"
            elif "cooking" in food:
                return "Ugh, breakfast foods, great."
            elif "mexican" in food:
                return "Noche de taco maravilloso!"
            elif "sweets" in food:
                return f"Something sweet? For me? Thanks, {user}."
            elif "nuts" in food:
                return "I love nuts. I eat them almost all the time, they're easy too carry around, and I am never hungry all the time, but most importantly they remind me of Sayori."
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "I'm-I'm not a baby..."
            elif "egg" in food:
                return "Ugh, breakfast foods, great..."
            elif "salt" in food:
                return "If you're trying to be funny, I can guarantee you that giving people salt is not funny at all."
            elif "silverware" in food:
                return "Well, what are we eating?"
            elif "bowl" in food:
                return "It's not like I wanted you to give me this empty bowl."
            elif "milk" in food:
                return "Ah, a nice, cold glass of milk is always welcoming!"
            elif "birthday_not" in food:
                return f"It's not my birthday, and even if it was, I don't want a cake {user}."
            elif "birthday" in food:
                return random.choices([
                    "I didn't want any cake, but I don't want Monika to be mad at me, so... ~~No one knows what she might do, when she's mad~~",
                    "I guess I'm fine with having Natsuki's cake."
                ])
            elif "knife" in food:
                return "I'm not Act 2 Yuri; feed that to her."
            elif "misc" in food:
                return "Um, thanks? *eats the food*"
            else:
                return "I don't think I can eat that."
            
        else:
            
            if not food:
                return "It's fine, I brought my own food..."
            elif "cookie" in food:
                return "I mean, it's not made by Natsuki but I'll eat it."
            elif "cupcake" in food:
                return "*munch munch* It's tasty but, it's not that full of favor comparing to Natsuki's cupcakes."
            elif "japanese" in food:
                return "I mean, it's from my homeland. *eats happily*"
            elif "takeout" in food:
                return "Ah, I love having one of those boxes, while I'm watching anime."
            elif "pizza" in food:
                return "Yay, pizza!"
            elif "burger" in food:
                return "Yay, I love hamburgers!"
            elif "falafel" in food:
                return "No thanks, I'm not really a fan of whatever that is."
            elif "ice" in food:
                return "What am I supposed to do with this Ice? Because I'm pretty sure you're not trying to feed me that."
            elif "cold" in food:
                return "Burr, cold."
            elif "cold_drink" in food:
                return "A cold drink is the answer to most of my problems."
            elif "canned" in food:
                return "Thanks I guess... ~~I hope it contains beans though.~~"
            elif "alcohol" in food:
                return "What the fuck? I'm not drinking alcohol!"
            elif "coffee" in food:
                return "Time to start the day..."
            elif "tea" in food:
                return "Time to start the day..."
            elif "bread" in food:
                return "Thanks, though I would've preferred a sandwich, a slice of bread is also fine."
            elif "sandwich" in food:
                return "As I always say \"Enjoy every sandwich\"."
            elif "waffle" in food:
                return "Why are you giving me this? Waffles are just pancakes with abs."
            elif "croissant" in food:
                return "Wow thanks, do you have any butter to go with this?"
            elif "pastries" in food:
                return "Ah, pastries my old friend"
            elif "butter" in food:
                return "Butter?? Why though?"
            elif "pepper" in food:
                return "***HOTHOTHOTHOTHOT!!!***"
            elif "cooking" in food:
                return "Ugh, breakfast foods, great."
            elif "mexican" in food:
                return "Noche de taco maravilloso!"
            elif "sweets" in food:
                return f"Something sweet? For me? Thanks, {user}."
            elif "nuts" in food:
                return "I love nuts. I eat them almost all the time, they're easy too carry around, and I am never hungry all the time, but most importantly they remind me of Sayori."
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "I'm-I'm not a baby..."
            elif "egg" in food:
                return "Ugh, breakfast foods, great..."
            elif "salt" in food:
                return "If you're trying to be funny, I can guarantee you that giving people salt is not funny at all."
            elif "silverware" in food:
                return "Well, what are we eating?"
            elif "bowl" in food:
                return "It's not like I wanted you to give me this empty bowl."
            elif "milk" in food:
                return "Ah, a nice, cold glass of milk is always welcoming!"
            elif "birthday_not" in food:
                return f"It's not my birthday, and even if it was, I don't want a cake {user}."
            elif "birthday" in food:
                return random.choices([
                    "I didn't want any cake, but I don't want Monika to be mad at me, so... ~~No one knows what she might do, when she's mad~~",
                    "I guess I'm fine with having Natsuki's cake."
                ])
            elif "knife" in food:
                return "I'm not Act 2 Yuri; feed that to her."
            elif "misc" in food:
                return "Um, thanks? *eats the food*"
            else:
                return "I don't think I can eat that."

        return

    def headpat(self, tamper=False):
        if not tamper:
            return random.choice([
                "Stop it!"
            ])
        else:
            return random.choice([
                "Stop it!"
            ])
        return 

    def hug(self, tamper=False, target="", targetName=""):
        if not tamper:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"Uh, ok? *hugs {targetName}*",
                    f"I don't do hugs.",
                    f"I mean, if you want. *hugs {targetName}*",
                    f"If it makes you happy, then fine. *hugs {targetName}*",
                    "No thanks, I'm fine.",
                    "*runs away*"
                ])
            elif target == "self":
                return random.choice([
                    "...fine. *hugs myself*",
                    "Well, if you say so... *hugs myself*",
                    "*hugs myself* Huh. Now I see why you guys like my hugs so much."
                ])
        else:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"Uh, ok? *hugs {targetName}*",
                    f"I don't do hugs.",
                    f"I mean, if you want. *hugs {targetName}*",
                    f"If it makes you happy, then fine. *hugs {targetName}*",
                    "No thanks, I'm fine.",
                    "*runs away*"
                ])
            elif target == "self":
                return random.choice([
                    "...fine. *hugs myself*",
                    "Well, if you say so... *hugs myself*",
                    "*hugs myself* Huh. Now I see why you guys like my hugs so much."
                ])
        return

    def interactions(self, tamper=False, bot=None, message=None):
        content = message.content.lower()
        monika = next( (c for c in bot.chrs if c["name"].lower() == "monika"), None)
        monikaID = monika["character"].id
        sayori = next( (c for c in bot.chrs if c["name"].lower() == "sayori"), None)
        sayoriID = sayori["character"].id
        yuri = next( (c for c in bot.chrs if c["name"].lower() == "yuri"), None)
        yuriID = yuri["character"].id
        natsuki = next( (c for c in bot.chrs if c["name"].lower() == "natsuki"), None)
        natsukiID = natsuki["character"].id
        mc = next( (c for c in bot.chrs if c["name"].lower() == "mc"), None)
        mcID = mc["character"].id
        if not tamper:
            if message.author.id == monikaID:
                if f"aww, you're the best hugger, <@{bot.user.id}>" in content.lower():
                    return "No I'm not..."
                if len(message.embeds) > 0 and "os.remove" in message.embeds[0].title:
                    return "Not this shit again, Monika."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "*muffled screaming*"
                if f"yes, <@{bot.user.id}>?" in content.lower():
                    return "I need to tell you something."
                if "hmm?" in content.lower():
                    return "I love you, Monika."
                if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in content.lower():
                    return "~~Of course you won't let anyone take me from you. You'll just delete them if they try.~~"
            elif message.author.id == sayoriID:
                if f"aww you're such a sweetheart, <@{bot.user.id}>" in content.lower():
                    return "You will always be my closest friend, Sayori."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Finnnnnnne, Sayori."
                if f"yes, <@{bot.user.id}>?" in content.lower():
                    return "I-I love you, Sayori."
                if "i-i do too! *hugs mc*" in content.lower():
                    return "*hugs back*"
                if "yay! my best friend loves me!!!" in content.lower():
                    return "Uhhhhhhh..."
            elif message.author.id == yuriID:
                if "augh!" in content.lower():
                    return "Sorry..."
                if f"hey <@{bot.user.id}>, get your sexy body over here and fuck me~" in content.lower():
                    return "Fuck no, get away from me, Yuri."
                if "then i'll stab you and crawl in your skin." in content.lower():
                    return "Yeah, fuck no."
                if f"that's right <@{bot.user.id}>, let me feel your pulsating cock on my pussy." in content.lower():
                    return "Oh hell no..."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "No, it's fine..."
                if "*tackle hugs mc*" in content.lower():
                    return "*hugs back*"
                if f"i love you too, you sexy <@{bot.user.id}>! now fuck me!!!" in content.lower():
                    return "Oh hell no!"
                if "of course he loves me! and I will make sure **nobody** takes him away from me!" in content.lower():
                    return "You're going to stab them to death if they try, aren't you?"
            elif message.author.id == natsukiID:
                if f"ah! you scared me, <@{bot.user.id}>" in content.lower():
                    return "Sorry, I'm a dumbass."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Augh!"
                if "what do you want, dummy?" in content.lower():
                    return "I-I love you, Natsuki..."
                if "well, i-i do too..." in content.lower():
                    return "*hugs Natsuki*"
                if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in content.lower():
                    return "I'm not surprised she would say that, given how much of a tsundere she is."
            elif message.author.id == mcID:
                if "yeah, fuck no." in content.lower():
                    return "y_tamper"
        else:
            if message.author.id == monikaID:
                if f"aww, you're the best hugger, <@{bot.user.id}>" in content.lower():
                    return "No I'm not..."
                if len(message.embeds) > 0 and "os.remove" in message.embeds[0].title:
                    return "Not this shit again, Monika."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "*muffled screaming*"
                if f"yes, <@{bot.user.id}>?" in content.lower():
                    return "I need to tell you something."
                if "hmm?" in content.lower():
                    return "I love you, Monika."
                if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in content.lower():
                    return "~~Of course you won't let anyone take me from you. You'll just delete them if they try.~~"
            elif message.author.id == sayoriID:
                if f"aww you're such a sweetheart, <@{bot.user.id}>" in content.lower():
                    return "You will always be my closest friend, Sayori."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Finnnnnnne, Sayori."
                if f"yes, <@{bot.user.id}>?" in content.lower():
                    return "I-I love you, Sayori."
                if "i-i do too! *hugs mc*" in content.lower():
                    return "*hugs back*"
                if "yay! my best friend loves me!!!" in content.lower():
                    return "Uhhhhhhh..."
            elif message.author.id == yuriID:
                if "augh!" in content.lower():
                    return "Sorry..."
                if f"hey <@{bot.user.id}>, get your sexy body over here and fuck me~" in content.lower():
                    return "Fuck no, get away from me, Yuri."
                if "then i'll stab you and crawl in your skin." in content.lower():
                    return "Yeah, fuck no."
                if f"that's right <@{bot.user.id}>, let me feel your pulsating cock on my pussy." in content.lower():
                    return "Oh hell no..."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "No, it's fine..."
                if "*tackle hugs mc*" in content.lower():
                    return "*hugs back*"
                if f"i love you too, you sexy <@{bot.user.id}>! now fuck me!!!" in content.lower():
                    return "Oh hell no!"
                if "of course he loves me! and I will make sure **nobody** takes him away from me!" in content.lower():
                    return "You're going to stab them to death if they try, aren't you?"
            elif message.author.id == natsukiID:
                if f"ah! you scared me, <@{bot.user.id}>" in content.lower():
                    return "Sorry, I'm a dumbass."
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Augh!"
                if "what do you want, dummy?" in content.lower():
                    return "I-I love you, Natsuki..."
                if "well, i-i do too..." in content.lower():
                    return "*hugs Natsuki*"
                if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in content.lower():
                    return "I'm not surprised she would say that, given how much of a tsundere she is."
            elif message.author.id == mcID:
                if "Yeah, fuck no." in content.lower():
                    return "y_tamper"

    def poems(self, tamper=False, name=""):
        if not tamper:
            sayori_words = [
                "Adventure",
                "Alone",
                "Amazing",
                "Awesome",
                "Beauty",
                "Bed",
                "Bliss",
                "Broken",
                "Calm",
                "Charm",
                "Cheer",
                "Childhood",
                "Clumsy",
                "Color",
                "Comfort",
                "Cry",
                "Dance",
                "Dark",
                "Daydream",
                "Dazzle",
                "Death",
                "Defeat",
                "Depression",
                "Embrace",
                "Empty",
                "Excitement",
                "Extraordinary",
                "Family",
                "Fear",
                "Feather",
                "Fireflies",
                "Fireworks",
                "Flower",
                "Flying",
                "Forgive",
                "Friends",
                "Fun",
                "Grief",
                "Happiness",
                "Heart",
                "Holiday",
                "Hope",
                "Hopeless",
                "Hurt",
                "Joy",
                "Laugh",
                "Lazy",
                "Loud",
                "Love",
                "Lucky",
                "Marriage",
                "Memories",
                "Misery",
                "Misfortune",
                "Music",
                "Nature",
                "Ocean",
                "Pain",
                "Party",
                "Peaceful",
                "Prayer",
                "Passion",
                "Play",
                "Precious",
                "Promise",
                "Rainbow",
                "Raincloud",
                "Romance",
                "Rose",
                "Sadness",
                "Scars",
                "Shame",
                "Silly",
                "Sing",
                "Smile",
                "Sparkle",
                "Special",
                "Sunny",
                "Sunset",
                "Sweet",
                "Tears",
                "Together",
                "Tragedy",
                "Treasure",
                "Unrequited",
                "Vacation",
                "Warm",
                "Wonderful"
            ]
            yuri_words = [
                "Afterimage",
                "Agonizing",
                "Ambient",
                "Analysis",
                "Anxiety",
                "Atone",
                "Aura",
                "Breathe",
                "Cage",
                "Captive",
                "Climax",
                "Contamination",
                "Covet",
                "Crimson",
                "Desire",
                "Despise",
                "Destiny",
                "Determination",
                "Disaster",
                "Disarray",
                "Disoriented",
                "Disown",
                "Dream",
                "Effulgent",
                "Electricity",
                "Entropy",
                "Essence",
                "Eternity",
                "Existence",
                "Explode",
                "Extreme",
                "Fester",
                "Fickle",
                "Flee",
                "Frightening",
                "Graveyard",
                "Heavensent",
                "Horror",
                "Imagination",
                "Incapable",
                "Incongruent",
                "Infallible",
                "Inferno",
                "Infinite",
                "Intellectual",
                "Insight",
                "Journey",
                "Judgement",
                "Landscape",
                "Lust",
                "Massacre",
                "Meager",
                "Melancholy",
                "Philosophy",
                "Pleasure",
                "Portrait",
                "Question",
                "Raindrops",
                "Secretive",
                "Sensation",
                "Starscape",
                "Suicide",
                "Tenacious",
                "Time",
                "Uncanny",
                "Uncontrollable",
                "Unending",
                "Universe",
                "Unrestrained",
                "Unstable",
                "Variance",
                "Vertigo",
                "Vibrant",
                "Vitality",
                "Vivacious",
                "Vivid",
                "Whirlwind",
                "Wrath"
            ]
            natsuki_words = [
                "Anger",
                "Anime",
                "Blanket",
                "Boop",
                "Bouncy",
                "Bubbles",
                "Bunny",
                "Candy",
                "Cheeks",
                "Chocolate",
                "Clouds",
                "Cute",
                "Doki-Doki",
                "Email",
                "Fantasy",
                "Fluffy",
                "Games",
                "Giggle",
                "Hair",
                "Headphones",
                "Heartbeat",
                "Hop",
                "Jump",
                "Jumpy",
                "Kawaii",
                "Kiss",
                "Kitty",
                "Lipstick",
                "Lollipop",
                "Marshmallow",
                "Melody",
                "Milk",
                "Mouse",
                "Nibble",
                "Nightgown",
                "Papa",
                "Parfait",
                "Peace",
                "Pink",
                "Playground",
                "Poof",
                "Pout",
                "Puppy",
                "Pure",
                "Ribbon",
                "Shiny",
                "Shopping",
                "Skipping",
                "Skirt",
                "Socks",
                "Spinning",
                "Sticky",
                "Strawberry",
                "Sugar",
                "Summer",
                "Swimsuit",
                "Twirl",
                "Valentine",
                "Vanilla",
                "Waterfall",
                "Whisper",
                "Whistle"
            ]
            chance = random.randint(1, 4)
            if chance == 1:
                return ["", " ".join(random.choices(sayori_words, k=20))]
            elif chance == 2:
                return ["", " ".join(random.choices(yuri_words, k=20))]
            elif chance == 3:
                return ["", " ".join(random.choices(natsuki_words, k=20))]
            elif chance == 4:
                return ["", " ".join(random.choices(sayori_words + yuri_words + natsuki_words, k=20))]
        else:
            nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
            monika_words = "(M|m)(O|o)(N|n)(I|i)(K|k)(A|a)"
            yuri_words = [
                "Afterimage",
                "Agonizing",
                "Alone",
                "Ambient",
                "Analysis",
                "Anxiety",
                "Atone",
                "Aura",
                "Breathe",
                "Broken",
                "Cage",
                "Calm",
                "Captive",
                "Climax",
                "Contamination",
                "Covet",
                "Crimson",
                "Cry",
                "Dark",
                "Daydream",
                "Death",
                "Defeat",
                "Depression",
                "Desire",
                "Despise",
                "Destiny",
                "Determination",
                "Disaster",
                "Disarray",
                "Disoriented",
                "Disown",
                "Dream",
                "Effulgent",
                "Electricity",
                "Embrace",
                "Empty",
                "Entropy",
                "Essence",
                "Eternity",
                "Existence",
                "Explode",
                "Extreme",
                "Fear",
                "Fester",
                "Fickle",
                "Flee",
                "Forgive",
                "Frightening",
                "Graveyard",
                "Grief",
                "Heavensent",
                "Hope",
                "Hopeless",
                "Horror",
                "Hurt",
                "Imagination",
                "Incapable",
                "Incongruent",
                "Infallible",
                "Inferno",
                "Infinite",
                "Intellectual",
                "Insight",
                "Journey",
                "Joy",
                "Judgement",
                "Landscape",
                "Lust",
                "Massacre",
                "Meager",
                "Melancholy",
                "Misery",
                "Misfortune",
                "Pain",
                "Peaceful",
                "Philosophy",
                "Pleasure",
                "Portrait",
                "Prayer",
                "Question",
                "Raindrops",
                "Rose",
                "Scars",
                "Secretive",
                "Sensation",
                "Shame",
                "Starscape",
                "Suicide",
                "Tears",
                "Tenacious",
                "Time",
                "Tragedy",
                "Uncanny",
                "Uncontrollable",
                "Unending",
                "Universe",
                "Unrequited",
                "Unrestrained",
                "Unstable",
                "Variance",
                "Vertigo",
                "Vibrant",
                "Vitality",
                "Vivacious",
                "Vivid",
                "Whirlwind",
                "Wrath"
            ]
            natsuki_words = [
                "Adventure",
                "Amazing",
                "Anger",
                "Anime",
                "Awesome",
                "Beauty",
                "Bed",
                "Blanket",
                "Bliss",
                "Boop",
                "Bouncy",
                "Bubbles",
                "Bunny",
                "Candy",
                "Charm",
                "Cheeks",
                "Cheer",
                "Childhood",
                "Chocolate",
                "Clouds",
                "Clumsy",
                "Color",
                "Comfort",
                "Cute",
                "Dance",
                "Dazzle",
                "Doki-Doki",
                "Email",
                "Excitement",
                "Extraordinary",
                "Family",
                "Fantasy",
                "Feather",
                "Fireflies",
                "Fireworks",
                "Flower",
                "Fluffy",
                "Flying",
                "Friends",
                "Fun",
                "Games",
                "Giggle",
                "Hair",
                "Happiness",
                "Headphones",
                "Heart",
                "Heartbeat",
                "Holiday",
                "Hop",
                "Jump",
                "Jumpy",
                "Kawaii",
                "Kiss",
                "Kitty",
                "Laugh",
                "Lazy",
                "Lipstick",
                "Lollipop",
                "Loud",
                "Love",
                "Lucky",
                "Marriage",
                "Marshmallow",
                "Melody",
                "Memories",
                "Milk",
                "Mouse",
                "Music",
                "Nature",
                "Nibble",
                "Nightgown",
                "Ocean",
                "Papa",
                "Parfait",
                "Party",
                "Passion",
                "Peace",
                "Pink",
                "Play",
                "Playground",
                "Poof",
                "Pout",
                "Precious",
                "Promise",
                "Puppy",
                "Pure",
                "Rainbow",
                "Raincloud",
                "Ribbon",
                "Romance",
                "Sadness",
                "Shiny",
                "Shopping",
                "Silly",
                "Sing",
                "Skipping",
                "Skirt",
                "Smile",
                "Socks",
                "Sparkle",
                "Special",
                "Spinning",
                "Sticky",
                "Strawberry",
                "Sugar",
                "Summer",
                "Sunny",
                "Sunset",
                "Sweet",
                "Swimsuit",
                "Together",
                "Treasure",
                "Twirl",
                "Vacation",
                "Valentine",
                "Vanilla",
                "Warm",
                "Waterfall",
                "Whisper",
                "Whistle",
                "Wonderful"
            ]
            chance = random.randint(1, 4)
            if chance == 1:
                return ["", " ".join(random.choices(yuri_words, k=20))]
            elif chance == 2:
                return ["", " ".join(random.choices(natsuki_words, k=20))]
            elif chance == 3:
                return ["", " ".join(random.choices(yuri_words + natsuki_words, k=20))]
            elif chance == 4:
                words = []
                for _ in range(20):
                    word = rstr.xeger(monika_words)
                    newword = []
                    for k in range(len(word)):
                        if random.randint(1, 5) == 1:
                            newword.append(" ")
                        elif random.randint(1, 5) == 1:
                            newword.append(random.choice(nonunicode))
                        else:
                            newword.append(word[k])
                    words.append(''.join(newword))
                return ["", " ".join(words)]

    def quotes(self):
        return random.choice([
            "And thus, today marks the day I sold my soul for a cupcake.",
            "Clubs...",
            "Well, tea and reading might not be a pastime for me, but I at least enjoy tea.",
            "...Manga...",
            "I gently open the door",
            "Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands",
            "Ah...I guess it's easier to be close together like this...",
            "H-Hey, I wasn't judging anything...!",
            "It sounds like you really know what you're talking about.",
            "Honestly, it takes a lot of effort to find friends how don't judge, much less friends who are also into it...",
            "I'm already kind of a loser, so I guess I gravitated towards the other losers over time.",
            "Writing is a really personal thing.",
            "Ah, so I joining the club was responsible for ruining the atmosphere...",
            "You shouldn't pick a fight just because someone's opinion is different.",
            "She might be an airhead, but sometimes it's weirdly suspicious that she knows exactly what she's doing.",
            "If you feel guilty, that means you deserves to feel guilty...",
            "Sorry, I'm not as good as everyone else...",
            "Does our school have a napping club...?",
            "That just means you're passionate about reading.",
            "I guess I'll do some more reading tonight.",
            "We have emotions, and we can't always hide them away.",
            "How can the two of you keep fighting when you know you're making your friend feel like this?",
            "And thus, today marks the day I sold my soul to Monika and her irresistible smile."
        ])

    def tagging(self, tamper=False, content=""):
        if not tamper:
            if re.search("^$", content, re.IGNORECASE):
                return "Hm? What is it?"
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi, I guess.",
                    "Hello..."
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "..."
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Um... Good night, I guess."
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return ":zzz: Huh- morning already?"
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Is it a good afternoon?",
                    "What? It's the afternoon?",
                    "Ehhhhhh..."
                ])
            elif re.search(f"(^|[^A-Za-z])((^|mc|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "No I'm not."
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I-It's ok."
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "She does? That's a surprise."
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Does she? It's hard to tell when she's so quiet."
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "She doesn't just love me. She's a bit of a yandere."
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Of course she does. She loves everyone."
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I’m not one for that stuff, maybe ask Monika."
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>|natsuki|<@!?580135631611494403>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I’ll have to agree with you there."
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|mc|<@!?<{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Who? Me? How?"
            else:
                return "Eh?"
        else:
            if re.search("^$", content, re.IGNORECASE):
                return "Hm? What is it?"
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi, I guess.",
                    "Hello..."
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "..."
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Um... Good night, I guess."
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return ":zzz: Huh- morning already?"
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Is it a good afternoon?",
                    "What? It's the afternoon?",
                    "Ehhhhhh..."
                ])
            elif re.search(f"(^|[^A-Za-z])((^|mc|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "No I'm not."
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I-It's ok."
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "She does? That's a surprise."
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Does she? It's hard to tell when she's so quiet."
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "She doesn't just love me. She's a bit of a yandere."
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Of course she does. She loves everyone."
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I’m not one for that stuff, maybe ask Monika."
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>|natsuki|<@!?580135631611494403>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I’ll have to agree with you there."
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|mc|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Who? Me? How?"
            else:
                return "Eh?"

    def tickle(self, tamper=False):
        if not tamper:
            return "I'm not ticklish, please stop."
        else:
            return "I'm not ticklish, please stop."

    def triggers(self, tamper=False, content=""):
        if not tamper:
            if re.search("(^|[^A-Za-z])ropes?([^A-Za-z]|$)", content, re.IGNORECASE):
                return "NO!"
            elif re.search("(^|[^A-Za-z])poetry([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Oh... you make poems too, cool."
        else:
            if re.search("(^|[^A-Za-z])ropes?([^A-Za-z]|$)", content, re.IGNORECASE):
                return "NO!"
            elif re.search("(^|[^A-Za-z])poetry([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Oh... you make poems too, cool."
        
    def welcome(self, tamper=False, member=False):
        if not tamper and member:
            return random.choice([
                rstr.xeger(r"Welcome to the club( newest member)? " + member + r"\."),
                f"Hey, {member}. Welcome to the club."
            ])
            
        elif member:
            return f"Ayyyo welcome to the club {member} little buddy!"
        return