import discord
import json
from LoggingModule import LoggingModule

class rolepinger():

    async def pinger(self, message):
        # Checks for Admin
         with open('settings.json') as json_file:
            settingsFile = json.load(json_file)
         if settingsFile["adminRoleId"] in str(message.author.roles):
             log = LoggingModule()
             # Makes the Pings role mentionable
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=True)
             # Sends ping
             await message.channel.send(f'<@&{settingsFile["notificationsRole"]}>')
             await message.channel.send(f'*To unsubscribe from pings, type >pings in <#{settingsFile["botChannel"]}>*')
             # Makes the Pings role unmentionable
             await (discord.utils.get(message.guild.roles, name='Pings')).edit(mentionable=False)
             await log.logIt(f"Pings role was successfully pinged", message)
         else:
            await message.channel.send("You must have the `Administrator` role to do this...")
            await log.logIt(f"Bad user tried to use the purge command unsucessfully", message)

