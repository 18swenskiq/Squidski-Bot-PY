import discord
from LoggingModule import LoggingModule

class rolepinger():
    adminRoleID = "574763874201501696"
    
    async def pinger(self, message):
        # Checks for Admin
         if self.adminRoleID in str(message.author.roles):
             log = LoggingModule()
             # Makes the Pings role mentionable
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=True)
             # Sends ping
             await message.channel.send("<@&579453547976982566>")
             await message.channel.send("*To unsubscribe from pings, type >pings in <#574764733849272347>*")
             # Makes the Pings role unmentionable
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=False)
             await log.logIt(f"Pings role was successfully pinged from {message.channel} called by {message.author}", message)
         else:
            await message.channel.send("You must have the `Administrator` role to do this...")
            await log.logIt(f"{message.author} tried to use the purge command unsucessfully", message)

