import discord, json, subprocess, sys
import discord.ext.commands as client


class Developer(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    def is_dev(self, id):
        return id in json.loads(open("config.json",'r').read())["devs"]

    @client.command()
    async def shutdown(self,ctx):
        if not self.is_dev(ctx.author.id):
            return
        color = self.bot.character.color
        e = discord.Embed(title = "Shutting the dokis...", color=int(color, base=16))
        await ctx.send(embed=e)
        await self.bot.change_presence(status=discord.Status.dnd)
        print(f"bots got shut down by {ctx.author.name}!")
        await quit()

    @client.command()
    async def restart(self,ctx):
        if not self.is_dev(ctx.author.id):
            return
        color = self.bot.character.color
        e = discord.Embed(title = "Restarting the dokis...", color=int(color, base=16))
        await ctx.send(embed=e)
        await self.bot.change_presence(status=discord.Status.idle)
        print(f"bots got restarted by {ctx.author.name}!")
        subprocess.call([sys.executable, f"DDLC.py"])
        await quit()

def setup(bot):
    bot.add_cog(Developer(bot))