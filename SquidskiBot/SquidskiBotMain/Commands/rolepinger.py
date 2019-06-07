import discord

class rolepinger():
    adminRoleID = "574763874201501696"
    
    async def pinger(self, message):
         if self.adminRoleID in str(message.author.roles):
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=True)
             await message.channel.send("<@&579453547976982566>")
             await message.channel.send("*To unsubscribe from pings, type >pings in <#574764733849272347>*")
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=False)
         else:
            await message.channel.send("You must have the `Administrator` role to do this...")
            print(str(message.author) + " tried to use the rolepinger command...")

