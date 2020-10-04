import asyncio, discord, random
import discord.ext.commands as client

class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            return
        tampered = await self.bot.checkTamper(message.guild.id if message.guild else message.author.id, type = "guild" if message.guild else "user")
        reply = self.bot.character.interactions(tamper=tampered, bot=self.bot, message=message)
        if isinstance(reply, discord.Embed):
            await self.bot.send(message.channel, "", reply)
        elif reply:
            await self.bot.send(message.channel, reply)

def setup(bot):
    bot.add_cog(Interactions(bot))