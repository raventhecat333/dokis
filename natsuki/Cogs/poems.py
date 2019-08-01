import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Poems(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def poems(self,ctx):
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        e = discord.Embed(color=conf.norm)
        e.set_author(name="My Poems!", icon_url=self.b.user.avatar_url)
        e.add_field(name="Poem #1",value="Amy likes spiders.")
        e.add_field(name="Poem #2",value="I'll be your beach.",inline=False)
        e.add_field(name="Poem #3",value="Because you.",inline=False)
        e.add_field(name="Poem #4",value="Eagles can fly.",inline=False)
        await ctx.send(embed=e)

    @client.command()
    async def poem(self,ctx, *, poem=None):
        poem_intros = ["I hope she doesn't get mad at me for showing you this...", "Oh! This is one of Natsuki's best poems!", "Aw, this is a cute one, just like her!"]

        if poem is None:
            await ctx.send("What? This isn't a poem that I made!")

#--------------------------------------------------------------
        elif "eagles can fly" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "amy likes spiders" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "i'll be your beach" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "because you" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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




def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Poems(bot)) 