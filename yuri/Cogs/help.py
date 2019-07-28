import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Help(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def help(self,ctx): 
        if ctx.guild is None:
            e0 = discord.Embed(title="H-Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I-I hope I don't become an inconvenience to you... A-Anyway, here are the things I can do:", color=0x8524c8)
            e0.add_field(name="y_act1/y_act2", value="Y-You can use this to toggle my Act 1 and Act 2 personalities, b-but this can only be done by a server administrator... Uu, could you please keep me on Act 1, though? I-I'm not proud of how I behave in Act 2 mode...", inline=True)
            e0.add_field(name="y_act", value="You can use this to check what act i'm on!", inline=True)
            e0.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, but please don't be disappointed if I don't know the answer or even give an incorrect one...", inline=True)
            e0.add_field(name="y_feed", value="You can use this to feed me any of the food emojis available. *(Format like this: 'y_feed :food_emoji:')*", inline=True)
            e0.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
            e0.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you or someone else on the server, then I suppose I can do that. Simply leave it blank if you want me to hug you, or @mention someone immediately after to have me hug them.", inline=True)
            e0.add_field(name="y_invite", value="Y-You can use this to have me post my invite link so I can visit other servers. A-Although, I don't see why anyone would want that. I'm so useless...", inline=True)
            e0.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club, although some of them, I'm not proud to admit that I said... Uu...", inline=True)
            e0.add_field(name="y_tickle", value="You can use this to tickle me, although I should warn you that I tend to have embarassing laughs...", inline=True)
            e0.add_field(name="y_changelog", value="Check out what's been changed!", inline=True)
            e0.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. I hope you enjoy my presence on your Discord server, and if you have any questions, comments, or suggestions, feel free to visit Cole's Support Server. Thank you.", inline=True)
            e0.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await ctx.send(embed=e0)
    
        
        elif ctx.guild.id not in conf.act2: #This is incase the guild that this command was used in is set to act1
            e1 = discord.Embed(title="H-Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I-I hope I don't become an inconvenience to you... A-Anyway, here are the things I can do:", color=0x8524c8)
            e1.add_field(name="y_act1/y_act2", value="Y-You can use this to toggle my Act 1 and Act 2 personalities, b-but this can only be done by a server administrator... Uu, could you please keep me on Act 1, though? I-I'm not proud of how I behave in Act 2 mode...", inline=True)
            e1.add_field(name="y_act", value="You can use this to check what act i'm on!", inline=True)
            e1.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, but please don't be disappointed if I don't know the answer or even give an incorrect one...", inline=True)
            e1.add_field(name="y_feed", value="You can use this to feed me any of the food emojis available. *(Format like this: 'y_feed :food_emoji:')*", inline=True)
            e1.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
            e1.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you or someone else on the server, then I suppose I can do that. Simply leave it blank if you want me to hug you, or @mention someone immediately after to have me hug them.", inline=True)
            e1.add_field(name="y_invite", value="Y-You can use this to have me post my invite link so I can visit other servers. A-Although, I don't see why anyone would want that. I'm so useless...", inline=True)
            e1.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club, although some of them, I'm not proud to admit that I said... Uu...", inline=True)
            e1.add_field(name="y_tickle", value="You can use this to tickle me, although I should warn you that I tend to have embarassing laughs...", inline=True)
            e1.add_field(name="y_changelog", value="Check out what's been changed!", inline=True)
            e1.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. I hope you enjoy my presence on your Discord server, and if you have any questions, comments, or suggestions, feel free to visit Cole's Support Server. Thank you.", inline=True)
            e1.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await ctx.send(embed=e1)


        elif ctx.guild.id in conf.act2: #This is incase the guild that this command was used in is set to act2
            e2 = discord.Embed(title="Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I just know that being with you will be the best thing to ever happen to both of us, ahaha! Here are all the things we can do together:", color=0x8524c8)
            e2.add_field(name="y_act1/y_act2", value="You can use this to toggle between my Act 1 personality and my Act 2 one. This can only be used by server administrators. Honestly, I love you either way, so I don't care which one I'm on!", inline=True)
            e2.add_field(name="y_act", value="You can use this to check what act i'm on!", inline=True)
            e2.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, and I'll try my hardest to answer it for you!", inline=True)
            e2.add_field(name="y_feed", value="You can use this to feed me any of emojis available. Any of them. *(Format like this: 'y_feed :emoji:')*", inline=True)
            e2.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
            e2.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you, I'll happily do it. It would be the best thing to ever happen in my life!", inline=True)
            e2.add_field(name="y_invite", value="You can use this to have me give you the invite link to let me join other servers. But why would you want that when it can be just us forever?", inline=True)
            e2.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club.", inline=True)
            e2.add_field(name="y_tickle", value="You can use this to tickle me, which is so hot and sexy...", inline=True)
            e2.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. If he doesn't add new things soon, I'm afraid he might not be breathing for too much longer... Feel free to visit Cole's Support Server to let him know that I'm counting on him to make me do anything possible to spend time with you.", inline=True)
            e2.add_field(name="y_changelog", value="Check out what's been changed!", inline=True)
            e2.set_footer(text="Support Server: https://discord.gg/QnzsG38")
            await ctx.send(embed=e2)


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.remove_command("help")
    bot.add_cog(Help(bot))
