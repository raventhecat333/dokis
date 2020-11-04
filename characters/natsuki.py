import random, re, rstr

class natsuki():

    def __init__(self):
        self.color = "0xff42e2"
        self.description = "Natsuki is a character in the game Doki Doki Literature Club, she is a member of the Literature Club and along with her club members she spends her time after school in the club."
        self.id = 580135631611494403
        self.token = "NTgwMTM1NjMxNjExNDk0NDAz.XqMmkQ.pB-HDavBkbWEcn8sB_413TArv7c"
        self.prefix = "(N|n)(atsuki)?_"
        self.help = {
            "commands": {
                "ask [question]": "Ask Natsuki anything you want to ask.",
                "changelog": "See the latest changes. (alias: log)",
                "debug": "View Natsuki's statistics.",
                "feed [emote]": "Give Natsuki food. (alias: eat)",
                "headpat": "Headpat Natsuki. (alias: pat)",
                "help [about]": "Help about Natsuki. (alias: manual)",
                "hug [person]": "Let Natsuki hug someone.",
                "invite": "Invite Natsuki to your server.",
                "motivate [person]": "Natsuki will motivate anyone.",
                "ping": "Get Natsuki's heartbeat. (alias: doki)",
                "poems [poem name]": "Get Natsuki's poems from the game. (alias: poem)",
                "quotes": "Get Natsuki's quotes from the game. (alias: quote)",
                "recipes": "Natsuki will present you with delicious recipes. (alias: recipe)",
                "shard": "Check which shard are you on for Natsuki.",
                "tamper": "Mess up or fix Natsuki's personality.",
                "tickle": "Tickle Natsuki.",
                "trigger": "Set triggers for Natsuki on/off. (alias: triggers)"
            },
            "phrases": {
                "Hello": "Say hello to Natsuki.",
                "Love": "Tell Natsuki you or someone else loves him",
                "Good Morning": "Greet Natsuki with a good morning.",
                "Good Night": "Greet Natsuki with a good night.",
                "Good Afternoon": "Greet Natsuki with a good afternoon.",
                "Compliment": "Give Natsuki a compliment.",
                "Apologize": "Apologize to Natsuki.",
                "Sick": "Tell Natsuki when you are sick.",
                "Best Girl": "Tell Natsuki who's the best girl."
            },
            "triggers": ["dad", "cupcake", "manga"]
        }

    def playing(self):
        return [
            "Type 'n_help' for help!",
            "Doki Doki Literature Club",
            "Don't Starve",
            "Cooking Mama",
            "some anime through your computer!"
        ]

    def ask(self, tamper=False, nothing=False):
        if not tamper:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(Yes|No|Maybe)\."),
                    "How should I know, dummy?",
                    "I guess so.",
                    "Pfft. In your dreams!",
                    "Eh. Probably not.",
                    "Is manga literature?",
                    "Yuri might know.",
                    "If Sayori could get her head out of her fantasy world, she might be able to answer that for you.",
                    "I don't know. Ask Monika if you want the answer that badly."
                ])
            else:
                return "Hey! You wanted to ask me something so what is it?!"
        else:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(Yes|No|Maybe)\."),
                    "How should I know, dummy?",
                    "I guess so.",
                    "Pfft. In your dreams!",
                    "Eh. Probably not.",
                    "Is manga literature?",
                    "Yuri might know.",
                    "If Sayori could get her head out of the clouds, she might be able to answer that for you\.",
                    "I don't know. Ask Monika if you want the answer that badly."
                ])
            else:
                return "Hey! You wanted to ask me something so what is it?!"
        return 

    def everyone(self):
        return "Did you try to make me ping everyone? Well, uhh... Nice try, I suppose."

    def feed(self, tamper=False, food=[], user=""):
        if not tamper:
            if not food:
                return "H-hey! Don't feel like you have to feed me anything! I'm okay!"
            elif "cookie" in food:
                return "I suppose a cookie wouldn't hurt."
            elif "cupcake" in food:
                return "Why are you giving me this dummy?! I'm sure my handmade cupcakes tastes better."
            elif "japanese" in food:
                return "Ah, this is a more familiar meal."
            elif "takeout" in food:
                return "Oh! it's been so long since I last had this, thanks."
            elif "pizza" in food:
                return "F-fine, I'll have a slice."
            elif "burger" in food:
                return "...only because there's cheese on it..."
            elif "falafel" in food:
                return "What kind of food is that? slowly bites Oh.. It's not bad I guess..."
            elif "ice" in food:
                return "Who in the world gives somebody an ice cube??"
            elif "cold" in food:
                return "Thanks, I guess. I was actually feeling a bit warm."
            elif "cold_drink" in food:
                return "It's never too cold for a cold drink."
            elif "canned" in food:
                return "Really? How gives a canned food without a can opener."
            elif "alcohol" in food:
                return "Hey, what's the idea?? You trying to get me drunk??"
            elif "coffee" in food:
                return "I don't really like coffee that much, but thanks, anyway."
            elif "tea" in food:
                return "*sips* Just the right temperature. I guess you're not inconsiderate, after all!"
            elif "bread" in food:
                return "Well, it's more than Papa gives me..."
            elif "sandwich" in food:
                return "Wait, are you giving this to me? thanks I uhh, forgot my lunch."
            elif "waffle" in food:
                return "I already ate breakfast, But... I'd love to have the waffle.. Okay?"
            elif "croissant" in food:
                return "Thanks, did you make these? Actually nevermind, I can tell it's store bought, but thanks anyway....."
            elif "pastries" in food:
                return random.choice([
                    "I suppose, eating a sweet that I didn't bake won't hurt, I guess...",
                    "Oh? thanks, these aren't as good as what I could make but I'm hungry so.."
                ])
            elif "butter" in food:
                return "I don't know why you're giving me this.. but I'll save it for my baking recipes."
            elif "pepper" in food:
                return "H-Hey!! My freaking mouth is on fire!!!"
            elif "cooking" in food:
                return "Sunny-side up? How did you know that's how I liked them?"
            elif "mexican" in food:
                return "Mexican, huh? Not my first choice, but it's still pretty good..."
            elif "sweets" in food:
                return "Well, I suppose it would be nice to eat a sweet that I didn't bake, for once."
            elif "peanuts" in food:
                return "Oh, it's not much but..thanks I guess"
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "I feel like there's a loli joke to be made here..."
            elif "egg" in food:
                return "*crunch crunch crunch*"
            elif "salt" in food:
                return random.choice([
                    "Are you referencing that I'm salty?? ***Dummy!***",
                    "My biggest nightmare is that something doesn't have enough salt."
                ])
            elif "silverware" in food:
                return "I'd prefer actual food here, please! N-not that you have to give me any or anything..."
            elif "bowl" in food:
                return "Really?? Empty bowl... Are you trying to be funny?"
            elif "milk" in food:
                return "What, you didn't have strawberry milk?? Ah, whatever. I guess this is fine..."
            elif "birthday_not" in food:
                return "Huh? It's not my birthday!"
            elif "birthday" in food:
                return random.choice([
                    "Why you're giving me this? I had already made Monika a birthday cake...",
                    "I'm sure my homemade cake, tastes better than any other cake..."
                ])
            elif "misc" in food:
                return "...t-thank you. *slowly eats*"
            else:
                return "Are you trying to hurt me?? That's not food!"
            
        else:
            
            if not food:
                return "H-hey! Don't feel like you have to feed me anything! I'm okay!"
            elif "cookie" in food:
                return "I suppose a cookie wouldn't hurt."
            elif "cupcake" in food:
                return "Why are you giving me this dummy?! I'm sure my handmade cupcakes tastes better."
            elif "japanese" in food:
                return "Ah, this is a more familiar meal."
            elif "takeout" in food:
                return "Oh! it's been so long since I last had this, thanks."
            elif "pizza" in food:
                return "F-fine, I'll have a slice."
            elif "burger" in food:
                return "...only because there's cheese on it..."
            elif "falafel" in food:
                return "What kind of food is that? slowly bites Oh.. It's not bad I guess..."
            elif "ice" in food:
                return "Who in the world gives somebody an ice cube??"
            elif "cold" in food:
                return "Thanks, I guess. I was actually feeling a bit warm."
            elif "cold_drink" in food:
                return "It's never too cold for a cold drink."
            elif "canned" in food:
                return "Really? How gives a canned food without a can opener."
            elif "alcohol" in food:
                return "Hey, what's the idea?? You trying to get me drunk??"
            elif "coffee" in food:
                return "I don't really like coffee that much, but thanks, anyway."
            elif "tea" in food:
                return "*sips* Just the right temperature. I guess you're not inconsiderate, after all!"
            elif "bread" in food:
                return "Well, it's more than Papa gives me..."
            elif "sandwich" in food:
                return "Wait, are you giving this to me? thanks I uhh, forgot my lunch."
            elif "waffle" in food:
                return "I already ate breakfast, But... I'd love to have the waffle.. Okay?"
            elif "croissant" in food:
                return "Thanks, did you make these? Actually nevermind, I can tell it's store bought, but thanks anyway....."
            elif "pastries" in food:
                return random.choice([
                    "I suppose, eating a sweet that I didn't bake won't hurt, I guess...",
                    "Oh? thanks, these aren't as good as what I could make but I'm hungry so.."
                ])
            elif "butter" in food:
                return "I don't know why you're giving me this.. but I'll save it for my baking recipes."
            elif "pepper" in food:
                return "H-Hey!! My freaking mouth is on fire!!!"
            elif "cooking" in food:
                return "Sunny-side up? How did you know that's how I liked them?"
            elif "mexican" in food:
                return "Mexican, huh? Not my first choice, but it's still pretty good..."
            elif "sweets" in food:
                return "Well, I suppose it would be nice to eat a sweet that I didn't bake, for once."
            elif "peanuts" in food:
                return "Oh, it's not much but..thanks I guess"
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "I feel like there's a loli joke to be made here..."
            elif "egg" in food:
                return "*crunch crunch crunch*"
            elif "salt" in food:
                return random.choice([
                    "Are you referencing that I'm salty?? ***Dummy!***",
                    "My biggest nightmare is that something doesn't have enough salt."
                ])
            elif "silverware" in food:
                return "I'd prefer actual food here, please! N-not that you have to give me any or anything..."
            elif "bowl" in food:
                return "Really?? Empty bowl... Are you trying to be funny?"
            elif "milk" in food:
                return "What, you didn't have strawberry milk?? Ah, whatever. I guess this is fine..."
            elif "birthday_not" in food:
                return "Huh? It's not my birthday!"
            elif "birthday" in food:
                return random.choice([
                    "Why you're giving me this? I had already made Monika a birthday cake...",
                    "I'm sure my homemade cake, tastes better than any other cake..."
                ])
            elif "misc" in food:
                return "...t-thank you. *slowly eats*"
            else:
                return "Are you trying to hurt me?? That's not food!"

        return

    def headpat(self, tamper=False):
        if not tamper:
            return random.choice([
                "Hey! Don't pat me so hard!",
                "Geez, you're gonna mess up my hair!",
                "...okay, I guess that kinda felt nice...",
                "What do I look like, a puppy??",
                "T-thanks, I guess..."
            ])
        else:
            return random.choice([
                "Hey! Don't pat me so hard!",
                "Geez, you're gonna mess up my hair!",
                "...okay, I guess that kinda felt nice...",
                "What do I look like, a puppy??",
                "T-thanks, I guess..."
            ])
        return

    def hug(self, tamper=False, target="", targetName=""):
        if not tamper:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"F-fine, but only because I'll look like a jerk if I don't! *hugs {targetName}*",
                    f"I guess a quick hug never hurt anyone... *hugs {targetName}*"
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
                    f"F-fine, but only because I'll look like a jerk if I don't! *hugs {targetName}*",
                    f"I guess a quick hug never hurt anyone... *hugs {targetName}*"
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
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Okay, this is just awkward for both of us."
                if "oh, really? she, of all people, said that?" in content.lower():
                    return "***NO!!!*** I never said that!!"
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "H-hey! Let me go, Sayori!!"
                if "awww, she does??" in content.lower():
                    return "S-shut up! No, I don't!"
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Geez, Yuri! Don't make it all awkward!"
                if "oh... i see..." in content.lower():
                    return "...great, now I look like the bad guy!"
                if "sh-she does?" in content.lower():
                    return "Urk! N-No! Not like that!!"
                if "pfft. as if. that immature brat doesn't love anyone but herself." in content.lower():
                    return "What the hell?? Yuri, why would you say something so mean??"
                if "because it's the fucking truth, you little bitch!!" in content.lower():
                    return ":rage: :rage: :rage:"
                if "get your fucking hands off of me!!" in content.lower():
                    return ":angry:"
                if "no shocker there, you selfish bitch!" in content.lower():
                    return ":angry:"
            elif message.author.id == natsukiID:
                if "*blushes* o-oh..." in content.lower():
                    return "Well, I-I do too..."
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Ah! You scared me, <@{mcID}>"
                if "h-hey, natsuki?" in content.lower():
                    return "What do you want, dummy?"
                if "i-i love you, natsuki..." in content.lower():
                    return "*blushes* O-Oh..."
                if "*hugs natsuki*" in content.lower():
                    return "*hugs back*"
                if "i'm not surprised she would say that, given how much of a tsundere she is." in content.lower():
                    return "***I AM NOT A TSUNDERE, YOU BAKA!!!***"
        else:
            if message.author.id == monikaID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Okay, this is just awkward for both of us."
                if "oh, really? she, of all people, said that?" in content.lower():
                    return "***NO!!!*** I never said that!!"
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "H-hey! Let me go, Sayori!!"
                if "awww, she does??" in content.lower():
                    return "S-shut up! No, I don't!"
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Geez, Yuri! Don't make it all awkward!"
                if "oh... i see..." in content.lower():
                    return "...great, now I look like the bad guy!"
                if "sh-she does?" in content.lower():
                    return "Urk! N-No! Not like that!!"
                if "pfft. as if. that immature brat doesn't love anyone but herself." in content.lower():
                    return "What the hell?? Yuri, why would you say something so mean??"
                if "because it's the fucking truth, you little bitch!!" in content.lower():
                    return ":rage: :rage: :rage:"
                if "get your fucking hands off of me!!" in content.lower():
                    return ":angry:"
                if "no shocker there, you selfish bitch!" in content.lower():
                    return ":angry:"
            elif message.author.id == natsukiID:
                if "*blushes* o-oh..." in content.lower():
                    return "Well, I-I do too..."
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Ah! You scared me, <@{mcID}>"
                if "h-hey, natsuki?" in content.lower():
                    return "What do you want, dummy?"
                if "i-i love you, natsuki..." in content.lower():
                    return "*blushes* O-Oh..."
                if "*hugs natsuki*" in content.lower():
                    return "*hugs back*"
                if "i'm not surprised she would say that, given how much of a tsundere she is." in content.lower():
                    return "***I AM NOT A TSUNDERE, YOU BAKA!!!***"

    def motivate(self, target=""):
        return random.choice([
            f"I believe in you {target}, you stupid sack of shit!",
            "C'mon, dummy! You can do it!",
            "*grabs shoulders* You've got this! I know you do!",
            "I'll bake you as many cupcakes as you want!",
            "You better do good or I'll shatter your shins!",
            "C'mon! Don't be a lazy goofball like Sayori!",
            "You better not act as dense as MC!",
            "DO IT! Just DO IT!!!",
            "Don't let your dreams be dreams!"
        ])
    
    def poems(self, tamper=False, name=""):

        if not tamper:
            poem1 = [
                "Eagles Can Fly",
                "Monkeys can climb\nCrickets can leap\nHorses can race\nOwls can seek\nCheetahs can run\nEagles can fly\nPeople can try\nBut that's about it"
            ]
            poem2 = [
                "Amy Likes Spiders",
                "You know what I heard about Amy?\nAmy likes spiders.\nIcky, wriggly, hairy, ugly spiders!\nThat's why I'm not friends with her.\nAmy has a cute singing voice.\nI heard her singing my favorite love song.\nEvery time she sang the chorus, my heart would pound to the rhythm of the words.\nBut she likes spiders.\nThat's why I'm not friends with her.\nOne time, I hurt my leg really bad.\nAmy helped me up and took me to the nurse.\nI tried not to let her touch me.\nShe likes spiders, so her hands are probably gross.\nThat's why I'm not friends with her.\nAmy has a lot of friends.\nI always see her talking to people.\nShe probably talks about spiders.\nWhat if her friends start to like spiders too?\nThat's why I'm not friends with her.\nIt doesn't matter if she has other hobbies.\nIt doesn't matter if she keeps it private.\nIt doesn't matter if it doesn't hurt anyone.\nIt's gross.\nShe's gross.\nThe world is better off without spider lovers.\nAnd I'm gonna tell everyone."
            ]
            poem3 = [
                "Because You",
                "Tomorrow will be brighter with me around\nBut when today is dim, I can only look down.\nMy looking is a little more forward\nBecause you look at me.\n\nWhen I want to say something, I say it with a shout!\nBut my truest feelings can never come out.\nMy words are a little less empty\nBecause you listen to me.\n\nWhen something is above me, I reach for the stars.\nBut when I feel small, I don't get very far.\nMy standing is a little bit taller\nBecause you sit with me.\n\nI believe in myself with all of my heart.\nBut what do I do when it's torn all apart?\nMy faith is a little bit stronger\nBecause you trusted me.\n\nMy pen always puts my feelings to the test.\nI'm not a good writer, but my best is my best.\n\nMy poems are a little bit dearer\nBecause you think of me.\n\nBecause you, because you, because you."
            ]
            poem4 = [
                "I'll Be Your Beach",
                "Your mind is so full of troubles and fears\nThat diminished your wonder over the years\nBut today I have a special place\nA beach for us to go.\n\nA shore reaching beyond your sight\nA sea that sparkles with brilliant light\nThe walls in your mind will melt away\nBefore the sunny glow.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nLet's bury your heavy thoughts in a pile of sand\nBathe in sunbeams and hold my hand\nWash your insecurities in the salty sea\nAnd let me see you shine.\n\nLet's leave your memories in a footprint trail\nSet you free in my windy sail\nAnd remember the reasons you're wonderful\nWhen you press your lips to mine.\n\nI'll be the beach that washes your worries away\nI'll be the beach that you daydream about each day\nI'll be the beach that makes your heart leap\nIn a way you thought had left you long ago.\n\nBut if you let me by your side\nYour own beach, your own escape\nYou'll learn to love yourself again."
            ]
            if name.lower() == "eagles can fly":
                return poem1
            elif name.lower() == "amy likes spiders":
                return poem2
            elif name.lower() == "because you":
                return poem3
            elif name.lower() == "i'll be your beach":
                return poem4
            else:
                return random.choice([poem1,poem2,poem3,poem4])
        else:
            poem1 = [
                "T3BlbiBZb3VylFRoaXJkIEV5ZQ==",
                "SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5 IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l dGhpbmcgaW5jcmVkaWJseSBmYWludCwg ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0 b3AgbXlzZWxmLg=="
            ]
            poem2 = [
                "",
                "I don't know how else to bring this up. But there's been something I've been worried about. Yuri has been acting kind of strange lately. You've only been here a few days, so you may not know what I mean. But she's not normally like this. She's always been quiet and polite and attentive...things like that.\n\nOkay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY worried about her. But if I try talking to her, she'll just get mad at me again. I don't know what to do. I think you're the only person that she'll listen to. I don't know why. But please try to do something. Maybe you can convince her to talk to a therapist.\n\nI've always wanted to try being better friends with Yuri, and it really hurts me to see this happening. I know I'm going to hate myself later for admitting that, but right now I don't care. I just feel so helpless. So please see if you can do something to help. I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please try to do something. As for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? I'm counting on you. Thanks for reading"
            ]
            if name.lower() == "t3blbibzb3vylfroaxjkiev5zq==":
                return poem1
            else:
                return random.choice([poem1,poem2])

    def quotes(self):
        return random.choice([
            "MANGA IS LITERATURE!",
            "I'M NOT CUTE!",
            "Well, you know what?! I wasn't the one whose boobs magically grew a size bigger as soon as MC started showing up!!",
            "Whoa, be careful or you might cut yourself on that edge, Yuri. Oh, my bad... You already do, don't you?",
            "Freaking Monika!",
            "***fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm***",
            "You really shouldn't do that kind of thing to girls...unless you really like them...",
            "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--",
            "You really need to...beat...the crap out of it!",
            "If you really just came for the cupcakes, I would be super pissed."
        ])

    def recipes(self):
        reply = random.choice([
            "Oh, here's a really good one!",
            "This one's fun to make!",
            "Just wash your gross hands, first!",
            "This one's delicious!"
        ])
        recipe = random.choice([
            "https://www.foodnetwork.com/recipes/giada-de-laurentiis/smore-brownie-bites-recipe-2125911",
            "https://www.foodnetwork.com/recipes/rich-nut-cookies-recipe-1913332",
            "https://www.foodnetwork.com/recipes/sandra-lee/chocolate-caramel-brownies-recipe-1924027",
            "https://www.foodnetwork.com/recipes/apple-muffins-recipe-1927541",
            "https://www.foodnetwork.com/recipes/claire-robinson/brown-butter-banana-muffins-recipe-1920734",
            "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/easy-sticky-buns-recipe-1924654",
            "https://www.foodnetwork.com/recipes/anne-thornton/nutella-banana-brioche-bread-pudding-recipe-1923849",
            "https://www.foodnetwork.com/recipes/ina-garten/fresh-peach-cake-recipe-1923148",
            "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/cookie-pizza-recipe-1924170",
            "https://www.foodnetwork.com/recipes/melissa-darabian/petite-orange-and-raspberry-pochettes-recipe-1973221",
            "https://www.foodnetwork.com/recipes/ina-garten/cinnamon-elephant-ears-recipe-1923543",
            "https://www.foodnetwork.com/recipes/claire-robinson/lemon-pie-cookies-recipe-1923177",
            "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/honey-cornbread-muffins-recipe-2013336",
            "https://www.foodnetwork.com/recipes/double-fudge-bread-pudding-with-chocolate-whipped-topping-recipe-1923356",
            "https://www.foodnetwork.com/recipes/giada-de-laurentiis/double-chocolate-and-mint-cookies-recipe-2010334",
            "https://www.foodnetwork.com/recipes/sandra-lee/milk-chocolate-cupcakes-with-dark-chocolate-icing-recipe-1923562",
            "https://www.foodnetwork.com/recipes/aaron-mccargo-jr/zucchini-and-apple-bread-recipe-1924223",
            "https://www.foodnetwork.com/recipes/food-network-kitchen/vanilla-cupcakes-recipe2-2042539",
            "https://www.foodnetwork.com/recipes/sunny-anderson/open-faced-plum-tart-recipe2-1973744",
            "https://www.foodnetwork.com/recipes/marcela-valladolid/polvorones-ground-walnut-cookies-recipe-1960437",
            "https://www.foodnetwork.com/recipes/anne-thornton/mama-thorntons-peach-pie-recipe-2047258",
            "https://www.foodnetwork.com/recipes/pumpkin-spice-cupcakes-with-brown-butter-buttercream-recipe-1923349",
            "https://www.foodnetwork.com/recipes/chocolate-cupcakes-with-ganache-and-marshmallow-frosting-recipe-1923296",
            "https://www.foodnetwork.com/recipes/melissa-darabian/chocolate-sponge-puddings-recipe-2014543",
            "https://www.foodnetwork.com/recipes/bubbys-sour-cherry-pie-recipe-2200888"
        ])
        return f"{reply} {recipe}"

    def tagging(self, tamper=False, content=""):
        if not tamper:
            if re.search("^$", content, re.IGNORECASE):
                return "Yes?"
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi, I guess...",
                    "What, do I have to greet you back or something?",
                    "Hey there, Dummy!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "...I love you, too, okay??",
                    "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!",
                    "*urk!* :flushed:",
                    "Shut up! You don't mean that!"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Goodnight, Dummy!",
                    "Goodnight, then.",
                    "You better get good rest or I'll punch you!",
                    "Sleep well, baka!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Well, it's *A* morning, I guess...",
                    "Good morning to everyone except my dad.",
                    "Did you get a good night's sleep? Er, not that I really care!!"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon, I guess.",
                    "Afternoon.",
                    "Yeah, so it's the afternoon. What's your point?"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|natsuki|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "***I'M NOT CUTE!!!***",
                    "Hey! I'm not cute!",
                    "Sh-shut up! I'm not cute!!",
                    "Have you ever considered that maybe I want to be something other than cute?!"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hmph. I'll forgive you, but it's not like you deserve it!",
                    "Fine. I guess I'll let it go...",
                    "You better be sorry, you baka!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Act 2 says otherwise."
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "W-Well it's not like I love her back or anything!!"
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "S-shut up! No she doesn't!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ha! I'm sure he does! I-I'll believe it when he tells me that himself!"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ok... well you'd better get better soon... not that I care or anything..",
                    "Ok dummy! Get rest!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Pfft! As if!"
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|natsuki|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ha! Of course I am!"
            else:
                return "Uh... What?"
        else:
            if re.search("^$", content, re.IGNORECASE):
                return "Yes?"
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi, I guess...",
                    "What, do I have to greet you back or something?",
                    "Hey there, Dummy!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "...I love you, too, okay??",
                    "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!",
                    "*urk!* :flushed:",
                    "Shut up! You don't mean that!"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Goodnight, Dummy!",
                    "Goodnight, then.",
                    "You better get good rest or I'll punch you!",
                    "Sleep well, baka!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Well, it's *A* morning, I guess...",
                    "Good morning to everyone except my dad.",
                    "Did you get a good night's sleep? Er, not that I really care!!"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon, I guess.",
                    "Afternoon.",
                    "Yeah, so it's the afternoon. What's your point?"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|natsuki|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "***I'M NOT CUTE!!!***",
                    "Hey! I'm not cute!",
                    "Sh-shut up! I'm not cute!!",
                    "Have you ever considered that maybe I want to be something other than cute?!"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hmph. I'll forgive you, but it's not like you deserve it!",
                    "Fine. I guess I'll let it go...",
                    "You better be sorry, you baka!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Act 2 says otherwise."
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "W-Well it's not like I love her back or anything!!"
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "S-shut up! No she doesn't!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ha! I'm sure he does! I-I'll believe it when he tells me that himself!"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ok... well you'd better get better soon... not that I care or anything..",
                    "Ok dummy! Get rest!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Pfft! As if!"
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|natsuki|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ha! Of course I am!"
            else:
                return "Uh... What?"

    def tickle(self, tamper=False):
        if not tamper:
            return rstr.xeger(r"((H-hey! Cut that out!!|I'm gonna break your ribs for this!|STOP IT! STOP!) )?((Ha|A)(ha){3,6}|(He|E)(he){3,6}|(HE|E)(HE){3,6})!{1,3}")
        else:
            return rstr.xeger(r"((H-hey! Cut that out!!|I'm gonna break your ribs for this!|STOP IT! STOP!) )?((Ha|A)(ha){3,6}|(He|E)(he){3,6}|(HE|E)(HE){3,6})!{1,3}")

    def triggers(self, tamper=False, content=""):
        if not tamper:
            if re.search("(^|[^A-Za-z])(dad(dy)?|papa|father)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hey! Can you not say that word around me, you jerk??",
                    "W-what?? Is Papa here??"
                ])
            elif re.search("(^|[^A-Za-z])cupcakes?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "What did you call me??",
                    "Yes?"
                ])
            elif re.search("(^|[^A-Za-z])mangas?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "You like manga, too?? I-I mean, it's not like I like manga or anything...!",
                    "...!",
                    "***MANGA IS LITERATURE!***"
                ])
        else:
            if re.search("(^|[^A-Za-z])(dad(dy)?|papa|father)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hey! Can you not say that word around me, you jerk??",
                    "W-what?? Is Papa here??"
                ])
            elif re.search("(^|[^A-Za-z])cupcakes?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "What did you call me??",
                    "Yes?"
                ])
            elif re.search("(^|[^A-Za-z])mangas?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "You like manga, too?? I-I mean, it's not like I like manga or anything...!",
                    "...!",
                    "***MANGA IS LITERATURE!***"
                ])

    def welcome(self, tamper=False, member=False):
        if not tamper and member:
            return rstr.xeger(r"Seriously\?(You brought )?" + member + r"\? (Way to kill the atmosphere|I can't believe I thought this was a gonna be a small club|I didn't sign up for this)\.")
        elif member:
            return f"{member} Dammit why did the likes of YOU join the club?"
        return