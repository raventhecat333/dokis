import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Poems(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def poems(self,ctx):
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send("```s_poem dear sunshine \ns_poem bottles \ns_poem % \ns_poem eagles can fly \ns_poem amy likes spiders \ns_poem i'll be your beach \ns_poem because you \ns_poem ghost under the light \ns_poem 2 ghost under the light \ns_poem the raccoon \ns_poem beach \ns_poem hole in wall \ns_poem 2 hole in wall \ns_poem save me \ns_poem the lady who knows everything \ns_poem happy end```")

    @client.command()
    async def poem(self,ctx, *, poem=None):
        s_poem_intros = ["Oh, I really loved writing this one!", "I hope you like it!", "I can't wait to show you this one!"]
        n_poem_intros = ["I hope she doesn't get mad at me for showing you this...", "Oh! This is one of Natsuki's best poems!", "Aw, this is a cute one, just like her!"]
        y_poem_intros = ["Oooo, Yuri did a great job with this one!", "I personally don't get what she's saying with this one, but I still like it!", "I kinda like this side of Yuri, if I'm being honest!"]
        m_poem_intros = ["Well, her writing style is unique, to say the least.", "I love how abstract Monika's writing is!", "There's a reason she's the president of the club!"]

        if poem is None:
            await ctx.send("ehh?")
        elif poem == "dear sunshine":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(s_poem_intros))
            embed = discord.Embed(title="Dear Sunshine", description="*by Sayori*", color=conf.norm)
            await ctx.send(embed=embed)
            await ctx.send(''' 
The way you glow through my blinds in the morning 
It makes me feel like you missed me. 
Kissing my forehead to help me out of bed. 
Making me rub the sleepy from my eyes. 
 
Are you asking me to come out and play? 
Are you trusting me to wish away a rainy day? 
I look above. The sky is blue. 
It's a secret, but I trust you too. 
 
If it wasn't for you, I could sleep forever. 
But I'm not mad. 
 
I want breakfast.''')  
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "bottles":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            embed = discord.Embed(title="Bottles", description="*by Sayori*", color=conf.norm)
            await ctx.send(random.choice(s_poem_intros))
            await ctx.send(embed=embed)
            await ctx.send(''' 
I pop off my scalp like the lid of a cookie jar. 
It's the secret place where I keep all my dreams. 
Little balls of sunshine, all rubbing together like a bundle of kittens 
I reach inside with my thumb and forefinger and pluck one out. 
It's warm and tingly. 
But there's no time to waste! I put it in a bottle to keep it safe. 
And I put the bottle on the shelf with all of the other bottles. 
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row. 
 
My collection makes me lots of friends. 
Each bottle a starlight to make amends. 
Sometimes my friend feels a certain way. 
Down comes a bottle to save the day. 
 
Night after night, more dreams. 
Friend after friend, more bottles. 
Deeper and deeper my fingers go. 
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies. 
Digging and digging. 
Scraping and scraping. 
 
I blow dust off my bottle caps. 
It doesn't feel like time elapsed. 
My empty shelf could use some more. 
My friends look through my locked front door. 
 
Finally, all done. I open up, and in come my friends. 
In they come, in such a hurry. Do they want my bottles that much? 
I frantically pull them from the shelf, one after the other. 
Holding them out to each and every friend. 
Each and every bottle. 
But every time I let one go, it shatters against the tile between my feet. 
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor. 
 
They were supposed to be for my friends, my friends who aren't smiling. 
They're all shouting, pleading. Something. 
But all I hear is echo, echo, echo, echo, echo 
Inside my head.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "%":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(s_poem_intros))
            embed = discord.Embed(title="%", description="*by Sayori*", color=conf.norm)
            await ctx.send(embed=embed)
            await ctx.send(''' 
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of 
Get. 
Out. 
Of. 
My. 
Head. 
 
 
 
Get out of my head before I do what I know is best for you. 
Get out of my head before I listen to everything she said to me. 
Get out of my head before I show you how much I love you. 
Get out of my head before I finish writing this poem. 
 
 
 
But a poem is never actually finished. 
It just stops moving.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "eagles can fly":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(n_poem_intros))
            embed = discord.Embed(title="Eagles Can Fly", description="*by Natsuki*", color=0xff42e2)
            await ctx.send(embed=embed)
            await ctx.send(''' 
Monkeys can climb 
Crickets can leap 
Horses can race 
Owls can seek 
Cheetahs can run 
Eagles can fly 
People can try 
But that's about it.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "amy likes spiders":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(n_poem_intros))
            embed = discord.Embed(title="Amy likes spiders", description="*by Natsuki*", color=0xff42e2)
            await ctx.send(embed=embed)
            await ctx.send(''' 
You know what I heard about Amy? 
Amy likes spiders. 
Icky, wriggly, hairy, ugly spiders! 
That's why I'm not friends with her. 
 
Amy has a cute singing voice. 
I heard her singing my favorite love song. 
Every time she sang the chorus, my heart would pound to the rhythm of the words. 
But she likes spiders. 
That's why I'm not friends with her. 
 
One time, I hurt my leg really bad. 
Amy helped me up and took me to the nurse. 
I tried not to let her touch me. 
She likes spiders, so her hands are probably gross. 
That's why I'm not friends with her. 
 
Amy has a lot of friends. 
I always see her talking to people. 
She probably talks about spiders. 
What if her friends start to like spiders too? 
That's why I'm not friends with her. 
 
It doesn't matter if she has other hobbies. 
It doesn't matter if she keeps it private. 
It doesn't matter if it doesn't hurt anyone. 
 
It's gross. 
She's gross. 
The world is better off without spider lovers. 
 
And I'm gonna tell everyone.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "i'll be your beach":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(n_poem_intros))
            embed = discord.Embed(title="I'll be your beach", description="*by Natsuki*", color=0xff42e2)
            await ctx.send(embed=embed)
            await ctx.send(''' 
Your mind is so full of troubles and fears 
That diminished your wonder over the years 
But today I have a special place 
A beach for us to go. 
 
A shore reaching beyond your sight 
A sea that sparkles with brilliant light 
The walls in your mind will melt away 
Before the sunny glow. 
 
I'll be the beach that washes your worries away 
I'll be the beach that you daydream about each day 
I'll be the beach that makes your heart leap 
In a way you thought had left you long ago. 
 
Let's bury your heavy thoughts in a pile of sand 
Bathe in sunbeams and hold my hand 
Wash your insecurities in the salty sea 
And let me see you shine. 
 
Let's leave your memories in a footprint trail 
Set you free in my windy sail 
And remember the reasons you're wonderful 
When you press your lips to mine. 

I'll be the beach that washes your worries away 
I'll be the beach that you daydream about each day 
I'll be the beach that makes your heart leap 
In a way you thought had left you long ago. 
 
But if you let me by your side 
Your own beach, your own escape 
You'll learn to love yourself again.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "because you":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(n_poem_intros))
            embed = discord.Embed(title="Because you", description="*by Natsuki*", color=0xff42e2)
            await ctx.send(embed=embed)
            await ctx.send(''' 
Tomorrow will be brighter with me around. 
But when today is dim, I can only look down. 
My looking is a little more forward 
Because you look at me. 
 
When I want to say something, I say it with a shout! 
But my truest feelings can never come out. 
My words are a little less empty 
Because you listen to me. 
 
When something is above me, I reach for the stars. 
But when I feel small, I don't get very far. 
My standing is a little bit taller 
Because you sit with me. 
 
I believe in myself with all of my heart 
But what do I do when it's torn all apart? 
My faith is a little bit stronger 
Because you trusted me. 
 
My pen always puts my feelings to the test. 
I'm not a good writer, but my best is my best. 
 
My poems are a little bit dearer 
Because you think of me. 
 
Because you, because you, because you.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "gohst under the light":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(y_poem_intros))
            embed = discord.Embed(title="Ghost Under the Light", description="*by Yuri*", color=0x8524c8)
            await ctx.send(embed=embed)
            await ctx.send(''' 
The tendrills of my hair illuminate beneath the amber glow. 
Bathing. 
It must be this one. 
The last remaining streetlight to have withstood the test of time. 
the last yet to be replaced by the sickening blue-green of the future. 
I bathe. Calm; breathing air of the present but living in the past. 
The light flickers. 
I flicker back.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "2 ghost under the light":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            embed = discord.Embed(title="Ghost Under the Light (2)", description="*by Yuri*", color=0x8524c8)
            await ctx.send(embed=embed)
            await ctx.send(random.choice(y_poem_intros))
            await ctx.send(''' 
The tendrills of my hair illuminate beneath the amber glow. 
Bathing. 
In the distance, a blue-green light flickers. 
A lone figure crosses its path- a silhouette obstructing the eerie glow. 
My heart pounds. The silhouette grows. Closer Closer. 
I open my umbrella, casting a shadow to shield me from visibility. 
But I am too late. 
He steps into the streetlight. I gasp and drop my umbrella. 
The light flickers. My heart pounds. He raises his arm. 
 
Time stops. 
 
The only indication of movement is the amber light flickering against his outstretched 
arm. 
The flickering light is in rhythm with the pounding of my heart. 
Teasing me for succumbing to his forbidden emotion. 
Have you ever heard of a ghost feeling warmth before? 
Giving up on understanding, I laugh. 
Understanding is overrated. 
I touch his hand. The flickering stops. 
Ghosts are blue-green. My heart is amber.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "the raccoon":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(y_poem_intros))
            embed = discord.Embed(title="The Raccoon", description="*by Yuri*", color=0x8524c8)
            await ctx.send(embed=embed)
            await ctx.send(''' 
It happened in the dead of night while I was slicing bread for a guilty snack. 
My attention was caught by the scuttering of a raccoon outside my window. 
That was, I believe, the first time I noticed my strange tendencies as an unusual 
human. 
I gave the raccoon a piece of bread, my subconscious well aware of the consequences. 
Well aware that a raccoon that is fed will always come back for more. 
The enticing beauty of my cutting knife was a symptom. 
The bread, my hungry curiosity. 
The raccoon, an urge. 
 
The moon increments its phase and reflects that much more light off of my cutting 
knife. 
The very same light that glistens in the eyes of my raccoon friend. 
I slice the bread, fresh and soft. The raccoon becomes excited. 
or perhaps I'm merely projecting my emotions onto the newly-satisfied animal. 
 
The raccoon has taken to following me. 
You could say that we've gotten quite used to each other. 
The raccoon becomes hungry more and more frequently, so my bread is always handy. 
Every time I brandish my cutting knife the raccoon shows me its excitement. 
A rush of blood. Classic Pavlovian conditioning. I slice the bread. 
 
And I feed myself again.''')
#--------------------------------------------------------------



#--------------------------------------------------------------
        elif poem == "beach":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(y_poem_intros))
            embed = discord.Embed(title="Beach", description="*by Yuri*", color=0x8524c8)
            await ctx.send(embed=embed)
            await ctx.send(''' 
A marvel millions of years in the making. 
Where the womb of Earth chaotically meets the surface. 
Under a clear blue sky, an expanse of bliss - 
But beneath gray rolling clouds, an endless enigma. 
The easiest world to get lost in 
is one where everything can be found. 
 
One can only build a sand castle where the sand is wet. 
But where the sand is wet, the tide comes. 
Will it gently lick at your foundations until you give in? 
Or will a sudden wave send you crashing down in the blink of an eye? 
Either way the outcome is the same. 
Yet we still build sand castles. 
 
I stand where the foam wraps around my ankles. 
Where my toes squish into the sand. 
The salty air is therapeutic. 
The breeze is gentle, yet powerful. 
I sink my toes into the ultimate boundary line, tempted by foamy tendrils. 
Turn back, and I abandon my peace to erode at the shore. 
Drift forward, and I return to Earth forever more.''')
#--------------------------------------------------------------



