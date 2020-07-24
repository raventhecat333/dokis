import discord, json
import discord.ext.commands as client


class Support(client.Cog):

    def __init__(self, bot):
         self.bot = bot

    def is_dev(self, id):
        return id in json.loads(open("config.json",'r').read())["devs"]

    def is_support_server(self, id):
        return id == json.loads(open("config.json",'r').read())["support server"]["invite"]

    @client.command()
    async def announce(self,ctx):
        if not self.is_dev(ctx.author.id) or not self.is_support_server(ctx.guild.id):
            return
        message = ctx.message.content.partition(' ')[2]
        title = message.partition('|')[0]
        desc = message.partition('|')[2]
        color = self.bot.character.color
        e = discord.Embed(title = title, description=desc, color=int(color, base=16))
        e.set_image(url=ctx.message.attachments[0].url)
        await next(c for c in ctx.guild.text_channels if "announcements" in c.name).send("@everyone",embed=e)

def setup(bot):
    bot.add_cog(Support(bot))