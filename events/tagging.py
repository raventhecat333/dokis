import discord, json, random, re
import discord.ext.commands as client

class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {message.guild.id if message.guild else 0}) OR (type = 'user' AND id = {message.author.id})").fetchone() is not None else False
        if (message.author.bot
        or (message.guild
            and not re.search(f"^<@!?{self.bot.user.id}>", message.content))
        or (message.channel.type == discord.ChannelType.private
            and (re.search(f"^{self.bot.character.prefix}", message.content)
                or self.bot.character.triggers(tamper=tampered, content=message.content)))):
            return
        if message.guild:
            content = message.content.partition('>')[2].strip()
        else:
            content = message.content
        await self.bot.send(message.channel, self.bot.character.tagging(tamper=tampered, content=content))
        
def setup(bot):
    bot.add_cog(Tagging(bot))