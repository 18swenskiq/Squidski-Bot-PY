import discord

from LoggingModule import LoggingModule

class pings():

    # Subscribe or unsubsribe to 'pings' role
    async def changePingRoleState(self, msg):
        # Unsubscribes from 'pings' role
        if "579453547976982566" in str(msg.author.roles):
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Removed the 'Pings' role!")
            LoggingModule.logMessage("Removed the 'pings' role from " + str(msg.author))
        # Subscribes to 'pings' role
        else:
            await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Added the 'Pings' role!")
            LoggingModule.logMessage("Added the 'pings' role to " + str(msg.author))


