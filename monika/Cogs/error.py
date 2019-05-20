import traceback, sys, discord, Cogs.checks, chalk
from discord.ext import commands
from Cogs.config import conf

name = conf.name
ver = conf.version
eol = conf.err
checks = Cogs.checks

class CommandErrorHandler(commands.Cog):
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
 
        elif isinstance(error, checks.dev_only):
            return

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Better ask a Club President to help with that one! (you need admin to change this setting)")

        else:
            tra = traceback.format_exception_only(type(error), error)
            e = discord.Embed(description=f"`Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this... I think...` ```py\n%s\n```" % ''.join(tra), file=sys.stderr, color=eol)
            e.set_author(name="That's an issue!",icon_url=ctx.message.author.avatar_url)
            e.set_footer(text=ver)
            await ctx.send(embed=e)




def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
