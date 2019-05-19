import discord, json, platform, os, subprocess, Cogs.checks, chalk, sys, traceback, asyncio 
from discord.ext import commands
from os import listdir
from os.path import isfile, join
from Cogs.config import conf

ver = conf.version
nol = conf.norm
eol = conf.err
checks = Cogs.checks
Cogs = "Cogs"

class Event(commands.Cog):

    def __init__(self, bot):
         self.b = bot

    @commands.command()
    @checks.dev()
    async def refresh(self, ctx):
        """Re-initialise the cogs folder."""
        await ctx.send(embed=discord.Embed(title="Give me a moment...", colour=nol))
        print("\n")
        for extension in [f.replace('.py', '') for f in listdir(Cogs) if isfile(join(Cogs, f))]:
            try:
                if extension == "config" or extension == "checks":
                    pass
                else:   
                    self.b.unload_extension(Cogs + "." + extension)
                    self.b.load_extension(Cogs + "." + extension) 
                    print(chalk.green(f"Loaded {extension}"))
            except Exception as e: 
                print(chalk.red(f'Failed to load extension {extension}', file=sys.stderr))
                ono = traceback.format_exc()
                print(chalk.red(ono))
                print("\n")
                continue


    @commands.command()
    @checks.dev()
    async def shutdown(self,ctx):
        await ctx.send("Shutting down...")
        await self.b.close()


    @commands.command()
    @checks.dev()
    async def restart(self,ctx):
        await ctx.send("Restarting, give me a moment...")
        print(chalk.yellow("A developer has restarted the bot!"))
        print("\n")
        subprocess.call([sys.executable, "maid.py"])
        await self.b.logout() 


    @commands.command()
    @checks.dev()
    async def say(self, ctx, *, message): # A commmand that makes the bot say the given argument and deletes the message the user sent before
        try:
            await ctx.message.delete() # Deletes our message
            await ctx.send(message) # sends our message
        except discord.errors.Forbidden: # If we can't delete it then 
            await ctx.send(message) # Just send the message


def setup(bot):
    bot.add_cog(Event(bot))
