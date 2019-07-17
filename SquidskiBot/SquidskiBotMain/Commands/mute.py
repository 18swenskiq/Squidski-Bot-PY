import asyncio
import discord
import json
from LoggingModule import LoggingModule

class mute():

    # TODO: Clean up this file by making the string f strings as well as not permamuting on >mute with nothing after it
    async def mute_users(self,message):
        log = LoggingModule()
        with open('settings.json') as json_file:
            settingsFile = json.load(json_file)

        if settingsFile["adminRoleId"] not in str(message.author.roles):
            await message.channel.send("You must be an administrator to use this command...")
            return
        await message.mentions[0].add_roles(discord.utils.get(message.guild.roles, name='Muted'))
        if(message.content.split(" ")[2] == "1"):
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minute.")
        else:
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minutes.")
        await log.logIt("Muted "  + str(message.mentions[0]) + " for " + str(message.content.split(" ")[2]) + " minutes.", message)
        await asyncio.sleep(int(message.content.split(" ")[2]) * 60)
        if (settingsFile["mutedRole"] in str(message.mentions[0].roles)):
            await message.mentions[0].remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
            await log.logIt(f"{message.mentions[0]} is now unmuted.", message)
            await message.channel.send(str(message.mentions[0]) + " has been unmuted. Please be a good user.")
        else:
            await log.logIt(f"It seems that {message.mentions[0]} was already unmuted by an admin. No message will be sent by me.", message)
