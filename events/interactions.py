import asyncio, discord, globalVars, random
import discord.ext.commands as client

class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            return
        tampered = True if self.bot.globalCursor.execute(f"SELECT * FROM tampered WHERE bot = '{self.bot.name}' AND (type = 'guild' AND id = {message.guild.id if message.guild else 0}) OR (type = 'user' AND id = {message.author.id})").fetchone() is not None else False
        reply = self.bot.character.interactions(tamper=tampered, bot=self.bot, message=message)
        if isinstance(reply, discord.Embed):
            await self.bot.send(message.channel, "", reply)
        elif reply:
            await self.bot.send(message.channel, reply)

def setup(bot):
    bot.add_cog(Interactions(bot))