import asyncio, discord, random, rstr
import discord.ext.commands as client

class Ready(client.Cog):

    def __init__(self, bot):

        self.bot = bot

    @client.Cog.listener()
    async def on_ready(self):

        print(f'Logged on as {self.bot.user} with {self.bot.ChrFile["about"]["name"].lower()}.chr!')
        self.bot.loop.create_task(self.StatusLoop())

    async def StatusLoop(self):

        while not self.bot.is_closed():

            games = self.bot.ChrFile["playing"]

            for game in games:

                await self.bot.change_presence(activity=discord.Game(name=rstr.xeger(game)))
                await asyncio.sleep(900)

def setup(bot):
    bot.add_cog(Ready(bot))