import discord, json, sys, traceback
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class CommandError(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    @client.Cog.listener()
    async def on_command_error(self,ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance(error, client.CommandNotFound) or isinstance(error, client.CheckFailure) or isinstance(error, client.CommandOnCooldown):
            return

        elif isinstance(error, client.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")

        elif isinstance(error, client.NoPrivateMessage):
            await ctx.send("This command only works on servers.")

        else:
            tra = traceback.format_exception_only(type(error), error)
            config = json.loads(open("config.json", "r").read())
            color = config["colors"]["error"]
            e = discord.Embed(title = "An exception has occurred.", description = f"Unexpected error has occured.\n{''.join(tra)}\n\nIf you want to assure this error won't happen again. Please report this by [clicking here!](https://forms.gle/hJ3KHVwKMFzfs5eq9)", file=sys.stderr, color=int(color, base=16))
            await ctx.send(embed=e)
            print(f"Warning! The command '{ctx.command}' has just Errored!")
            print(f"Traceback: {''.join(tra)}")

def setup(bot):
    bot.add_cog(CommandError(bot))
