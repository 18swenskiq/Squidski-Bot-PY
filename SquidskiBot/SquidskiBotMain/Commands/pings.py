import discord
import json
from LoggingModule import LoggingModule

class pings():

    # Subscribe or unsubsribe to 'pings' role
    # TODO: Make it pull the name using the ID, rather than hardcoding the ID
    async def changePingRoleState(self, msg):
        log = LoggingModule()
        with open('settings.json') as json_file:
            settingsFile = json.load(json_file)

        # Unsubscribes from 'pings' role
        if settingsFile["notificationsRole"] in str(msg.author.roles):
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Removed the 'Pings' role!")
            await log.logIt(f"Removed the 'Pings' role", msg)
        # Subscribes to 'pings' role
        else:
            await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Added the 'Pings' role!")
            await log.logIt(f"Added the 'Pings' role", msg)


