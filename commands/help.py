import discord, re, rstr
import discord.ext.commands as client
from datetime import datetime

class Help(client.Cog):

    def __init__(self, bot):
         self.bot = bot
         self.file = open("changelog.txt", "r").read()

    @client.command(pass_context=True, aliases=['manual'])
    async def help(self,ctx):
        color = self.bot.character.color
        value = ctx.message.content.partition(' ')[2]
        helps = self.bot.character.help

        if re.search("commands?", value.lower(), re.IGNORECASE):
            e = discord.Embed(title = f"Manual of {self.bot.name.lower()}.chr! Commands!",
            description = f"Commands are actions to interact with {self.bot.name}, either directly or through cmd.",
            color = int(color, base=16))
            commands = []
            for i in helps["commands"]:
                commands.append(f"**{i}**: {helps['commands'][i]}")
            commands = '\n'.join(commands)
            e.add_field(name = "Commands", value = f"{commands}", inline = False)
            e.set_footer(text = f"Thanks for reading!", icon_url = self.bot.user.avatar_url)

        elif re.search("phrases?", value.lower(), re.IGNORECASE):
            e = discord.Embed(title = f"Manual of {self.bot.name.lower()}.chr! Phrases!",
            description = f"Phrases are variants of words to talk with {self.bot.name}, to talk, mention {self.bot.name} at the beginning.",
            color = int(color, base=16))
            phrases = []
            for i in helps["phrases"]:
                phrases.append(f"**{i}**: {helps['phrases'][i]}")
            phrases = '\n'.join(phrases)
            e.add_field(name = "Phrases", value = f"{phrases}", inline = False)
            e.set_footer(text = f"Thanks for reading!", icon_url = self.bot.user.avatar_url)

        elif re.search("triggers?", value.lower(), re.IGNORECASE):
            e = discord.Embed(title = f"Manual of {self.bot.name.lower()}.chr! Triggers!",
            description = f"Trigger words are words that {self.bot.name} reacts to, it can be toggled on and off using ``{rstr.xeger(self.bot.character.prefix)}trigger``.",
            color = int(color, base=16))
            e.add_field(name = "Triggers", value = f"``{'`` ``'.join(helps['triggers'])}``", inline = False)
            e.set_footer(text = f"Thanks for reading!", icon_url = self.bot.user.avatar_url)

        else:
            e = discord.Embed(title = f"Manual of {self.bot.name.lower()}.chr!",
            description = f"{self.bot.character.description}",
            color = int(color, base=16))
            e.add_field(name = "Commands", value = f"Commands are actions to interact with {self.bot.name}, either directly or through cmd, to know what commands you can use, write ``{rstr.xeger(self.bot.character.prefix)}help commands``.", inline = False)
            e.add_field(name = "Phrases", value = f"Phrases are variants of words to talk with {self.bot.name}, to talk, mention {self.bot.name} at the beginning, to know what you can say to {self.bot.name}, write ``{rstr.xeger(self.bot.character.prefix)}help phrases``.", inline = False)
            e.add_field(name = "Triggers", value = f"Trigger words are words that {self.bot.name} reacts to, it can be toggled on and off using ``{rstr.xeger(self.bot.character.prefix)}trigger``, to know what trigger words there are, write ``{rstr.xeger(self.bot.character.prefix)}help triggers``.", inline = False)
            e.add_field(name = "Got a suggestion or bug report?", value = f"[Click here to tell the devs about it](https://support.dokis.dev/) or [join the support server](https://discord.gg/a2ePdNf).", inline = False)
            e.set_footer(text = f"Thanks for reading!", icon_url = self.bot.user.avatar_url)
            
        await ctx.send(embed=e)

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
