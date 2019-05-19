import discord

class pings():

    async def changePingRoleState(self, msg):
        if "579453547976982566" in str(msg.author.roles):
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Removed the 'Pings' role!")
            print("Removed the 'pings' role from " + str(msg.author))
        else:
            await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Pings'))
            await msg.channel.send("Added the 'Pings' role!")
            print("Added the 'pings' role to " + str(msg.author))


