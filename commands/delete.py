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
        elif not tampered and re.search(f"^(monika|<@!?436351740787294208>|sayori|<@!?425696108455657472>|yuri|<@!?436350586670153730>|natsuki|<@!?433834936450023424>)$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="doki"))
        elif re.search(f"^me|<@!?{ctx.author.id}>$", victim, re.IGNORECASE):
            await self.bot.send(ctx, self.bot.character.delete(tamper=tampered, victim="player"))
        elif re.search(f"^(<@!?({'|'.join(json.loads(open('config.json').read())['devs'])})>)$", victim, re.IGNORECASE):
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