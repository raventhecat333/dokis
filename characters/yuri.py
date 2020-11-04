import discord, random, re, rstr

class yuri():

    def __init__(self):
        self.color = "0x8524c8"
        self.description = "Yuri is a character in the game Doki Doki Literature Club, she is a member of the Literature Club and along with her club members she spends her time after school in the club."
        self.id = 580134475250532352
        self.token = "NTgwMTM0NDc1MjUwNTMyMzUy.XqMmvg.14y3YKHmImXlvYoRhVut1Xf_hok"
        self.prefix = "(Y|y)(uri)?_"
        self.help = {
            "commands": {
                "ask [question]": "Ask Yuri anything you want to ask.",
                "changelog": "See the latest changes. (alias: log)",
                "debug": "View Yuri's statistics.",
                "feed [emote]": "Give Yuri food. (alias: eat)",
                "headpat": "Headpat Yuri. (alias: pat)",
                "help [about]": "Help about Yuri. (alias: manual)",
                "hug [person]": "Let Yuri hug someone.",
                "invite": "Invite Yuri to your server.",
                "ping": "Get Yuri's heartbeat. (alias: doki)",
                "poems [poem name]": "Get Yuri's poems from the game. (alias: poem)",
                "quotes": "Get Yuri's quotes from the game. (alias: quote)",
                "shard": "Check which shard are you on for Yuri.",
                "tamper": "Mess up or fix Yuri's personality.",
                "tickle": "Tickle Yuri.",
                "trigger": "Set triggers for Yuri on/off. (alias: triggers)"
            },
            "phrases": {
                "Hello": "Say hello to Yuri.",
                "Love": "Tell Yuri you or someone else loves him",
                "Good Morning": "Greet Yuri with a good morning.",
                "Good Night": "Greet Yuri with a good night.",
                "Good Afternoon": "Greet Yuri with a good afternoon.",
                "Compliment": "Give Yuri a compliment.",
                "Apologize": "Apologize to Yuri.",
                "Sick": "Tell Yuri when you are sick.",
                "Best Girl": "Tell Yuri who's the best girl."
            },
            "triggers": ["cut", "knife", "pen"]
        }

    def playing(self):
        return [
            "Type 'y_help' for help!",
            "Doki Doki Literature Club",
            "with knifes!",
            "Everlasting Summer",
            "Yandere Simulator",
            "with your pen!"
        ]

    def ask(self, tamper=False, nothing=False):
        if not tamper:
            if not nothing:
                return random.choice([
                    "Y-Yes.",
                    "No...",
                    "I'm not really sure.",
                    "I don't believe so...",
                    "I think that's a question best suited for Sayori.",
                    "Perhaps Monika could be of better help?",
                    "I-I don't know. I'm sorry...",
                    "Natsuki might know.",
                    "I believe so!"
                ])
            else:
                return "Did you want to ask me something? S-sorry if I was bothering you! Uuu..."
        else:
            if not nothing:
                return random.choice([
                    "Yes.",
                    "I don't know, and I don't care. I just want to look at you...",
                    "No.",
                    "Possibly, but who knows?",
                    "Meet me in the closet and we'll find out... :kissing_closed_eyes:",
                    "Ahaha! You're so silly to ask such a question!",
                    "I'm not sure... I'll think about it while I'm touching myself to you tonight."
                ])
            else:
                return "Ahaha... If you don't have a question, that's okay. I'd rather stare at you."
        return 

    def everyone(self):
        return "Hey! Do you **WANT** everyone to freak out in the chat?! Because I won't let you do that!"

    def feed(self, tamper=False, food=[], user=""):
        if not tamper:
            if not food:
                return "Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~."
            elif "cookie" in food:
                return "Oh, the chocolate chips just melt in my mouth!"
            elif "cupcake" in food:
                return "T-Thank you, *slowly bites* Oh.. It tastes almost as good as Natsuki's cupcakes."
            elif "japanese" in food:
                return "Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things..."
            elif "takeout" in food:
                return "Takeout boxes always been my favorite kind of fast food... It helps me feel real relaxed and claim plus they're more enjoyable when I watch movies."
            elif "pizza" in food:
                return "A slice of pizza never hurt, right...?"
            elif "burger" in food:
                return "Fast food? I-I suppose that'll do."
            elif "falafel" in food:
                return "Egyptian meal, huh? Uu, well I not sure if it's healthy to eat something that's not very common in other countries, but it's from Egypt so.. I'll give it a try."
            elif "ice" in food:
                return "I feel like... you're trying to make a reference here."
            elif "cold" in food:
                return "Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination."
            elif "cold_drink" in food:
                return "I predict a brain freeze in my near future."
            elif "canned" in food:
                return "T-Thank you, but I'm not quite sure how to open it without a can opener."
            elif "wine" in food:
                return "Ah wine, that reminds me when I brought wine to the club once. Anyways if you want to give me wine you need to take me on a date first."
            elif "alcohol" in food:
                return "T-Thank you, but I'll have to kindly decline."
            elif "coffee" in food:
                return "I-I'm more of a tea drinker. I'm sorry..."
            elif "tea" in food:
                return "Ah, thank you so much. All I need now is a good book."
            elif "bread" in food:
                return "Hm... I suppose I need more ingredients than this, don't you think?"
            elif "sandwich" in food:
                return "I believe that all anyone really wants in this life, is to sit in peace and eat a sandwich."
            elif "waffle" in food:
                return "W-Waffle? I hope it tastes good with some tea..."
            elif "croissant" in food:
                return "Thank you, these go  really well with tea"
            elif "pastries" in food:
                return "T-This pastries tastes delicious, thank you... Did you make them yourself?"
            elif "butter" in food:
                return "I-I'm not sure.. why you're giving me this butter... but I'll save it for later."
            elif "pepper" in food:
                return "O-Oh! Oh my goodness! That has quite a kick!!"
            elif "cooking" in food:
                return "Oh, I didn't know you knew how to cook eggs!"
            elif "mexican" in food:
                return "Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?"
            elif "chocolate" in food:
                return "Oh! This brings up some... memories... with MC..."
            elif "sweets" in food:
                return "I suppose a sweet wouldn't be such a bad idea..."
            elif "nuts" in food:
                return "Nuts? Do you know that nuts are indisapensable for cardiovascular health?? The protective properties of nuts against coronary heart disease were first recognized in early 1990s, and strong body of literature has followed, confirming these original findings. Oh...uuuu, I'm sorry, I should just stop talking, shouldn't I?"
            elif "popcorn" in food:
                return "*crunch crunch crunch*"
            elif "baby" in food:
                return "I-I'm not sure what you're insinuating, b-but I don't have a need for th-that..."
            elif "egg" in food:
                return "Oh, is it hard-boiled? Oh... no, it's not..."
            elif "salt" in food:
                return "I-I don't understand, why you're giving me salt?"
            elif "silverware" in food:
                return "Ah, I'm generally used to chopsticks, but silverware will suffice."
            elif "bowl" in food:
                return "O-Oh... I'm afraid that bowl is empty..."
            elif "milk" in food:
                return "Th-Thank you. I love a nice glass of milk."
            elif "birthday_not" in food:
                return "Oh, I-I'm sorry, but you must be confused; it's not my birthday..."
            elif "birthday" in food:
                return random.choice([
                    "O-Oh, umm.. T-Thanks for sharing the birthday cake with me, I-I also have already made some tea for everyone, since I'm sure some warm oolong will go well with the cake.",
                    "*munch munch* O-Oh that's definitely one of the best cakes I ever had."
                ])
            elif "misc" in food:
                return "Oh, you didn't really have to, but thank you so much. *munch munch*"
            else:
                return "Uuuu!! Th-that's not food!"
            
        else:
            
            if not food:
                return "I'll eat anything you like, Darling. Anything."
            elif "alcohol" in food:
                return "I'll drink it because you want me to, my love! *chugs*"
            elif "tea" in food:
                return "ou know. I love drinking tea, but not as much as I love you! **HAHAHA~**"
            elif "baby" in food:
                return "Oh, are you into that kind of thing? Well, I'll happily play along for you. Wah! Waah!"
            elif "egg" in food:
                return "Uhuhuhu! Raw eggs? Now you're just being silly, but I'll still accept!"
            elif "silverware" in food:
                return "Well, I'll admit that it wasn't as disgusting as I had originally assumed!"
            elif "birthday_not" in food:
                return "It's not my birthday, but I'll still eat this cake!"
            elif "birthday" in food:
                return "Do you think I give a shit, about that evil bitch's birthday?"
            elif "eggplant" in food:
                return "Mmmm.... I wish this was your long, hard cock... :smirk: I can shove it all the way down my throat, if you'd like..."
            elif "peach" in food:
                return "It's so sweet and juicy... I just wanna lick all the juices up!"
            elif "pen" in food:
                return "Oh, I do believe this is the one with my juices on it. *licks* Mmm... Tasty..."
            elif "knife" in food:
                return "Mmmm.... I just wanna rub the blade across my tongue and taste the blood... Maybe I could let you taste it, as well..."
            else:
                return "*munch munch munch* Does that please you, my beloved?"

        return

    def headpat(self, tamper=False):
        if not tamper:
            return random.choice([
                "Mmm... :relaxed:",
                "Oh... I'm not sure how to feel about that...",
                "H-Hey, could you be a little more gentle, please?",
                "That feels rather nice...",
                "T-Thank you."
            ])
        else:
            return random.choice([
                "Oh, only my head is being pat? Shame.",
                "Huhuhu. I love it when you do cute things like that to me!",
                "Mmm... You know what would be better? If you moved that hand somewhere else...",
                "Oh, am I your dog or something? That's okay. I'll be anything you want me to be, my love."
            ])
        return
    
    def hug(self, tamper=False, target="", targetName=""):
        if not tamper:
            if not target or target == "mc":
                return random.choice([
                    f"Y-you want me to hug them? Well, o-okay, I guess I can do that for you... *hugs {targetName}*",
                    f"Just let me know if this is too much for you... *hugs {targetName}*",
                    f"*hugs {targetName}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"
                ])
            elif target == "player":
                return random.choice([
                    f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs {targetName}*",
                    f"Just let me know if this is too much for you... *hugs {targetName}*",
                    f"*hugs {targetName}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"
                ])
            elif target == "self":
                return random.choice([
                    "What? O-Okay, I suppose... *hugs myself*",
                    "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"
                ])
        else:
            if not target or target == "mc":
                return "No. I refuse to hug anyone other than you."
            elif target == "player":
                return random.choice([
                    f"*hugs {targetName}* Ahaha... I could hug you forever...!",
                    f"Oh, you have no idea how long I've been waiting for you to say that!! *hugs {targetName}*",
                    f"*hugs {targetName}* Mmm... You smell so wonderful! I wish I could smell this smell forever!",
                    f"Uhuhu... You can even grab my ass while we hug if you wanted. I don't mind ;) *hugs {targetName}*",
                    f"*hugs {targetName}* Oh, you're pressing hard against my chest. I must say, I really, really love it!"
                ])
            elif target == "self":
                return "But I don't ***want*** to hug myself! I want to hug ***YOU!!!***"
            elif target == "mc":
                return f"Hey {targetName}, get your sexy body over here and fuck me~"

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
                    return f"O-Oh! Well, uh, thank you, Monika."
                if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in content.lower():
                    return "Uuu... :flushed:"
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"H-Hey! Don't hug so hard, Sayori!"
                if "aww thank you, yuri!" in content.lower():
                    return "Y-You're welcome, Sayori."
                if "well, of course she does! yuri loves everybody!" in content.lower():
                    return "S-Sayori! You didn't have to say it like that..."
            elif message.author.id == yuriID:
                return
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Oh! Well, that was certainly unexpected!"
                if "geez, yuri! don't make it all awkward!" in content.lower():
                    return "I'm sorry..."
                if "w-well it's not like i love her back or anything!!" in content.lower():
                    return "Oh... I see..."
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Augh!"
                if "i-i love you, yuri." in content.lower():
                    return "*tackle hugs MC*"
        else:
            if message.author.id == monikaID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"Get your dirty, selfish hands off of me before I kill you and take your spot as President!!"
                if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in content.lower():
                    return "Except that I don't love you, sooo..."
                if "y_tamper" in content.lower():
                    bot.globalCursor.execute(f"DELETE FROM tampered WHERE bot = '{bot.name}' AND type = 'guild' AND id = {message.guild.id}")
                    bot.globalConnection.commit()
                    return discord.Embed(title = f'{bot.name} got fixed!',color=int(self.color, base=16))
            elif message.author.id == sayoriID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"I'm sorry, who are you? And why are you hugging me?"
                if "well, of course she does! yuri loves everybody!" in content.lower():
                    return "No, I don't. In fact, I hate most people."
                if "yuri, it's me! sayori! your friend and vice president of the literature club!" in content.lower():
                    return "What the fuck?? ***I'M*** the Vice President, you stupid bitch! And I'm no friend of yours!!"
                if "i-it's me, sayori! and i-i just wanted to hug you!" in content.lower():
                    return "Sorry, but I don't know you. Please get your messy, stupid self away from me."
            elif message.author.id == yuriID:
                return
            elif message.author.id == natsukiID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return "Get your fucking hands off of me!!"
                if "w-well it's not like i love her back or anything!!" in content.lower():
                    return "No shocker there, you selfish bitch!"
                if "what the hell?? yuri, why would you say something so mean??" in content.lower():
                    return "Because it's the fucking truth, you little bitch!!"
            elif message.author.id == mcID:
                if re.search(r"\*hugs <@!?{0}>\*".format(bot.user.id), content, re.IGNORECASE):
                    return f"That's right <@{mcID}>, let me feel your pulsating cock on my pussy."
                if "y_tamper" in content.lower():
                    bot.globalCursor.execute(f"DELETE FROM tampered WHERE bot = '{bot.name}' AND type = 'guild' AND id = {message.guild.id}")
                    bot.globalConnection.commit()
                    return discord.Embed(title = f'{bot.name} got fixed!',color=int(self.color, base=16))
                if "fuck no, get away from me, yuri." in content.lower():
                    return "Then I'll stab you and crawl in your skin."    
                if "i-i love you, yuri." in content.lower():
                    return f"I love you too, you sexy <@{mcID}>! Now fuck me!!! :smirk:"
                if "you're going to stab them to death if they try, aren't you?" in content.lower():
                    return "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"

    def poems(self, tamper=False, name=""):

        if not tamper:
            poem1 = [
                "Ghost under the light",
                "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIt must be this one.\nThe last remaining streetlight to have withstood the test of time.\nThe last yet to be replaced by the sickening blue-green of the future.\nI bathe. Calm; breathing air of the present but living in the past.\nThe light flickers.\nI flicker back."
            ]
            poem2 = [
                "The Raccoon",
                "It happened in the dead of night while I was slicing bread for a guilty snack.\nMy attention was caught by the scuttering of a raccoon outside my window.\nThat was, I believe, the first time I noticed my strange tendencies as an unusual\nhuman.\nI gave the raccoon a piece of bread, my subconscious well aware of the consequences.\nWell aware that a raccoon that is fed will always come back for more.\nThe enticing beauty of my cutting knife was the symptom.\nThe bread, my hungry curiosity.\nThe raccoon, an urge.\n\nThe moon increments its phase and reflects that much more light off of my cutting\nknife.\nThe very same light that glistens in the eyes of my raccoon friend.\nI slice the bread, fresh and soft. The raccoon becomes excited.\nor perhaps I'm merely projecting my emotions onto the newly-satisfied animal.\n\nThe raccoon has taken to following me.\nYou could say that we've gotten quite used to each other.\nThe raccoon becomes hungry more and more frequently, so my bread is always handy.\nEvery time I brandish my cutting knife the raccoon shows me its excitement.\nA rush of blood. Classic Pavlovian conditioning. I slice the bread.\nAnd I feed myself again."
            ]
            poem3 = [
                "Ghost under the light pt. 2",
                "The tendrils of my hair illuminate beneath the amber glow.\nBathing.\nIn the distance, a blue-green light flickers.\nA lone figure crosses its path– a silhouette obstructing the eerie glow.\nMy heart pounds. The silhouette grows. Closer Closer\nI open my umbrella, casting a shadow to shield me from visibility.\nBut I am too late.\nHe steps into the streetlight. I gasp and drop my umbrella.\nThe light flickers. My heart pounds. He raises his arm.\n\nTime stops.\n\nThe only indication of movement is the amber light flickering against his outstretched\narm.\nThe flickering light is in rhythm with the pounding of my heart.\nTeasing me for succumbing to this forbidden emotion.\nHave you ever heard of a ghost feeling warmth before?\nGiving up on understanding, I laugh.\nUnderstanding is overrated.\nI touch his hand. The flickering stops.\nGhosts are blue-green. My heart is amber."
            ]
            poem4 = [
                "Beach",
                "A marvel millions of years in the making.\nWhere the womb of Earth chaotically meets the surface.\nUnder a clear blue sky, an expanse of bliss -\nBut beneath gray rolling clouds, an endless enigma.\nThe easiest world to get lost in\nis one where everything can be found.\n\nOne can only build a sand castle where the sand is wet.\nBut where the sand is wet, the tide comes.\nWill it gently lick at your foundations until you give in?\nOr will a sudden wave send you crashing down in the blink of an eye?\nEither way the outcome is the same.\nYet we still build sand castles.\n\nI stand where the foam wraps around my ankles.\nWhere my toes squish into the sand.\nThe salty air is therapeutic.\nThe breeze is gentle, yet powerful.\nI sink my toes into the ultimate boundary line, tempted by the foamy tendrils.\nTurn back, and I abandon my peace to erode at the shore.\nDrift forward, and I return to Earth forevermore."
            ]
            if name.lower() == "ghost under the light":
                return poem1
            elif name.lower() == "the raccoon":
                return poem2
            elif name.lower() == "ghost under the light pt. 2":
                return poem3
            elif name.lower() == "beach":
                return poem4
            else:
                return random.choice([poem1,poem2,poem3,poem4])
        else:
            poem1 = [
                "Wheel",
                "A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel."
            ]
            poem2 = [
                "mdpnfbo,jrfp",
                "ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imbossing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bristlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotically overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano revealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuzzi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sharia prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness swerveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine flagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,delirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hryvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphides cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares castanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters subjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotising,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations snarier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lancelet,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulias flaggers wammul boastfully,,galravitch happies interassociation multipara augmentations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usuals,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterburs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadblocked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravellings quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistically,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist sticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unkenneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispositions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating retiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obduration exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi Fresh blood seeps through the line parting her skin and slowly colors her breast red. I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of me driving the knife into her flesh continuously, fucking her body with the blade, making a mess of her. My head starts going crazy as my thoughts start to return. Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely disgusting. How could I ever let myself think these things? But it’s unmistakable. The lust continues to linger through my veins. An ache in my muscles stems from the unreleased tension experienced by my entire body. Her Third Eye is drawing me closer."
            ]
            if name.lower() == "wheel":
                return poem1
            elif name.lower() == "mdpnfbo,jrfp":
                return poem2
            else:
                return random.choice([poem1,poem2])
    
    def quotes(self):
        return random.choice([
            "Here's a suggestion. Have you considered killing yourself? It would be beneficial to your mental health.",
            "After all, doesn't a hot cup of tea help you enjoy a good book?",
            "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?",
            "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment.",
            "Monika, please mind your own business for once. Or do you want to tell me there's something wrong with helping involve MC in club activities?",
            "Yes! I have terrible reading posture! So that's why we should sit on the floor.",
            "The thing is, I'm kind of into knives... They're just...so pretty...",
            "Just...for a little longer. It feels really nice...",
            "Sorry that my lifestyle is too much for someone of your mental age to comprehend!",
            "D-Did you just accuse me of cutting myself?? What the fuck is wrong with your head?!",
            "I love you so much that I even touch myself with the pen I stole from you.",
            "I just want to pull your skin open and crawl inside of you.",
            "Stagnating air is common foreshadowing that something terrible is about to happen..."
        ])
    
    def tagging(self, tamper=False, content=""):
        if not tamper:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Y-Yes...?",
                    "Did you want to talk to me...?",
                    "Hm?"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "H-Hello there.",
                    "...h-hi...",
                    "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "O-Oh! W-W-Well, uhh... :flushed:",
                    "I-I love you, too... :relaxed:",
                    "R-Really? Why? I-I don't have anything worth loving...",
                    "Uuu, why is my heart beating so fast right now??"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "G-Goodnight, then.",
                    "Until next time.",
                    "I hope you have wonderful dreams!"
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "It is a good morning, indeed.",
                    "I hope you slept wonderfully!",
                    "Good morning!"
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon.",
                    "A truly beautiful afternoon, it is.",
                    "Ah, it's times like this where I just want to sit outsite and read a good book."
                ])
            elif re.search(f"(^|[^A-Za-z])((^|yuri|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Y-You really think so...?",
                    "Uuu... :flushed:",
                    "T-Thank you. I needed to hear that...",
                    ":blush:"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I don't think I fully understand why you're apologizing, but I accept it, anyway.",
                    "It's alright; I forgive you.",
                    "N-No, I'm the one who should be sorry; I mess up everything...",
                    "Consider your apology accepted, then!"
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Sh-She does?"
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Ahaha... I-I'm glad that I have a friend like Monika who loves me... :blush:"
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Haha. Well, she is a loving soul."
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Uuuuuuuuuu..."
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "O-Oh... I hope y-you feel better soon.",
                    "Oh... please do feel better."
                ])
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|natsuki|<@!?580135631611494403>|sayori|<@!?580133736721678341>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "W-Well, I suppose that's true; she's much better than I am..."
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|yuri|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Oh! Uh... Well, I'm glad you think that!"
            else:
                return "I-I'm sorry, but I don't understand what you mean..."
        else:
            if re.search("^$", content, re.IGNORECASE):
                return random.choice([
                    "Yes, my love?",
                    "Oh, did someone call for me?"
                ])
            elif re.search("(^|[^A-Za-z])(h+(i+|e+(y+|l+o+)))([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Hello there.",
                    "Hello, my beloved! Nice to see you!"
                ])
            elif re.search("(^|[^A-Za-z])(ily|i *love *you)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I love you, too! I love you so much that I touch myself to you every night!",
                    "I'm glad, because if you didn't, I'd be very, *very* upset...",
                    ":smirk:",
                    "...Ahahaha. Ahahahahahaha! Ahahahahahahahaha! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
                ])
            elif re.search("(^|[^A-Za-z])good *night([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Haha. No. You're not allowed to go.",
                    "Goodnight! I'll be sure to watch over you very closely while you're resting...",
                    "I hope you don't mind if I look at your chest move up and down while the beautiful, soft breathing noises come from your mouth. Ahaha..."
                ])
            elif re.search("(^|[^A-Za-z])good *morning([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good morning, my love!",
                    "Oh, good! You're finally awake!",
                    "Did you know you snore very loudly? Ahaha...",
                    "Good morning! I can't wait to spend the day together! Just you and me, nobody else..."
                ])
            elif re.search("(^|[^A-Za-z])good *afternoon([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Good afternoon! But who cares what time it is; we'll be together forever, right??",
                    "A perfect afternoon for just staring at each other, telling what kind of dirty things we could do together..."
                ])
            elif re.search(f"(^|[^A-Za-z])((^|yuri|<@!?{self.id}>) *is|you('re| *are)) *(adorable|amazing|beautiful|cute|hot|pretty)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ohoho, stop it, you! I'm nothing compared to you!",
                    "But you're 10 times as amazing!",
                    "no u",
                    "Oh? Am I attractive enough for you to pleasure yourself to the thought of me? Because I do it to the thought of you all the time!",
                    "Oh, I love it when you tell me that!"
                ])
            elif re.search("(^|[^A-Za-z])(i *apologi(s|z)e|sorry)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahaha. There's no need to be sorry. I honestly found it kinda hot...",
                    "Well, if it'll make you feel better, I accept your apology.",
                    "Uhuhu. You look so cute when you apologize like that!"
                ])
            elif re.search("(^|[^A-Za-z])(natsuki|<@!?580135631611494403>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Pfft. As if. That immature brat doesn't love anyone but herself."
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "I'll believe that when that bitch says it to my face!"
            elif re.search("(^|[^A-Za-z])(sayori|<@!?580133736721678341>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Who the hell is Sayori? I don't know any Sayoris..."
            elif re.search("(^|[^A-Za-z])(mc|<@!?606721454297448448>) *loves *you([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Of course he loves me! And I will make sure **NOBODY** takes him away from me!"
            elif re.search("(^|[^A-Za-z])(i('m| *am) *(feel(ing)?)? *sick|not *feeling *(good|great)|puk(ed?|ing))([^A-Za-z]|$)", content, re.IGNORECASE):
                return "Feel better soon my love so we can love each other forever!"
            elif re.search("(^|[^A-Za-z])(monika|<@!?707337539677192272>|natsuki|<@!?580135631611494403>|sayori|<@!?580133736721678341>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "No, she's fucking not."
            elif re.search(f"(^|[^A-Za-z])(^is|you('re| *are)?|yuri|<@!?{self.id}>) *best *(doki|girl)([^A-Za-z]|$)", content, re.IGNORECASE):
                return "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
            else:
                return "I love you, but I have no clue what you just said."

    def tickle(self, tamper=False):
        if not tamper:
            return rstr.xeger(r"((Oh!|P-Please! Stop it!|Hey, that tickles!|H-Hey! That's my ticklish spot!!) )?(((A|Ha)(ha){3,6}|(E|He)(he){3,6}|(A|HA)(HA){3,6})!{1,3}( \*snort\*)?|:laughing:)")
        else:
            return rstr.xeger(r"((A|Ha)(ha){3,6}|(A|HA)(HA){5,9}|(E|HE)(HE){5,9})!{1,3}( Yes, just like that!)?")
    
    def triggers(self, tamper=False, content=""):
        if not tamper:
            if re.search("(^|[^A-Za-z])(cut(s|ting|ted)?|stab(s|bing|bed)?)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Uuu...!",
                    "D-Did you have to say that word...?",
                    "I-I'm sorry, I-I really don't like that word...",
                    ":confounded:"
                ])
            elif re.search("(^|[^A-Za-z])kni(fe|(v|f)es)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Y-You know, I'm a fan of knives...",
                    "Do you like knives, as well?"
                ])
            elif re.search("(^|[^A-Za-z])pens?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I-I get the feeling you're insulting me by mentioning pens...",
                    "Uuu...! Why did Monika have to make me do...things...? Now I can't think of pens the same way again...!! :cold_sweat:",
                    "I-I only use pens for writing, I swear!!"
                ])
        else:
            if re.search("(^|[^A-Za-z])(cut(s|ting|ted)?|stab(s|bing|bed)?)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Oooo, yes. Say that again, please.",
                    "Hahaha! I love your twisted sense of humor! It makes me so wet...",
                    "Oh, I love it when you say that word... it makes me want to cut you and lick all the blood off."
                ])
            elif re.search("(^|[^A-Za-z])kni(fe|(v|f)es)([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "Ahahaha! Did someone mention knives...?!",
                    "Oh, I love knives! The way the sharp blade slides along skin is just beautiful!",
                    "Oh, just hearing that word makes me feel so... Ahaha..."
                ])
            elif re.search("(^|[^A-Za-z])pens?([^A-Za-z]|$)", content, re.IGNORECASE):
                return random.choice([
                    "I still have the pen I stole from MC... I even still use it from time to time...",
                    "Hahaha. Are you expecting me to do something naughty with a pen? Because I just might if you ask nicely...",
                    "Oh... Oh...! OH!!! YES, YES, YESYESYES!!!"
                ])

    def welcome(self, tamper=False, member=False):
        if not tamper and member:
            return rstr.xeger(r"Welcome to the Literature Club " + member + r"\. (It\'s a p|P)leasure (meeting you|to have you|to be with us)\.")
        elif member:
            return f"Welcome {member} my one true love! Please ignore any other whore who you encounter, they don't matter."
        return