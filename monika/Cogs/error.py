import traceback, sys, discord, Cogs.checks, chalk
from discord.ext import commands
from Cogs.config import conf

name = conf.name
ver = conf.version
eol = conf.err
checks = Cogs.checks

class CommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance(error, commands.DisabledCommand):
            print(chalk.red(f"{ctx.command} is disabled with the command deco"))

        elif isinstance(error, commands.CommandNotFound):
            return
 
        elif isinstance(error, checks.blank):
            return

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Better ask a Club President to help with that one! (you need admin to change this setting)")

        else:
            tra = traceback.format_exception_only(type(error), error)
            e = discord.Embed(description=f"`Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this... I think...` ```py\n%s\n``` \n Looks like you encountered an issue! If you want, you can report this by clicking [here!](https://support.dokis.dev/index.php) (It takes you to a website where you can explain the bug in detail.)" % ''.join(tra), file=sys.stderr, color=eol)
            e.set_author(name="That's an issue!",icon_url=ctx.message.author.avatar_url)
            e.set_footer(text="v"+ver)
            await ctx.send(embed=e)
            print(chalk.yellow(f"Warning! The command '{ctx.command}' has just Errored!")) 
            print(chalk.red(f"Traceback: %s" % ''.join(tra)))



def setup(bot):
    bot.add_cog(CommandError(bot))
