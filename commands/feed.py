import datetime, discord, re
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Feed(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.command(pass_context=True, aliases=['eat'])
    @client.cooldown(1, 2, BucketType.user)
    async def feed(self,ctx):
        if await self.bot.detectEveryoneMention(ctx):
            return
        tampered = await self.bot.checkTamper(ctx.guild.id if ctx.guild else ctx.author.id, type = "guild" if ctx.guild else "user")
        fed = ctx.message.content.partition(' ')[2]
        options = []
        if not fed:
            await self.bot.send(ctx, self.bot.character.feed(tamper=tampered, food=[], user=ctx.author))
            return
        if re.search("^(🍺|🍻|🍷|🍸|🍹|🍶|🥃|🍾)$", fed):
            options.append("alcohol")
        if re.search("^(🍼|🍭)$", fed):
            options.append("baby")
        if re.search("^(🎂)$", fed):
            if datetime.datetime.today().day == 22 and datetime.datetime.today().month == 9:
                options.append("birthday")
            else:
                options.append("birthday_not")
        if re.search("^(🥣)$", fed):
            options.append("bowl")
        if re.search("^(🍞|🥖)$", fed):
            options.append("bread")
        if re.search("^(🍔)$", fed):
            options.append("burger")
        if re.search("^(🧈)$", fed):
            options.append("butter")
        if re.search("^(🥫)$", fed):
            options.append("canned")
        if re.search("^(🍫)$", fed):
            options.append("chocolate")
        if re.search("^(☕)$", fed):
            options.append("coffee")
        if re.search("^(🍧|🍦|🍨)$", fed):
            options.append("cold")
        if re.search("^(🥤|🧃)$", fed):
            options.append("cold_drink")
        if re.search("^(🍪)$", fed):
            options.append("cookie")
        if re.search("^(🍳)$", fed):
            options.append("cooking")
        if re.search("^(🥐)$", fed):
            options.append("croissant")
        if re.search("^(🧁)$", fed):
            options.append("cupcake")
        if re.search("^(🥚)$", fed):
            options.append("egg")
        if re.search("^(🍆)$", fed):
            options.append("eggplant")
        if re.search("^(🧆)$", fed):
            options.append("falafel")
        if re.search("^(🧊)$", fed):
            options.append("ice")
        if re.search("^(🍣|🍱|🍛|🍙|🍚|🍘|🍜|🍢|🍡|🍥|🍲)$", fed):
            options.append("japanese")
        if re.search("^(🔪)$", fed):
            options.append("knife")
        if re.search("^(🍗|🍖|🍤|🌭|🥓|🥘|🥙|🥩)$", fed):
            options.append("meat")
        if re.search("^(🌮|🌯)$", fed):
            options.append("mexican")
        if re.search("^(🥛)$", fed):
            options.append("milk")
        if re.search("^(🌰|🥜)$", fed):
            options.append("nuts")
        if re.search("^(🥯|🥨)$", fed):
            options.append("pastries")
        if re.search("^(🍑)$", fed):
            options.append("peach")
        if re.search("^(🥜)$", fed):
            options.append("peanuts")
        if re.search("^(🌶️|🌶)$", fed):
            options.append("pepper")
        if re.search("^(🖊️)$", fed):
            options.append("pen")
        if re.search("^(🍕)$", fed):
            options.append("pizza")
        if re.search("^(🍿)$", fed):
            options.append("popcorn")
        if re.search("^(🧂)$", fed):
            options.append("salt")
        if re.search("^(🥪)$", fed):
            options.append("sandwich")
        if re.search("^(🍴|🍽️|🥄|🥢)$", fed):
            options.append("silverware")
        if re.search("^(🍰|🍮|🍬|🍫|🍩|🥮|🥧)$", fed):
            options.append("sweets")
        if re.search("^(🥡)$", fed):
            options.append("takeout")
        if re.search("^(🍵)$", fed):
            options.append("tea")
        if re.search("^(🧇)$", fed):
            options.append("waffle")
        if re.search("^(🍷)$", fed):
            options.append("wine")
        if re.search("^(🍏|🍎|🫐|🫒|🫑|🫓|🫔|🍐|🍊|🍋|🍌|🍉|🍇|🍓|🍈|🍒|🍑|🥭|🍍|🥥|🥝|🍅|🍆|🥑|🥦|🥬|🥒|🌶️|🌶|🌽|🥕|🧅|🧄|🥔|🍠|🥐|🥯|🍞|🥖|🥨|🧀|🥚|🍳|🥞|🧇|🥓|🥩|🍗|🍖|🌭|🍔|🍟|🍕|🥪|🧆|🥙|🌮|🌯|🥗|🥘|🥫|🍝|🍜|🍲|🍛|🍣|🍱|🥟|🍤|🍙|🍚|🍘|🍥|🥠|🥮|🍢|🍡|🍧|🍨|🍦|🥧|🧁|🍰|🎂|🍮|🍭|🍬|🍫|🍿|🍩|🍪|🌰|🥜|🍯|🧈|🥛|🍼|☕|🍵|🧉|🥤|🧃|🧊|🍶|🍺|🍻|🥂|🍷|🥃|🍸|🍹|🍾|🍽️|🥄|🍴|🥣|🥡|🥢|🧂)$", fed):
            options.append("misc")
        if not options:
            await self.bot.send(ctx, self.bot.character.feed(tamper=tampered, food=["bad food"], user=ctx.author))
            return
        await self.bot.send(ctx, self.bot.character.feed(tamper=tampered, food=options, user=ctx.author))

def setup(bot):
    bot.add_cog(Feed(bot))