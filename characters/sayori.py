import random, re, rstr

class sayori():

    def __init__(self):
        self.color = "0x3eb0ff"
        self.description = "Sayori is a character in the game Doki Doki Literature Club, she is the vice president of the Literature Club founded by Monika and along with the other club members she spends her time after school in the club."
        self.id = 580133736721678341
        self.token = "NTgwMTMzNzM2NzIxNjc4MzQx.XqMmsw.IS8cOl_y0wCRk_7ftZt82usJ5j8"
        self.prefix = "(S|s)(ayori)?_"
        self.help = {
            "commands": {
                "ask [question]": "Ask Sayori anything you want to ask.",
                "changelog": "See the latest changes. (alias: log)",
                "debug": "View Sayori's statistics.",
                "feed [emote]": "Give Sayori food. (alias: eat)",
                "headpat": "Headpat Sayori. (alias: pat)",
                "help [about]": "Help about Sayori. (alias: manual)",
                "hug [person]": "Let Sayori hug someone.",
                "invite": "Invite Sayori to your server.",
                "jokes": "Sayori will tell you a funy joke. (alias: joke)",
                "lifeline": "If you feel suicidal, please let Sayori help.",
                "ping": "Get Sayori's heartbeat. (alias: doki)",
                "poems [poem name]": "Get Sayori's poems from the game. (alias: poem)",
                "quotes": "Get Sayori's quotes from the game. (alias: quote)",
                "shard": "Check which shard are you on for Sayori.",
                "swear": "Sayori will say a forbidden word.",
                "tamper": "Mess up or fix Sayori's personality.",
                "tickle": "Tickle Sayori.",
                "trigger": "Set triggers for Sayori on/off. (alias: triggers)"
            },
            "phrases": {
                "Hello": "Say hello to Sayori.",
                "Love": "Tell Sayori you or someone else loves him",
                "Good Morning": "Greet Sayori with a good morning.",
                "Good Night": "Greet Sayori with a good night.",
                "Good Afternoon": "Greet Sayori with a good afternoon.",
                "Compliment": "Give Sayori a compliment.",
                "Apologize": "Apologize to Sayori.",
                "Sick": "Tell Sayori when you are sick.",
                "Best Girl": "Tell Sayori who's the best girl."
            },
            "triggers": ["cinnamon bun", "breakfast", "hang", "kill"]
        }

    def playing(self):
        return [
            "Type 's_help' for help!",
            "Doki Doki Literature Club",
            "with the crayons!",
            "Katawa Shoujo",
            r"with Mr\. Cow!",
            "with a noose!"
        ]

    def ask(self, tamper=False, nothing=False):
        if not tamper:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(Yes|Of course( not)?|No|Maybe|Possibly)[!\.]"),
                    rstr.xeger(r"My vice president powers tell me '(yes|no|maybe)'!"),
                    rstr.xeger(r"(Yes|Of course( not)?|No), silly!"),
                    "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!",
                    "I'd say ask Yuri, but she's a little shy at the moment.",
                    "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!",
                    "You've got a better chance of having a happy ending in DDLC! Ehehe...~",
                    "Not really.",
                    "J-Just a little bit!",
                    "Maybe we should ask The Magic Conch, instead."
                ])
            else:
                return "I can't answer the question if you don't ask one, silly!"
        else:
            if not nothing:
                return random.choice([
                    rstr.xeger(r"(Yes|Of course( not)?|No|Maybe|Possibly)[!\.]"),
                    rstr.xeger(r"My vice president powers tell me '(yes|no|maybe)'!"),
                    rstr.xeger(r"(Yes|Of course( not)?|No), silly!"),
                    "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!",
                    "I'd say ask Yuri, but she's a little shy at the moment.",
                    "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!",
                    "You've got a better chance of having a happy ending in DDLC! Ehehe...~",
                    "Not really.",
                    "J-Just a little bit!",
                    "As sure as I'm depressed!"
                ])
            else:
                return "I can't answer the question if you don't ask one, silly!"
        return 

    def everyone(self):
        return "Nice try, you meanie."

    def feed(self, tamper=False, food=[], user=""):
        if not tamper:
            if not food:
                return "You wanna feed me something? I'm open for anything!"
            elif "cookie" in food:
                return "A cookie?? Yummy! Thank you so much!"
            elif "cupcake" in food:
                return "*omnomnom* Ooo! This tastes just like Natsuki's cupcakes!"
            elif "japanese" in food:
                return "Oooo! Japanese food! Reminds me of home!"
            elif "takeout" in food:
                return "Yay we're getting take out! I love watching a movie with some warm takeout!"
            elif "pizza" in food:
                return "I love pizza! Thanks!"
            elif "burger" in food:
                return "Mmmmm! Burgers are delicious!"
            elif "falafel" in food:
                return "*om nom nom* It's salty, but I like it."
            elif "ice" in food:
                return "Puts it in mouth  Oww.. It's too cold and it tastes like water!"
            elif "cold" in food:
                return "AHH! Brain freeze!!"
            elif "cold_drink" in food:
                return "Sip, sip, hooray!"
            elif "canned" in food:
                return "Canned food? Aww but I don't have a can opener."
            elif "alcohol" in food:
                return "H-Hey! I'm too young for that!"
            elif "coffee" in food:
                return "Ah, the delicious beverage known as coffee! Where would I be without thee?"
            elif "tea" in food:
                return "How could I refuse a hot cup of tea? Thank you!"
            elif "bread" in food:
                return "I mean, I suppose I could survive off of plain bread..."
            elif "sandwich" in food:
                return "Oh! is this for me? thanks I love sandwiches!"
            elif "waffle" in food:
                return "I've waffled before. I'll waffle again!!"
            elif "croissant" in food:
                return "yay! I love having these for breakfast!"
            elif "pastries" in food:
                return random.choice([
                    "Mmm this is really yummy but I bet Natsuki can make better ones!",
                    "Ooooo! I love these! thanks!"
                ])
            elif "butter" in food:
                return "Oooo, Butter! But... how am I supposed to eat it without some toast?"
            elif "pepper" in food:
                return "***OWOWOWOWHOTHOTHOTHOT!!!***"
            elif "cooking" in food:
                return "I made eggs and toast!"
            elif "mexican" in food:
                return "Ole!"
            elif "sweets" in food:
                return "Sweets! My one, true weakness!! *omnomnomnomnom*"
            elif "peanuts" in food:
                return "Ooo! peanuts! they always make me remember when MC and I went to the fair as kids!"
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "Hey! I'm not a baby!"
            elif "egg" in food:
                return "I feel like I should cook this, first..."
            elif "salt" in food:
                return "Sugar yay! ugh ptoo ugh yuck! this is salt isn't it? why would you do that meanie!"
            elif "silverware" in food:
                return "I didn't know you could eat silverware!"
            elif "bowl" in food:
                return "Hey! That bowl's empty you meanie!"
            elif "milk" in food:
                return "Ah, a nice, cold glass of milk is always welcoming!"
            elif "birthday_not" in food:
                return "It's not my birthday, but I accept!"
            elif "birthday" in food:
                return random.choice([
                    "om nom nom OOOO! Monika's birthday cake tastes incredibly delicious!!! :star_struck:",
                    "Oooo! Thanks I'll have piece of Monika's birthday cake! And I'll have another piece, of the one that Natsuki made eheheh~"
                ])
            elif "misc" in food:
                return "*om nom nom* Thank you! That was delicious! :grin:"
            else:
                return "Ptoo ptoo! This isn't food, you meanie!"
            
        else:
            
            if not food:
                return "You wanna feed me something? I'm open for anything!"
            elif "cookie" in food:
                return "A cookie?? Yummy! Thank you so much!"
            elif "cupcake" in food:
                return "*omnomnom* Ooo! This tastes just like Natsuki's cupcakes!"
            elif "japanese" in food:
                return "Oooo! Japanese food! Reminds me of home!"
            elif "takeout" in food:
                return "Yay we're getting take out! I love watching a movie with some warm takeout!"
            elif "pizza" in food:
                return "I love pizza! Thanks!"
            elif "burger" in food:
                return "Mmmmm! Burgers are delicious!"
            elif "falafel" in food:
                return "*om nom nom* It's salty, but I like it."
            elif "ice" in food:
                return "Puts it in mouth  Oww.. It's too cold and it tastes like water!"
            elif "cold" in food:
                return "AHH! Brain freeze!!"
            elif "cold_drink" in food:
                return "Sip, sip, hooray!"
            elif "canned" in food:
                return "Canned food? Aww but I don't have a can opener."
            elif "alcohol" in food:
                return "H-Hey! I'm too young for that!"
            elif "coffee" in food:
                return "Ah, the delicious beverage known as coffee! Where would I be without thee?"
            elif "tea" in food:
                return "How could I refuse a hot cup of tea? Thank you!"
            elif "bread" in food:
                return "I mean, I suppose I could survive off of plain bread..."
            elif "sandwich" in food:
                return "Oh! is this for me? thanks I love sandwiches!"
            elif "waffle" in food:
                return "I've waffled before. I'll waffle again!!"
            elif "croissant" in food:
                return "yay! I love having these for breakfast!"
            elif "pastries" in food:
                return random.choice([
                    "Mmm this is really yummy but I bet Natsuki can make better ones!",
                    "Ooooo! I love these! thanks!"
                ])
            elif "butter" in food:
                return "Oooo, Butter! But... how am I supposed to eat it without some toast?"
            elif "pepper" in food:
                return "***OWOWOWOWHOTHOTHOTHOT!!!***"
            elif "cooking" in food:
                return "I made eggs and toast!"
            elif "mexican" in food:
                return "Ole!"
            elif "sweets" in food:
                return "Sweets! My one, true weakness!! *omnomnomnomnom*"
            elif "peanuts" in food:
                return "Ooo! peanuts! they always make me remember when MC and I went to the fair as kids!"
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "Hey! I'm not a baby!"
            elif "egg" in food:
                return "I feel like I should cook this, first..."
            elif "salt" in food:
                return "Sugar yay! ugh ptoo ugh yuck! this is salt isn't it? why would you do that meanie!"
            elif "silverware" in food:
                return "I didn't know you could eat silverware!"
            elif "bowl" in food:
                return "Hey! That bowl's empty you meanie!"
            elif "milk" in food:
                return "Ah, a nice, cold glass of milk is always welcoming!"
            elif "birthday_not" in food:
                return "It's not my birthday, but I accept!"
            elif "birthday" in food:
                return random.choice([
                    "om nom nom OOOO! Monika's birthday cake tastes incredibly delicious!!! :star_struck:",
                    "Oooo! Thanks I'll have piece of Monika's birthday cake! And I'll have another piece, of the one that Natsuki made eheheh~"
                ])
            elif "misc" in food:
                return "*om nom nom* Thank you! That was delicious! :grin:"
            else:
                return "Ptoo ptoo! This isn't food, you meanie!"

        return

    def headpat(self, tamper=False):
        if not tamper:
            return random.choice([
                "Hehehe!~", "Just don't mess up my bow!",
                "S-stop being so silly! :blush:",
                "Well, my hair's already pretty messy, so I don't see an issue!",
                "Hehehe! Thank you!"
            ])
        else:
            return random.choice([
                "Hehehe!~", "Just don't mess up my bow!",
                "S-stop being so silly! :blush:",
                "Well, my hair's already pretty messy, so I don't see an issue!",
                "Hehehe! Thank you!"
            ])
        return

    def hug(self, tamper=False, target="", targetName=""):
        if not tamper:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"One hug, coming right up! *hugs {targetName}*",
                    f"I'll try not to squeeze too hard! *hugs {targetName}*",
                    f"Time for the super-mega-cinnamon-bun hug! *hugs {targetName}*",
                    f"How could I say no to a hug? *hugs {targetName}*",
                    f"Yay, hugs! *hugs {targetName}*"
                ])
            elif target == "self":
                return random.choice([
                    "A hug for me? Yay! *hugs myself*",
                    "Well, if you insist! *hugs myself*",
                    "Awww, you're too kind! *hugs myself*",
                    "How can I say no to that? *hugs myself*"
                ])
        else:
            if not target or target == "mc" or target == "player":
                return random.choice([
                    f"One hug, coming right up! *hugs {targetName}*",
                    f"I'll try not to squeeze too hard! *hugs {targetName}*",
                    f"Time for the super-mega-cinnamon-bun hug! *hugs {targetName}*",
                    f"How could I say no to a hug? *hugs {targetName}*",
                    f"Yay, hugs! *hugs {targetName}*"
                ])
            elif target == "self":
                return random.choice([
                    "A hug for me? Yay! *hugs myself*",
                    "Well, if you insist! *hugs myself*",
                    "Awww, you're too kind! *hugs myself*",
                    "How can I say no to that? *hugs myself*"
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
                    return f"Ehehe! I love your hugs, Monika! You should give them more often!"
                if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in content.lower():
                    return "Hey, everyone deserves forgiveness! Even you, Monika!"
            elif message.author.id == sayoriID:
                return
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aww, thank you, Yuri!"
                if "h-hey! Don't hug so hard, Sayori!" in content.lower():
                    return "Oops! I'm sorry!"
                if "haha. well, she is a loving soul." in content.lower():
                    return "You bet your booty I am! :yum:"
                if "who the hell is sayori? i don't know any sayoris..." in content.lower():
                    return "Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!"
                if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in content.lower():
                    return ":disappointed_relieved: :cold_sweat: :confounded: :sob:"
                if "i'm sorry, who are you? and why are you hugging me?" in content.lower():
                    return "I-It's me, Sayori! And I-I just wanted to hug you!"
                if "sorry, but i don't know you. please get your messy, stupid self away from me." in content.lower():
                    return "O-Okay... I'm sorry... :pensive:"
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Hehehe! You give the best hugs, Natsuki!"
                if "s-shut up! no she doesn't!" in content.lower():
                    return "Oh, yes I do!"
                if "s-shut up! no, i don't!" in content.lower():
                    return "Awww... :("
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Aww you're such a sweetheart, <@{mcID}>"
                if "finnnnnnne, sayori." in content.lower():
                    return f"YAY! *keeps hugging <@{mcID}>*"
                if f"<@{bot.user.id}>" in content.lower():
                    return f"Yes, <@{mcID}>?"
                if "i-i love you, sayori" in content.lower():
                    return f"I-I do too! *hugs MC*"
        else:
            if message.author.id == monikaID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Ehehe! I love your hugs, Monika! You should give them more often!"
                if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in content.lower():
                    return "Hey, everyone deserves forgiveness! Even you, Monika!"
            elif message.author.id == sayoriID:
                return
            elif message.author.id == yuriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Aww, thank you, Yuri!"
                if "h-hey! Don't hug so hard, Sayori!" in content.lower():
                    return "Oops! I'm sorry!"
                if "haha. well, she is a loving soul." in content.lower():
                    return "You bet your booty I am! :yum:"
                if "who the hell is sayori? i don't know any sayoris..." in content.lower():
                    return "Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!"
                if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in content.lower():
                    return ":disappointed_relieved: :cold_sweat: :confounded: :sob:"
                if "i'm sorry, who are you? and why are you hugging me?" in content.lower():
                    return "I-It's me, Sayori! And I-I just wanted to hug you!"
                if "sorry, but i don't know you. please get your messy, stupid self away from me." in content.lower():
                    return "O-Okay... I'm sorry... :pensive:"
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Hehehe! You give the best hugs, Natsuki!"
                if "s-shut up! no she doesn't!" in content.lower():
                    return "Oh, yes I do!"
                if "s-shut up! no, i don't!" in content.lower():
                    return "Awww... :("
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Aww you're such a sweetheart, <@{mcID}>"
                if "finnnnnnne, sayori." in content.lower():
                    return f"YAY! *keeps hugging <@{mcID}>*"
                if f"<@{bot.user.id}>" in content.lower():
                    return f"Yes, <@{mcID}>?*"
                if "i-i love you, sayori" in content.lower():
                    return f"I-I do too! *hugs MC*"

    def jokes(self):
        return random.choice([
            "What do you call a mix between a fish and an elephant? Swimming trunks!",
            "I was going to tell a joke about a skunk, but, honestly, it really stinks.",
            "Why did the rooster cross the road? To prove he wasn't a chicken!",
            "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
            "I have severe depression. That's not a joke, it's a cry for help.",
            "My life. Ehehe...~",
            "What do you get when you cross an author and an alcoholic? Ernest Hemmingway!",
            "What do you call fake spaghetti? An im-pasta!",
            "Why don't cannibals eat clowns? Because they taste funny...",
            "What do you call a bird that sticks to everything? A vel-crow!",
            "What do you call a sleepwalking nun? A Roamin' Catholic!",
            "What's brown and sticky? A stick!",
            "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.",
            "How many tickles does it take to make an octopus laugh? Ten tickles!",
            "Why do stadiums get hot after games? All the fans left!",
            "What do attorneys wear to court? Lawsuits!",
            "Why are there gates around cemeteries? Everyone is dying to get in!",
            "Why did the baby strawberry cry? His parents were in a jam!",
            "I was gonna tell a joke about a broken pencil, but it's pointless.",
            "The past, present, and future walk into a bar. It was tense.",
            "How do you comfort the Grammar Police? \"There, they're, their...\"",
            "Is there a word in the English language that uses all 5 vowels, as well as 'y'? Unquestionably!",
            "Once, I was spacing out in class and my English teacher asked me to name two pronouns. Not sure who she was talking to, I replied, \"Who, me?\"",
            "Why do writers feel so cold? They're surrounded by drafts!",
            "A man went into a library and asked for a book on how to commit suicide. The librarian replies, \"Why would I give you that? You won't return it!\"",
            "\"I'm sorry\" and \"I apologize\" mean the same thing. Unless you're at a funeral.",
            "A dyslexic man walks into a bra...",
            "What does cement and MC have in common? They both can be dense.",
            "I asked Yuri if I can have a book-mark, and she said her name is Yuri.",
            "I should probably clean my room's windows. But privacy is important too.",
            "I used think that the brain was the most important organ. But then I thought, hey, look how's telling me that.",
            "Why did the dinosaur cross the road? Because the chicken hasn't evolved yet.",
            "I told MC he should embrace his mistakes. He laughed, then he gave me a quick hug."
        ])

    def lifeline(self):
        return "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"

    def poems(self, tamper=False, name=""):

        if not tamper:
            poem1 = [
                "Dear Sunshine",
                "The way you glow through my blinds in the morning\nIt makes me feel like you missed me.\nKissing my forehead to help me out of bed.\nMaking me rub the sleepy from my eyes.\n\nAre you asking me to come out and play?\nAre you trusting me to wish away a rainy day?\nI look above. The sky is blue.\nIt's a secret, but I trust you too.\n\nIf it wasn't for you, I could sleep forever.\nBut I'm not mad.\n\nI want breakfast."
            ]
            poem2 = [
                "Bottles",
                "I pop off my scalp like the lid of a cookie jar.\nIt's the secret place where I keep all my dreams.\nLittle balls of sunshine, all rubbing together like a bundle of kittens.\nI reach inside with my thumb and forefinger and pluck one out.\nIt's warm and tingly.\nBut there's no time to waste! I put it in a bottle to keep it safe.\nAnd I put the bottle on the shelf with all of the other bottles.\nHappy thoughts, happy thoughts, happy thoughts in bottles, all in a row.\n\nMy collection makes me lots of friends.\nEach bottle a starlight to make amends.\nSometimes my friend feels a certain way.\nDown comes a bottle to save the day.\n\nNight after night, more dreams.\nFriend after friend, more bottles.\nDeeper and deeper my fingers go.\nLike exploring a dark cave, discovering the secrets hiding in the nooks and crannies.\nDigging and digging.\nScraping and scraping.\n\nI blow dust off my bottle caps.\nIt doesn't feel like time elapsed.\nMy empty shelf could use some more.\nMy friends look through my locked front door.\n\nFinally, all done. I open up, and in come my friends.\nIn they come, in such a hurry. Do they want my bottles that much?\nI frantically pull them from the shelf, one after the other.\nHolding them out to each and every friend.\nEach and every bottle.\nBut every time I let one go, it shatters against the tile between my feet.\nHappy thoughts, happy thoughts, happy thoughts in shards, all over the floor.\n\nThey were supposed to be for my friends, my friends who aren't smiling.\nThey're all shouting, pleading. Something.\nBut all I hear is echo, echo, echo, echo, echo\nInside my head."
            ]
            if name.lower() == "dear sunshine":
                return poem1
            elif name.lower() == "bottles":
                return poem2
            else:
                return random.choice([poem1,poem2])
        else:
            return ["","Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of\nGet.\nOut.\nOf.\nMy.\nHead.\n\n\nGet out of my head before I do what I know is best for you.\nGet out of my head before I listen to everything she said to me.\nGet out of my head before I show you how much I love you.\nGet out of my head before I finish writing this poem.\n\n\n\nBut a poem is never actually finished.\nIt just stops moving."]

    def quotes(self):
        return random.choice([
            "I want breakfast.",
            "AAAAAaaaaAAAAAAAAHH!!!!",
            "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head",
            "I made eggs and toast!",
            "It's bad to skip breakfast! I get all cranky...",
            "I was playing with the crayons and smacked my forehead into the shelf!",
            "Yuri's boobs are just as they've always been! Big and beautiful!",
            "I did something bad, and now I have to accept the revolution!",
            "This isn't the napping club!",
            "I'm fine with--looking like a unicorn--",
            "So, if I keep it unbuttoned then I won't get a boyfriend, right?"
        ])

    def swear(self):
        return random.choice([
            "HECK!",
            "DARN IT!",
            "POOP!",
            "CRUD!",
            "FRICK!",
            "SON OF A BISCUIT!",
            "MOTHERTRUCKER!"
        ])

    def tagging(self, tamper=False, content=""):
        if not tamper:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "You rang?",
                    "Are you guys talking about me?"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi!",
                    "Hello!",
                    "Hiiiiii!~",
                    "Hello, human person!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Aww! I love you too!",
                    "Thank you so much!~",
                    "I love you too! :smile:",
                    ":blush:",
                    "I don't really deserve your love, but I'm flattered, anyway!"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Goodnight! Sleep tight! Don't let the bedbugs bite!~",
                    "Nighty night!~",
                    "Sleep well!",
                    "Goodnight!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good morning! I hope you slept well!~",
                    "Morning, everyone!",
                    "Goooooooood morning!~",
                    "Morning, Sunshine!~"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    rstr.xeger(r"Good afternoon(, indeed)?!"),
                    "Afternoon?? Shoot! I'm late for school again!",
                    "Afternoon!"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|sayori|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Awww! Thank you so much! :blush:",
                    "I know you are, but what am I? :stuck_out_tongue_closed_eyes:",
                    "Y-You really think so? Aww!~",
                    "How sweet! Thank you so much!"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "It's okay; I forgive you!",
                    "Well, alright. As long as you promise to behave yourself!",
                    "Thank you for apologizing!",
                    "Okay. Just try not to do it again!"
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Awww, she does??"
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, of course she does! Yuri loves everybody!"
            elif re.search(f"(^|[^A-Za-z])(sayori|<@!?{self.id}>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Yay! I'm glad she does!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Yay! My best friend loves me!!! :heart:"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Don't worry! I'm sure you'll feel better soon!",
                    "Aww... get plenty of rest, and eat a lot of healthy foods!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|natsuki|<@!?580135631611494403>|yuri|<@!?580134475250532352>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, I respect your opinion!"
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|sayori|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "S-Stop it! That's not true!"
            else:
                return random.choice([
                    "Huh? I don't understand.",
                    "I don't get it.", "???",
                    "Maybe try something I actually understand?"
                ])
        else:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "You rang?",
                    "Are you guys talking about me?"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hi!",
                    "Hello!",
                    "Hiiiiii!~",
                    "Hello, human person!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Aww! I love you too!",
                    "Thank you so much!~",
                    "I love you too! :smile:",
                    ":blush:",
                    "I don't really deserve your love, but I'm flattered, anyway!"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Goodnight! Sleep tight! Don't let the bedbugs bite!~",
                    "Nighty night!~",
                    "Sleep well!",
                    "Goodnight!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good morning! I hope you slept well!~",
                    "Morning, everyone!",
                    "Goooooooood morning!~",
                    "Morning, Sunshine!~"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    rstr.xeger(r"Good afternoon(, indeed)?!"),
                    "Afternoon?? Shoot! I'm late for school again!",
                    "Afternoon!"
                ])
            elif re.search(f"(^|[^A-Za-z])((^|sayori|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Awww! Thank you so much! :blush:",
                    "I know you are, but what am I? :stuck_out_tongue_closed_eyes:",
                    "Y-You really think so? Aww!~",
                    "How sweet! Thank you so much!"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "It's okay; I forgive you!",
                    "Well, alright. As long as you promise to behave yourself!",
                    "Thank you for apologizing!",
                    "Okay. Just try not to do it again!"
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Awww, she does??"
            elif re.search("(^|[^A-Za-z])(yuri|<@!?580134475250532352>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, of course she does! Yuri loves everybody!"
            elif re.search(f"(^|[^A-Za-z])(sayori|<@!?{self.id}>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Yay! I'm glad she does!"
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Yay! My best friend loves me!!! :heart:"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Don't worry! I'm sure you'll feel better soon!",
                    "Aww... get plenty of rest, and eat a lot of healthy foods!"
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|natsuki|<@!?580135631611494403>|yuri|<@!?580134475250532352>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Well, I respect your opinion!"
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|sayori|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "S-Stop it! That's not true!"
            else:
                return random.choice([
                    "Huh? I don't understand.",
                    "I don't get it.", "???",
                    "Maybe try something I actually understand?"
                ])

    def tickle(self, tamper=False):
        if not tamper:
            return random.choice([
                "*giggles*",
                rstr.xeger(r"\*\*(PFFFT )?(W?A)?(HAH?){9,11}!{3,5}~?\*\*"),
                rstr.xeger(r"((Ha|A)(ha){3,6}|(He|E)(he){3,6})!{1,3}~?")
            ])
        else:
            return random.choice([
                "*giggles*",
                rstr.xeger(r"\*\*(PFFFT )?(W?A)?(HAH?){9,11}!{3,5}~?\*\*"),
                rstr.xeger(r"((Ha|A)(ha){3,6}|(He|E)(he){3,6})!{1,3}~?")
            ])

    def triggers(self, tamper=False, content=""):
        if not tamper:
            if re.search("(^|[^A-Za-z])cinnamon *bun([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "You rang?",
                    "Are you guys talking about me?"
                ])
            elif re.search("(^|[^A-Za-z])breakfasts?([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I want breakfast"
            elif re.search("(^|[^A-Za-z])(h(a|u)ng(s|ing|ed)?|kill(s|ing|ed)?) *(my)?self([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!",
                    "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!",
                    "Listen, I've been where you are. You'll get through it, I promise.",
                    "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"
                ])
            elif re.search("(^|[^A-Za-z])h(a|u)ng(s|ing|ed)?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    ":unamused:",
                    "Hey! Stop acting like a meanie!",
                    ":rolling_eyes:",
                    "I thought we were better than this...",
                    "Ha, ha. Funny. Can you sense my sarcasm?"
                ])
            elif re.search("(^|[^A-Za-z])kill(s|ing|ed)?([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Can we change the topic to something more wholesome please?"
            elif re.search("(^|[^A-Za-z])(mean(y|ies?)|bull(y|i|ies))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do we have a meanie in the server? If so, please stop.",
                    "Cease your bulli, you meanie!",
                    "Boo! You meanie..."
                ])
        else:
            if re.search("(^|[^A-Za-z])cinnamon *bun([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Did someone mention me?",
                    "You rang?",
                    "Are you guys talking about me?"
                ])
            elif re.search("(^|[^A-Za-z])breakfasts?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I want breakfast"
                ])
            elif re.search("(^|[^A-Za-z])(h(a|u)ng(s|ing|ed)?|kill(s|ing|ed)?) *(my)?self([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!",
                    "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!",
                    "Listen, I've been where you are. You'll get through it, I promise.",
                    "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"
                ])
            elif re.search("(^|[^A-Za-z])h(a|u)ng(s|ing|ed)?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    ":unamused:",
                    "Hey! Stop acting like a meanie!",
                    ":rolling_eyes:",
                    "I thought we were better than this...",
                    "Ha, ha. Funny. Can you sense my sarcasm?"
                ])
            elif re.search("(^|[^A-Za-z])kill(s|ing|ed)?([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Can we change the topic to something more wholesome please?"
            elif re.search("(^|[^A-Za-z])(mean(y|ies?)|bull(y|i|ies))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Do we have a meanie in the server? If so, please stop.",
                    "Cease your bulli, you meanie!",
                    "Boo! You meanie..."
                ])

    def welcome(self, tamper=False, member=False):
        if not tamper and member:
            return rstr.xeger(r"Everyone! (The n|We have a n|N)ew member,? " + member + r", (is here|just joined)~?!( Ehehehe~)?e~")
        elif member:
            return f"{member} Welcome... I guess, what's the point of even joining when this club is failing..."
        return