import discord, json, re, rstr
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Delete(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.cooldown(1, 2, BucketType.user)
    async def delete(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {ctx.guild.id if ctx.guild else 0}) OR (type = 'user' AND id = {ctx.author.id})").fetchone() is not None else False
        victim = ctx.message.content.partition(' ')[2]

        if not victim:
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim=""))
        elif not tampered and re.search(f"^(monika|<@!?707337539677192272>|sayori|<@!?580133736721678341>|yuri|<@!?580134475250532352>|natsuki|<@!?580135631611494403>)$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="doki"))
        elif re.search(f"^me|<@!?{ctx.author.id}>$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="player"))
        elif re.search(f"^(<@!?({'|'.join(list(str(x) for x in json.loads(open('config.json').read())['devs']))})>)$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="dev"))
        elif re.search(f"^({self.bot.name})|<@!?{self.bot.user.id}>$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="self"))
        else:
            isMention = re.search("<@!?([0-9]{18})>", victim, re.IGNORECASE)
            if isMention:
                user = await self.bot.fetch_user(isMention.group(1))
                victim = user.name.lower()
            color = self.bot.character.color
            e = discord.Embed(title = self.bot.character.delete(tamper=tampered, victim="anyone", victimName=victim, channel=ctx.channel.id),color=int(color, base=16))
            await self.bot.send(ctx, "", embed= e)


def setup(bot):
    bot.add_cog(Delete(bot))

def check(character):
    return hasattr(character, "delete")
