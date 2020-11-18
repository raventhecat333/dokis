import discord, re
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Action(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def hug(self,ctx):
        await action(self, ctx, "Hug")

    @client.command(pass_context=True, aliases=['pat'])
    @client.cooldown(1, 2, BucketType.user)
    async def headpat(self,ctx):
        await action(self, ctx, "Headpat")

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def boop(self,ctx):
        await action(self, ctx, "Boop")

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def tickle(self,ctx):
        await action(self, ctx, "Tickle")

async def action(self, ctx, act):
    #perform action here
    if await self.bot.DetectEveryoneMention(ctx):
        return
    target = ctx.message.content.partition(' ')[2]
    
    monikaID = self.bot.GetCharacter("Monika").ChrFile["about"]["id"]
    sayoriID = self.bot.GetCharacter("Sayori").ChrFile["about"]["id"]
    yuriID = self.bot.GetCharacter("Yuri").ChrFile["about"]["id"]
    natsukiID = self.bot.GetCharacter("Natsuki").ChrFile["about"]["id"]
    mcID = self.bot.GetCharacter("MC").ChrFile["about"]["id"]
   
    if not target:
        await self.bot.Send(ctx, f"{act}-Player-{self.bot.ChrFile['about']['name']}")
    elif re.search(f"^({self.bot.ChrFile['about']['name']}|<@!?{self.bot.ChrFile['about']['id']}>|yourself)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-{self.bot.ChrFile['about']['name']}")
    elif ctx.guild and ctx.channel.permissions_for(self.bot.GetCharacter("MC").get_guild(ctx.guild.id).me).read_messages and re.search(f"^(mc|<@!?{mcID}>)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-MC")
    elif ctx.guild and ctx.channel.permissions_for(self.bot.GetCharacter("Natsuki").get_guild(ctx.guild.id).me).read_messages and re.search(f"^(natsuki|<@!?{natsukiID}>)$", target, re.IGNORECASE):       
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Natsuki")
    elif ctx.guild and ctx.channel.permissions_for(self.bot.GetCharacter("Yuri").get_guild(ctx.guild.id).me).read_messages and re.search(f"^(yuri|<@!?{yuriID}>)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Yuri")
    elif ctx.guild and ctx.channel.permissions_for(self.bot.GetCharacter("Sayori").get_guild(ctx.guild.id).me).read_messages and re.search(f"^(sayori|<@!?{sayoriID}>)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Sayori")
    elif ctx.guild and ctx.channel.permissions_for(self.bot.GetCharacter("Monika").get_guild(ctx.guild.id).me).read_messages and re.search(f"^(monika|<@!?{monikaID}>)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Monika")
    elif re.search(f"^(me|{ctx.author.name}|{ctx.author.display_name}|<@!?{ctx.author.id}>)$", target, re.IGNORECASE):
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Player")
    else:
        await self.bot.Send(ctx, f"{act}-{self.bot.ChrFile['about']['name']}-Target")

def setup(bot):
    bot.add_cog(Action(bot))