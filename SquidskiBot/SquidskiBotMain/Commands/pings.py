import discord
from LoggingModule import LoggingModule

class pings():

    # Subscribe or unsubsribe to 'pings' role
    async def changePingRoleState(self, msg):
        log = LoggingModule()
        # Unsubscribes from 'pings' role
        if "579453547976982566" in str(msg.author.roles):
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Removed the 'Pings' role!")
            await log.logIt(f"Removed the 'Pings' role from {msg.author}", msg)
        # Subscribes to 'pings' role
        else:
            await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Added the 'Pings' role!")
            await log.logIt(f"Added the 'Pings' role to {msg.author}", msg)


