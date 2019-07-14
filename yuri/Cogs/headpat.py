import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Headpat(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def headpat(self,ctx):
        if ctx.guild is None:#PM'S
            headpat_list0 = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(headpat_list0))

        elif ctx.guild.id not in conf.act2:#ACT1 
            headpat_list1 = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(headpat_list1))
        
        elif ctx.guild.id in conf.act2:#ACT2
            headpat_list2 = ["Oh, only my head is being pat? Shame.", "Huhuhu. I love it when you do cute things like that to me!", "Mmm... You know what would be better? If you moved that hand somewhere else...", "Oh, am I your dog or something? That's okay. I'll be anything you want me to be, my love."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(headpat_list2))

def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Headpat(bot))
