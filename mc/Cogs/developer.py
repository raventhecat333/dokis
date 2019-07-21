import discord, json, platform, os, subprocess, Cogs.checks, chalk, sys, traceback, asyncio, textwrap
from discord.ext import commands as client
from os import listdir
from os.path import isfile, join
from Cogs.config import conf

checks = Cogs.checks
Cogs = "Cogs"

class Developer(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self._last_result = None

    @client.command()
    @checks.dev()
    async def shutdown(self,ctx):
        embed = discord.Embed(title = "Closing this instance...",color = conf.norm)
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.dnd)
        await quit()


    @client.command()
    @checks.dev()
    async def restart(self,ctx):
        embed = discord.Embed(title = "Give me a moment to restart...",color = conf.norm)
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.idle)
        print(chalk.yellow("A developer has restarted the bot!"))
        print("\n")
        subprocess.call([sys.executable, "maid.py"])


    @client.command()
    @checks.dev()
    async def say(self, ctx, *, message): # A commmand that makes the bot say the given argument and deletes the message the user sent before
        try:
            await ctx.message.delete() # Deletes our message
            await ctx.send(message) # sends our message
        except discord.errors.Forbidden: # If we can't delete it then 
            await ctx.send(message) # Just send the message

    # Pulled from my bot (Axiro) for the sake of development. -iDroid
    @client.command()
    @checks.dev()
    async def pull(self, ctx):
        c = subprocess.call(('git', 'pull'))
        if c != 0:
            await ctx.send("Updating from Git failed.")
            return
        await ctx.send("Successfully updated from Git.")



def setup(bot):
    bot.add_cog(Developer(bot))