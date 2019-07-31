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
        e.add_field(value="Poem #1",name="Ghost under the light.")
        e.add_field(value="Poem #2",name="Ghost under the light 2.",inline=False)
        e.add_field(value="Poem #3",name="The Raccoon.",inline=False)
        await ctx.send(embed=e)

    @client.command()
    async def poem(self,ctx, *, poem=None):
        poem_intros = ["Oooo, Yuri did a great job with this one!", "I personally don't get what she's saying with this one, but I still like it!", "I kinda like this side of Yuri, if I'm being honest!"]

        if poem is None:
            await ctx.send("This is not a poem that i made.")

#--------------------------------------------------------------
        elif "gohst under the light" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "ghost under the light 2" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            embed = discord.Embed(title="Ghost Under the Light (2)", description="*by Yuri*", color=0x8524c8)
            await ctx.send(embed=embed)
            await ctx.send(random.choice(poem_intros))
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
        elif "the raccoon" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "beach" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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


def setup(bot):
    bot.add_cog(Poems(bot))
