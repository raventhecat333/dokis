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
        e.add_field(name="Poem #1",value="Dear Sunshine.")
        e.add_field(name="Poem #2",value="Bottles.",inline=False)
        e.add_field(name="Poem #3",value="%.",inline=False)
        await ctx.send(embed=e)

    @client.command()
    async def poem(self,ctx, *, poem=None):
        poem_intros = ["Oh, I really loved writing this one!", "I hope you like it!", "I can't wait to show you this one!"]

        if poem is None:
            await ctx.send("Huh?")

#--------------------------------------------------------------
        elif "dear sunshine" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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
        elif "bottles" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            embed = discord.Embed(title="Bottles", description="*by Sayori*", color=conf.norm)
            await ctx.send(random.choice(poem_intros))
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
        elif "%" in poem.lower():
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(poem_intros))
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



def setup(bot):
    bot.add_cog(Poems(bot))