#-------------------------------------------------------------
        elif poem == "hole in the wall":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(m_poem_intros))
            embed = discord.Embed(title="Hole in Wall", description="*by Monika*", color=0x12ba01)
            await ctx.send(embed=embed)
            await ctx.send(''' 
It couldn't have been me. 
See, the direction the spackle protrudes. 
A noisy neighbor? An angry boyfriend? I'll never know. I wasn't home. 
I peer inside for a clue. 
No! I can't see. I reel, blind, like a film left out in the sun. 
But it's too late. My retinas. 
Already scorched with a permanent copy of the meaningless image. 
It's just a little hole. It wasn't too bright. 
It was too deep. 
Stretching forever into everything. 
A hole of infinite choices. 
I realize now, that I wasn't looking in. 
I was looking out. 
And he, on the other side, was looking in.''')
#-------------------------------------------------------------



#-------------------------------------------------------------
        elif poem == "2 hole in the wall":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(m_poem_intros))
            embed = discord.Embed(title="Hole in Wall (2)", description="*by Monika*", color=0x12ba01)
            await ctx.send(embed=embed)
            await ctx.send(''' 
But he wasn't looking at me. 
Confused, I frantically glance at my surroundings. 
But my burned eyes can no longer see color. 
Are there others in this room? Are they talking? 
Or are they simply poems on flat sheets of paper, 
The sound of frantic scrawling playing tricks on my ears? 
The room begins to crinkle. 
Closing in on me. 
The air I breathe dissipate before it reaches my lungs. 
I panic. There must be a way out. 
It's right there. He's right there. 
 
Swallowing my fears, I brandish my pen.''')
#--------------------------------------------------------------


