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
        e.add_field(name="Poem #1",value="Hole in the Wall.")
        e.add_field(name="Poem #2",value="Hole in the Wall 2.",inline=False)
        e.add_field(name="Poem #3",value="Save me.",inline=False)
        e.add_field(name="Poem #4",value="The lady who knows everything.",inline=False)
        await ctx.send(embed=e)

    @client.command()
    async def poem(self,ctx, *, poem=None):
        poem_intros = ["Well, her writing style is unique, to say the least.", "I love how abstract Monika's writing is!", "There's a reason she's the president of the club!"]

        if poem is None:
            await ctx.send("Uhh, sorry but this isn't a poem that i made.")

#-------------------------------------------------------------
        elif "hole in the wall" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "hole in the wall 2" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "save me" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "the lady who knows everything" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "happy end" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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

        else:
            await ctx.send("Hey! This isn't a poem, sorry about that! Could you please check if you spelt that correctly?")


def setup(bot):
    bot.add_cog(Poems(bot))
