import discord, random, re
import discord.ext.commands as client

class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if (message.author.bot
        or (message.guild is not None and self.bot.globalCursor.execute(f"SELECT * FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'guild' AND id = {message.guild.id}").fetchone() is not None)
        or (message.guild is None and self.bot.globalCursor.execute(f"SELECT * FROM offTriggers WHERE bot = '{self.bot.name}' AND type = 'user' AND id = {message.author.id}").fetchone() is not None)
        or re.search(f"^({self.bot.character.prefix}|<@!?{self.bot.character.id}>|(m(onika)?|s(ayori)?|y(uri)?|n(atsuki)?|mc)_poem)", message.content.lower())):
            return
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {message.guild.id if message.guild else 0}) OR (type = 'user' AND id = {message.author.id})").fetchone() is not None else False
        reply = self.bot.character.triggers(tamper=tampered, content=message.content)
        if reply:
            await self.bot.send(message.channel, reply)

def setup(bot):
    bot.add_cog(Triggers(bot))