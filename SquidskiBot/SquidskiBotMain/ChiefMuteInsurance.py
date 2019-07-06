import asyncio
import discord

from LoggingModule import LoggingModule

class ChiefMuteInsurance():
    
    # If a user pings Ch(i)ef, they are muted (sent to void) for 1 minute
    async def the_muter(self, msg):
        await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Muted'))
        await msg.channel.send("For pinging Ch(i)ef, " + str(msg.author)[:-5] + " has been muted for 1 mintue.")
        log.logMessage(str(msg.author) + " was muted because they pinged Ch(i)ef.")
        await asyncio.sleep(60)
        if("579453547976982566" in str(msg.author.roles)):
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Muted'))
            logCmd.logMessage(str(msg.author) + " was unmuted after 1 minute for muting Ch(i)ef.")
            await msg.channel.send(str(msg.author)[:-5] + " has been unmuted after pinging Ch(i)ef. Please don't ping Ch(i)ef.")
        else:
            await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Muted'))
            log.logMessage("It seems that " + str(msg.author) + " was already unmuted by an admin. No action from me is required")
            


