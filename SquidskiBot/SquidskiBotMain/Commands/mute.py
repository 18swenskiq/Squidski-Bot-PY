import asyncio
import discord
import json
import sys


class mute():

    # TODO: Fix the crashing of the task when you do >mute with none or not enough parameters
    async def mute_users(self,message):
        with open('settings.json') as json_file:
            settingsFile = json.load(json_file)

        # If user is not an admin, they can't mute
        if settingsFile["adminRoleId"] not in str(message.author.roles):
            await message.channel.send("You must be an administrator to use this command...")
            return

        # If you don't provide a name and time, then the person won't be muted
        if len(message.content.split(" ")) < 3:
            await message.channel.send("You didn't provide enough arguments to properly mute someone.")
            return

        # If the mute duration isn't an actual number, then don't mute
        if not message.content.split(" ")[2].isdigit():
            await message.channel.send("A valid mute time was not provided.")
            return

        await message.mentions[0].add_roles(discord.utils.get(message.guild.roles, name='Muted'))

        # Decides whether to use minute or minutes in the message
        if(message.content.split(" ")[2] == "1"):
            await message.channel.send(f'Muted {message.mentions[0]} for {message.content.split(" ")[2]} minute.')
        else:
            await message.channel.send(f'Muted {message.mentions[0]} for {message.content.split(" ")[2]} minutes.')

        # Keep the user muted for however long we picked in minutes
        await asyncio.sleep(int(message.content.split(" ")[2]) * 60)

        # Unmute the user
        if (settingsFile["mutedRole"] in str(message.mentions[0].roles)):
            await message.mentions[0].remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
            await message.channel.send(f"{message.mentions[0]} has been unmuted. Please be a good user.")