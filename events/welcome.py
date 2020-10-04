import asyncio, discord, random
import discord.ext.commands as client

class Welcome(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_support_server(self, id):
        return id == json.loads(open("config.json",'r').read())["support server"]["invite"]

    @client.Cog.listener()
    async def on_member_join(self, member):
        if member.bot or not self.is_support_server(member.guild.id):
            return
        tampered = await self.bot.checkTamper(message.guild.id if message.guild else message.author.id, type = "guild" if message.guild else "user")
        self.bot.globalCursor.execute(f"INSERT INTO 'currentWelcomer' ('bot','id') SELECT '{random.choice([i['name'] for i in characters])}',{config['support server']['id']} WHERE NOT EXISTS(SELECT bot FROM currentWelcomer WHERE id = {member.guild.id}) LIMIT 1")
        currentWelcomer = self.bot.globalCursor.execute(f"SELECT bot FROM currentWelcomer WHERE id = {member.guild.id}").fetchone()
        print(f"|{currentWelcomer.lower()}|")
        print(f"|{self.bot.name.lower()}|")
        if currentWelcomer.lower() == self.bot.name.lower():
            reply = self.bot.character.welcome(tamper=tampered, member=member)
            await self.bot.send(member.channel, reply)

def setup(bot):
    bot.add_cog(Welcome(bot))