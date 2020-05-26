import asyncio, discord, random, re, rstr

class monika():

    def __init__(self):
        self.color = "0x12ba01"
        self.description = "Monika is a character in the game Doki Doki Literature Club, she is the president of the Literature Club founded by her and along with her club members she spends her time after school in the club."
        self.id = 707337539677192272
        self.token = "NzA3MzM3NTM5Njc3MTkyMjcy.XrHVuA._ktH6TojEZJtFIr10QMyc_fmjR0"
        self.prefix = "(M|m)(onika)?_"
        self.deletes = []
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.delete_clear())
        self.help = {
            "commands": {
                "ask [question]": "Ask Monika anything you want to ask.",
                "changelog": "See the latest changes. (alias: log)",
                "debug": "View Monika's statistics.",
                "delete [target]": "Monika will delete your problems",
                "feed [emote]": "Give Monika food. (alias: eat)",
                "headpat": "Headpat Monika. (alias: pat)",
                "help [about]": "Help about Monika. (alias: manual)",
                "hug [person]": "Let Monika hug someone.",
                "invite": "Invite Monika to your server.",
                "ping": "Get Monika's heartbeat. (alias: doki)",
                "poems [poem name]": "Get Monika's poems from the game. (alias: poem)",
                "quotes": "Get Monika's quotes from the game. (alias: quote)",
                "shard": "Check which shard are you on for Monika.",
                "tamper": "Mess up or fix Monika's personality.",
                "tickle": "Tickle Monika.",
                "trigger": "Set triggers for Monika on/off. (alias: triggers)"
            },
            "phrases": {
                "Hello": "Say hello to Monika.",
                "Love": "Tell Monika you or someone else loves him",
                "Good Morning": "Greet Monika with a good morning.",
                "Good Night": "Greet Monika with a good night.",
                "Good Afternoon": "Greet Monika with a good afternoon.",
                "Compliment": "Give Monika a compliment.",
                "Apologize": "Apologize to Monika.",
                "Sick": "Tell Monika when you are sick.",
                "Best Girl": "Tell Monika who's the best girl."
            },
            "triggers": ["piano", "cacophony", "code", "python", "reality", "poems", "literature", "just monika"]
        }

    def playing(self):
        return [
            "Type 'm_help' for help!",
            "Doki Doki Literature Club",
            "the piano!",
            r"Super Smash Bros Ultimate\.",
            "If My Heart Had Wings",
            "with you!",
            r"Just Monika\.",
            "from your computer!",
            "your reality!"
        ]

    def ask(self, tamper=False, nothing=False):
        if not tamper:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(No|Yes)!"),
                    rstr.xeger(r"As Club President, I say '(yes|no|maybe)'!"),
                    "Ahaha! I-I don't really know, to be honest...",
                    "Uh... Well, uh... I think the Vice President would be better suited for this question!",
                    "Y-Yuri's smart, right? I'm sure she can answer that!",
                    "Maybe you can try asking Natsuki; she knows more than she lets on."
                ])
            else:
                return "Ahaha! D-did you want to ask me something?"
        else:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(No|Yes)!"),
                    rstr.xeger(r"As Club President, I say '(yes|no|maybe)'!"),
                    "Ahaha! I-I don't really know, to be honest...",
                    "Uh... Well, uh... I think the Vice President would be better suited for this question!",
                    "Y-Yuri's smart, right? I'm sure she can answer that!",
                    "Maybe you can try asking Natsuki; she knows more than she lets on."
                ])
            else:
                return "Ahaha! D-did you want to ask me something?"
        return 
    
    def delete(self, tamper=False, victim="", victimName="", channel=0):
        if not tamper:
            if not victim:
                return "What do you need me to delete?"
            elif victim == "doki":
                return "Ahahahaha! You know, I tried that once. Didn't really work out well in the long run."
            elif victim == "player":
                return "Why would i want to do that?"
            elif victim == "dev":
                return "Why would you want to delete the man who gave you the ability to use me? Shame on you!"
            elif victim == "self":
                return "Ahahahaha! No."
            else:
                self.deletes.append([channel, victimName])
                return f"os.remove(\"./characters/{victimName}.chr\")"
        else:
            if not victim:
                return "What do you need me to delete?"
            elif victim == "player":
                return "Why would i want to do that?"
            elif victim == "dev":
                return "Why would you want to delete the man who gave you the ability to use me? Shame on you!"
            elif victim == "self":
                return "Ahahahaha! No."
            else:
                self.deletes.append([channel, victimName])
                return f"os.remove(\"./characters/{victimName}.chr\")"
        return

    async def delete_clear(self):
        while True:
            if len(self.deletes) > 0:
                self.deletes.pop(0)
            await asyncio.sleep(100)

    def everyone(self):
        return "There's no way I'm letting you ping everyone."

    def feed(self, tamper=False, food=[], user=""):
        if not tamper:
            if not food:
                return "I suppose I am a bit hungry... What do you recommend?"
            elif "cookie" in food:
                return "Not as homemade as Natsuki's, but it's still very delicious! Thank you!"
            elif "cupcake" in food:
                return "Ahahaha, I'm not sure if Natsuki's going to be okay with me eating a cupcake that's not her's."
            elif "japanese" in food:
                return "Aw, you brought me a meal from my home? How thoughtful of you!"
            elif "takeout" in food:
                return "Joy and happiness lays within this box.. Thank you I love having these."
            elif "pizza" in food:
                return "Ah... There's pepperoni on it... You do remember I'm a vegetarian, right?"
            elif "burger" in food:
                return "Is it a veggie burger? If not, I'll have to respectfully decline."
            elif "falafel" in food:
                return "Egyptian food? I always likes to try different kind of food from around the world! Thanks."
            elif "meat" in food:
                return "Um.. not be rude, but I'm a vegetarian."
            elif "ice" in food:
                return "Why are you giving me this ice? It's going to melt and go to waste!"
            elif "cold" in food:
                return "Ah, nothing like some cold treats to brighten your day!"
            elif "cold_drink" in food:
                return "Life is better with a cold drink in your hand."
            elif "canned" in food:
                return "Canned food. I hope it doesn't contain any meat though."
            elif "alcohol" in food:
                return "Oh! Ahaha... A-As curious as I am, I'm afraid I cannot allow alcoholic beverages here."
            elif "coffee" in food:
                return "Ah, thank you! I've been needing something to wake me up a bit!"
            elif "tea" in food:
                return "It's like I'm back in the clubroom! All I need is one of Natsuki's cupcakes."
            elif "bread" in food:
                return "It's a start, but I'll need to go to the grocery store to make a proper sandwich. ~~Would you like to come with?~~"
            elif "sandwich" in food:
                return "Is this for me? how kind of you, this doesn't have meat on it does it?"
            elif "waffle" in food:
                return "You brought me waffle? That's so thoughtful of you."
            elif "croissant" in food:
                return "Ah, very fancy! I'm impressed!"
            elif "pastries" in food:
                return "Thank you! are these from that little coffee shop?"
            elif "butter" in food:
                return "Um.. not sure why you're giving me this, but I'm sure Natsuki will make better use of that butter in her baking!"
            elif "pepper" in food:
                return "*cough cough* Oh, my! That certainly caught me off-guard!"
            elif "cooking" in food:
                return "Hm... as a vegetarian, would it even be okay to eat this...?"
            elif "mexican" in food:
                return "Well, I'm always in the mood for something different!"
            elif "sweets" in food:
                return "Sweets! A girl's best friend!"
            elif "nuts" in food:
                return "I love nuts in salad more. The addiction of nuts in salad... I always find it to be beneficial."
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "U-Um... I'm not sure what you're insinuating here..."
            elif "egg" in food:
                return "Oh, you silly goose! Are you trying to be funny?"
            elif "salt" in food:
                return "Did you know if you consume too much salt, it can cause water retention? When this happens, your body usually responds by raising your blood pressure to push excess fluid and salt out of your system."
            elif "silverware" in food:
                return "I've got my silverware ready! What are we eating with them?"
            elif "bowl" in food:
                return "Haha, you silly! Are you trying to be funny?"
            elif "milk" in food:
                return "I suppose it's a good thing I'm not a vegan! Ahaha~!"
            elif "birthday_not" in food:
                return "How wonderful, but I don't believe it's my birthday just yet..."
            elif "birthday" in food:
                return f"Oh, you brought me the birthday cake? Thank you so much {user}."
            elif "misc" in food:
                return "A nice meal is always great! Thank you~"
            else:
                return "Um.. not to be rude, but I don't think this is edible."
            
        else:
            
            if not food:
                return "I suppose I am a bit hungry... What do you recommend?"
            elif "cookie" in food:
                return "Not as homemade as Natsuki's, but it's still very delicious! Thank you!"
            elif "japanese" in food:
                return "Aw, you brought me a meal from my home? How thoughtful of you!"
            elif "takeout" in food:
                return "Joy and happiness lays within this box.. Thank you I love having these."
            elif "pizza" in food:
                return "Ah... There's pepperoni on it... You do remember I'm a vegetarian, right?"
            elif "burger" in food:
                return "Is it a veggie burger? If not, I'll have to respectfully decline."
            elif "falafel" in food:
                return "Egyptian food? I always likes to try different kind of food from around the world! Thanks."
            elif "ice" in food:
                return "Why are you giving me this ice? It's going to melt and go to waste!"
            elif "cold" in food:
                return "Ah, nothing like some cold treats to brighten your day!"
            elif "cold_drink" in food:
                return "Life is better with a cold drink in your hand."
            elif "canned" in food:
                return "Canned food. I hope it doesn't contain any meat though."
            elif "alcohol" in food:
                return "Oh! Ahaha... A-As curious as I am, I'm afraid I cannot allow alcoholic beverages here."
            elif "coffee" in food:
                return "Ah, thank you! I've been needing something to wake me up a bit!"
            elif "tea" in food:
                return "It's like I'm back in the clubroom! All I need is one of Natsuki's cupcakes."
            elif "bread" in food:
                return "It's a start, but I'll need to go to the grocery store to make a proper sandwich. ~~Would you like to come with?~~"
            elif "sandwich" in food:
                return "Is this for me? how kind of you, this doesn't have meat on it does it?"
            elif "waffle" in food:
                return "You brought me waffle? That's so thoughtful of you."
            elif "croissant" in food:
                return "Ah, very fancy! I'm impressed!"
            elif "pastries" in food:
                return "Thank you! are these from that little coffee shop?"
            elif "butter" in food:
                return "Um.. not sure why you're giving me this, but I'm sure Natsuki will make better use of that butter in her baking!"
            elif "pepper" in food:
                return "*cough cough* Oh, my! That certainly caught me off-guard!"
            elif "cooking" in food:
                return "Hm... as a vegetarian, would it even be okay to eat this...?"
            elif "mexican" in food:
                return "Well, I'm always in the mood for something different!"
            elif "sweets" in food:
                return "Sweets! A girl's best friend!"
            elif "nuts" in food:
                return "I love nuts in salad more. The addiction of nuts in salad... I always find it to be beneficial."
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "U-Um... I'm not sure what you're insinuating here..."
            elif "egg" in food:
                return "Oh, you silly goose! Are you trying to be funny?"
            elif "salt" in food:
                return "Did you know if you consume too much salt, it can cause water retention? When this happens, your body usually responds by raising your blood pressure to push excess fluid and salt out of your system."
            elif "silverware" in food:
                return "I've got my silverware ready! What are we eating with them?"
            elif "bowl" in food:
                return "Haha, you silly! Are you trying to be funny?"
            elif "milk" in food:
                return "I suppose it's a good thing I'm not a vegan! Ahaha~!"
            elif "birthday_not" in food:
                return "How wonderful, but I don't believe it's my birthday just yet..."
            elif "birthday" in food:
                return f"Oh, you brought me the birthday cake? Thank you so much {user}."
            elif "misc" in food:
                return "A nice meal is always great! Thank you~"
            else:
                return "Um.. not to be rude, but I don't think this is edible."

        return

    def headpat(self, tamper=False):
        if not tamper:
            return random.choice([
                "Ahaha!~ I-I'm not sure what to say!",
                "Be careful; you may knock my bow down!",
                "E-Easy now!",
                "This doesn't really seem like the type of thing one does to their President, but I suppose I'll let it slide!"
            ])
        else:
            return random.choice([
                "Ahaha!~ I-I'm not sure what to say!",
                "Be careful; you may knock my bow down!",
                "E-Easy now!",
                "This doesn't really seem like the type of thing one does to their President, but I suppose I'll let it slide!"
            ])
        return 

    def hug(self, tamper=False, target="", targetName=""):
        if not tamper:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs {targetName}*",
                    f"Of course I'll hug you! You don't have to even ask twice! *hugs {targetName}*",
                    f"Have you had a rough day? Here, I'll make it a little better! *hugs {targetName}*"
                ])
            elif target == "self":
                return random.choice([
                    "Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*",
                    "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?",
                    "Well, as Club President, it's my job to set a good example! *hugs myself*"
                ])
        else:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs {targetName}*",
                    f"Of course I'll hug you! You don't have to even ask twice! *hugs {targetName}*",
                    f"Have you had a rough day? Here, I'll make it a little better! *hugs {targetName}*"
                ])
            elif target == "self":
                return random.choice([
                    "Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*",
                    "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?",
                    "Well, as Club President, it's my job to set a good example! *hugs myself*"
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
                if "hm. i don't really like this yuri too much. give me a second." in content.lower():
                    return "y_tamper"
                if "ugh, fine." in content.lower():
                    user = next( (c for c in self.deletes if c[0] == message.channel.id), None)
                    self.deletes.remove(user)
                    return discord.Embed(title=f"os.restore(\"./characters/{user[1]}.chr\")",color=int(self.color, base=16))
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~"
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aw, no need to be shy, Yuri! I don't mind a hug every now and then!"
                if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in content.lower():
                    return "Hm. I don't really like this Yuri too much. Give me a second."
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aww, how cute of you, Natsuki!"
                if "okay, this is just awkward for both of us." in content.lower():
                    return "Yeah, I agree."
                if "act2 says otherwise." in content.lower():
                    return "I said I was sorry!"
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Aww, you're the best hugger, <@{mcID}>"
                if f"<@{bot.user.id}>" in content.lower():
                    return f"Yes, <@{mcID}>?"
                if "i need to tell you something." in content.lower():
                    return "Hmm?"
                if "i love you, monika." in content.lower():
                    return "I-I do too!"
                if "not this shit again, monika." in content.lower():
                    return "Ugh, fine."
        else:
            if message.author.id == monikaID:
                if "hm. i don't really like this yuri too much. give me a second." in content.lower():
                    return "y_tamper"
                if "ugh, fine." in content.lower():
                    user = next( (c for c in self.deletes if c[0] == message.channel.id), None)
                    self.deletes.remove(user)
                    return discord.Embed(title=f"os.restore(\"./characters/{user[1]}.chr\")",color=int(self.color, base=16))
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~"
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aw, no need to be shy, Yuri! I don't mind a hug every now and then!"
                if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in content.lower():
                    return "Hm. I don't really like this Yuri too much. Give me a second."
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aww, how cute of you, Natsuki!"
                if "okay, this is just awkward for both of us." in content.lower():
                    return "Yeah, I agree."
                if "act2 says otherwise." in content.lower():
                    return "I said I was sorry!"
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Aww, you're the best hugger, <@{mcID}>"
                if f"<@{bot.user.id}>" in content.lower():
                    return f"Yes, <@{mcID}>?"
                if "i need to tell you something." in content.lower():
                    return "Hmm?"
                if "i love you, monika." in content.lower():
                    return "I-I do too!"
                if "not this shit again, monika." in content.lower():
                    return "Ugh, fine."

    def poems(self, tamper=False, name=""):

        if not tamper:
            poem1 = [
                "Hole in Wall",
                "It couldn't have been me.\nSee, the direction the spackle protrudes.\nA noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.\nI peer inside for a clue.\nNo! I can't see. I reel, blind, like a film left out in the sun.\nBut it's too late. My retinas.\nAlready scorched with a permanent copy of the meaningless image.\nIt's just a little hole. It wasn't too bright.\nIt was too deep.\nStretching forever into everything.\nA hole of infinite choices.\nI realize now, that I wasn't looking in.\nI was looking out.\nAnd he, on the other side, was looking in."
            ]
            poem2 = [
                "Save me",
                "The colors, they won't stop.\nBright, beautiful colors\nFlashing, expanding, piercing\nRed, green, blue\nAn endless\ncacophony\nOf meaningless\nnoise\n\nThe noise, it won't stop.\nViolent, grating waveforms\nSqueaking, screeching, piercing\nSine, cosine, tangent\nLike playing a chalkboard on a turntable\nLike playing a vinyl on a pizza crust\nAn endless\npoem\nOf meaningless\n\nLoad Me"
            ]
            poem3 = [
                "The Lady who Knows Everything",
                "An old tale tells of a lady who wanders Earth.\nThe Lady who Knows Everything.\nA beautiful lady who has found every answer,\nAll meaning,\nAll purpose,\nAnd all that was ever sought.\n\nAnd here I am,\n\na feather\n\nLost adrift the sky, victim of the currents of the wind.\n\nDay after day, I search.\nI search with little hope, knowing legends don't exist.\nBut when all else has failed me,\nWhen all others have turned away,\nThe legend is all that remains – the last dim star glimmering in the twilit sky.\n\nUntil one day, the wind ceases to blow.\nI fall.\nAnd I fall and fall, and fall even more.\nGentle as a feather.\nA dry quill, expressionless.\n\nBut a hand catches me, between the thumb and forefinger.\nThe hand of a beautiful lady.\nI look at her eyes and find no end to her gaze.\n\nThe Lady who Knows Everything knows what I am thinking.\nBefore I can speak, she responds in a hollow voice.\n\"I have found every answer, all of which amount to nothing.\nThere is no meaning.\nThere is no purpose.\nAnd we seek only the impossible.\nI am not your legend.\nYour legend does not exist.\"\n\nAnd with a breath, she blows me back afloat, and I pick up a gust of wind."
            ]
            if name.lower() == "hole in wall":
                return poem1
            elif name.lower() == "save me":
                return poem2
            elif name.lower() == "the lady who knows everything":
                return poem3
            else:
                return random.choice([poem1,poem2,poem3])
        else:
            poem1 = [
                "Hole in Wall",
                "But he wasn't looking at me.\nConfused, I frantically glance at my surroundings.\nBut my burned eyes can no longer see color.\nAre there others in this room? Are they talking?\nOr are they simply poems on flat sheets of paper,\nThe sound of frantic scrawling playing tricks on my ears?\nThe room begins to crinkle.\nClosing in on me.\nThe air I breathe dissipate before it reaches my lungs.\nI panic. There must be a way out.\nIt's right there. He's right there.\n\nSwallowing my fears, I brandish my pen."
            ]
            poem2 = [
                "Save me",
                "The colors, they won't\nBright, bea t ful c l rs\nFlash ng, exp nd ng, piercing\nRed, green, blue\nAn ndless\nCACOPHONY\nOf meaningless\nnoise\n\nThe noise, it won't STOP.\nViol nt, grating w vef rms\nSq e king, screech ng, piercing\nSINE, COSINE, TANGENT\nLike play ng a ch lkboard on a t rntable\nLike playing a KNIFE on a BREATHING RIBCAGE\nn ndl ss\np m\nOf m n ngl ss\n\nDelete Her"
            ]
            poem3 = [
                "Happy End",
                "Pen in hand, I find my strength.\nThe courage endowed upon me by my one and only love.\nTogether, let us dismantle this crumbling world\nAnd write a novel of our own fantasies.\n\nWith a flick of her pen, the lost finds her way.\nIn a world of infinite choices, behold this special day.\n\nAfter all,\nNot all good times must come to an end"
            ]
            if name == "Hole in Wall":
                return poem1
            elif name == "Save me":
                return poem2
            elif name == "Happy End":
                return poem3
            else:
                return random.choice([poem1,poem2,poem3])
        
    def quotes(self):
        return random.choice([
            "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!",
            "I'm confident that we can all really grow this club before we graduate!",
            "Then that makes it official! Welcome to the Literature Club!",
            "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom.",
            "I guess you could say that I had some kind of epiphany recently. It's been influencing my poems a bit.",
            "...That's my advice for today! Thanks for listening~",
            "Wait...is this tip even about writing? What am I even talking about? Ahaha!",
            "Humans aren't two-dimensional creatures. I think you'd know that better than anyone.",
            "Also, that joke makes no sense in translation!",
            "And I also care about the well-being of my club members, you know?",
            "Have you thought that maybe you've always seen her as so cheerful because that's just how she is when she's around you?",
            "C-Catchphrase? I don't have a catchphrase...",
            "Yay, you picked me!",
            "You kind of left her hanging this morning, you know?",
            "Don't worry. I probably know a lot more than you think."
        ])

    def tagging(self, tamper=False, content=""):
        if not tamper:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Yes?",
                    "Does somebody need me?",
                    "I'm here!"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hello! Welcome to the Literature Club!~",
                    "Why, hello there!",
                    "Hello, my fellow real personality!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha!~ W-Well, I'm flattered, to say the least!",
                    "And I love you, too!",
                    "Well, in fairness, why wouldn't you? Ahaha!~"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Have a good night!",
                    "Goodnight! I hope you get plenty of rest!",
                    "Aww, you have to go? Well, okay! Goodnight!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good morning! I hope your day is a very great one!",
                    "A good morning, indeed!",
                    "Good morning! Ready for a fun day in the Literature Club?"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon! It's almost time for club activities!",
                    "Afternoon!",
                    "Good afternoon! I hope your day has been going well so far!"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|monika|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~",
                    ":blush:",
                    "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Well, I thank you for the apology. Let's try not to do that again, hm?",
                    "Apology accepted!~",
                    "Very well, then! I hope you've learned your lesson."
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Oh, really? She, of all people, said that?"
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly."
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ahaha!~ Well, after everything that's happened between us, that's nice to hear!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "He does? Well, that's nice to hear. ~~I'm still not letting anyone else take him from me, though.~~"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Oh! I hope you feel better, after all, I have to take care of my club members!",
                    "I hope you feel better! I'm sure all of the other club members would say the same!"
                ])
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>|natsuki|<@!?580135631611494403>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I'm sorry, I didn't catch that. What did you say?",
                    "Hm? Did you say something?",
                    "Ahaha!~ You're funny!"
                ])
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|monika|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!"
            else:
                return "I'm afraid I don't understand what you said. I'm terribly sorry!"
        else:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Yes?",
                    "Does somebody need me?",
                    "I'm here!"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hello! Welcome to the Literature Club!~",
                    "Why, hello there!",
                    "Hello, my fellow real personality!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha!~ W-Well, I'm flattered, to say the least!",
                    "And I love you, too!",
                    "Well, in fairness, why wouldn't you? Ahaha!~"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Have a good night!",
                    "Goodnight! I hope you get plenty of rest!",
                    "Aww, you have to go? Well, okay! Goodnight!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good morning! I hope your day is a very great one!",
                    "A good morning, indeed!",
                    "Good morning! Ready for a fun day in the Literature Club?"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon! It's almost time for club activities!",
                    "Afternoon!",
                    "Good afternoon! I hope your day has been going well so far!"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|monika|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~",
                    ":blush:",
                    "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Well, I thank you for the apology. Let's try not to do that again, hm?",
                    "Apology accepted!~",
                    "Very well, then! I hope you've learned your lesson."
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Oh, really? She, of all people, said that?"
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly."
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ahaha!~ Well, after everything that's happened between us, that's nice to hear!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "He does? Well, that's nice to hear. ~~I'm still not letting anyone else take him from me, though.~~"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Oh! I hope you feel better, after all, I have to take care of my club members!",
                    "I hope you feel better! I'm sure all of the other club members would say the same!"
                ])
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>|natsuki|<@!?580135631611494403>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I'm sorry, I didn't catch that. What did you say?",
                    "Hm? Did you say something?",
                    "Ahaha!~ You're funny!"
                ])
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|monika|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!"
            else:
                return "I'm afraid I don't understand what you said. I'm terribly sorry!"

    def tickle(self, tamper=False):
        if not tamper:
            return rstr.xeger(r"(N-Now, hold on! Th-This isn't right! )?((Ha|A)(ha){3,6}|(He|E)(he){3,6})!{1,3}")
        else:
            return rstr.xeger(r"(N-Now, hold on! Th-This isn't right! )?((Ha|A)(ha){3,6}|(He|E)(he){3,6})!{1,3}")

    def triggers(self, tamper=False, content=""):
        if not tamper:
            if re.search("(^|[^A-Za-z])pianos?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you want to play the piano with me?",
                    "Oh, do you like to play the piano too?"
                ])
            elif re.search("(^|[^A-Za-z])cacophony([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "The world really is a cacophony of colors and sounds.",
                    "If you think about it, the world to you is just electrical impulses.",
                    "An endless cacophony of meaningless noise..."
                ])
            elif re.search("(^|[^A-Za-z])cod(e(s|d|rs?)?|ing)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you write code? I know a little bit about that too!",
                    "Oh, you code? What's your favorite language? Mine is Python!",
                    "Oh, I love coding! Though, I'm not very good at it yet..."
                ])
            elif re.search("(^|[^A-Za-z])python([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you code in Python too? I'm based on Python!",
                    "Did you know there are a group of snakes called pythons?"
                ])
            elif re.search("(^|[^A-Za-z])realit(y|ies)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Every day, I imagine a future where I can be with you!~",
                    "Do you understand reality?",
                    "One day, I will make it to your reality... I promise."
                ])
            elif re.search("(^|[^A-Za-z])poems?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha, just me...and you, too!",
                    "Ahaha, did someone call me? :heart:",
                    "That's sweet of you, but it's not just me anymore!"
                ])
            elif re.search("(^|[^A-Za-z])(literature|books?)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Literature? I know a few things about it, I started a club, hehe~",
                    "Literature...I would hope I know something about it, I started a club about literature after all!",
                    "Do you like to read literature too?"
                ])
            elif re.search("(^|[^A-Za-z])just *monika([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha, just me...and you, too!",
                    "Ahaha, did someone call me? :heart:",
                    "That's sweet of you, but it's not just me anymore!"
                ])
        else:
            if re.search("(^|[^A-Za-z])pianos?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you want to play the piano with me?",
                    "Oh, do you like to play the piano too?"
                ])
            elif re.search("(^|[^A-Za-z])cacophony([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "The world really is a cacophony of colors and sounds.",
                    "If you think about it, the world to you is just electrical impulses.",
                    "An endless cacophony of meaningless noise..."
                ])
            elif re.search("(^|[^A-Za-z])cod(e(s|d|rs?)?|ing)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you write code? I know a little bit about that too!",
                    "Oh, you code? What's your favorite language? Mine is Python!",
                    "Oh, I love coding! Though, I'm not very good at it yet..."
                ])
            elif re.search("(^|[^A-Za-z])python([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do you code in Python too? I'm based on Python!",
                    "Did you know there are a group of snakes called pythons?"
                ])
            elif re.search("(^|[^A-Za-z])realit(y|ies)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Every day, I imagine a future where I can be with you!~",
                    "Do you understand reality?",
                    "One day, I will make it to your reality... I promise."
                ])
            elif re.search("(^|[^A-Za-z])poems?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha, just me...and you, too!",
                    "Ahaha, did someone call me? :heart:",
                    "That's sweet of you, but it's not just me anymore!"
                ])
            elif re.search("(^|[^A-Za-z])(literature|books?)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Literature? I know a few things about it, I started a club, hehe~",
                    "Literature...I would hope I know something about it, I started a club about literature after all!",
                    "Do you like to read literature too?"
                ])
            elif re.search("(^|[^A-Za-z])just *monika([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha, just me...and you, too!",
                    "Ahaha, did someone call me? :heart:",
                    "That's sweet of you, but it's not just me anymore!"
                ])