#--------------------------------------------------------------
        elif poem == "save me":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(m_poem_intros))
            embed = discord.Embed(title="Save me", description="*by Monika*", color=0x12ba01)
            await ctx.send(embed=embed)
            await ctx.send(''' 
The colors, they won't stop. 
Bright, beautiful colors 
Flashing, expanding, piercing 
Red, green, blue 
An endless 
cacophony 
Of meaningless 
noise 
 
The noise, it won't stop. 
Violent, grating waveforms 
Squeaking, screeching, piercing 
Sine, cosine, tangent 
Like playing a chalkboard on a turntable 
Like playing a vinyl on a pizza crust. 
An endless 
poem 
Of meangless 
 
Load me''')
#--------------------------------------------------------------


#--------------------------------------------------------------
        elif poem == "the lady who knows everything":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(m_poem_intros))
            embed = discord.Embed(title="The lady who knows everything", description="*by Monika*", color=0x12ba01)
            await ctx.send(embed=embed)
            await ctx.send(''' 
An old tale tells of a lady who wanders Earth. 
The Lady who Knows Everything. 
A beautiful lady who has found every answer, 
All meaning, 
All purpose, 
And all that was ever sought. 
 
And here I am, 
 
a feather 
 
Lost adrift the sky, victim of the currents of the wind. 
 
Day after day, I search. 
I search with little hope, knowing legends don't exist. 
But when all else has failed me, 
When all others have turned away, 
The legend is all that remains - the last dim star glimmering in the twilit sky. 
 
Until one day, the wind ceases to blow. 
I fall. 
And I fall and fall, and fall even more. 
Gentle as a feather. 
A dry quill, expressionless. 
 
But a hand catches me, between the thumb and forefinger. 
The hand of a beautiful lady. 
I look at her eyes and find no end to her gaze. 
 
The Lady who Knows Everything knows what I am thinking. 
Before I can speak, she responds in a hollow voice. 
"I have found every answer, all of which amount to nothing. 
There is no meaning. 
There is no purpose. 
And we seek only the impossible. 
I am not your legend. 
Your legend does not exist." 
 
And with a breath, she blows me back afloat, and I pick up a gust of wind.''')
#--------------------------------------------------------------


#--------------------------------------------------------------
        elif poem == "happy end":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(m_poem_intros))
            embed = discord.Embed(title="Happy end", description="*by Monika*", color=0x12ba01)
            await ctx.send(embed=embed)
            await ctx.send(''' 
Pen in hand, I find my strength. 
The courage endowed upon me by my one and only love. 
Together, let us dismantle this crumbling world 
And write a novel of our own fantasies. 
 
With a flick of her pen, the lost finds her way. 
In a world of infinite choices, behold her special day. 
 
After all, 
Not all good times must come to an end''')
#--------------------------------------------------------------



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Poems(bot)) 