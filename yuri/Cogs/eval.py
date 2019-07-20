import discord, random, asyncio, Cogs.checks, io, textwrap, traceback
from discord.ext import commands as client
from Cogs.config import conf
from contextlib import redirect_stdout
#Imports

checks = Cogs.checks

class Eval(client.Cog):

    def __init__(self, bot):
         self.b = bot 
         self._last_result = None


    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')


    @client.command()
    @checks.dev()
    async def eval(self, ctx, *, message: str):
        env = {
            'bot': self.b,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(message)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                pass
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')



                
def setup(bot):
    bot.add_cog(Eval(bot))