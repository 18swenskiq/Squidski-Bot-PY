import asyncio
import discord

class mute():
    
    adminRoleID = "574763874201501696"

    async def mute_users(self,message):

        if self.adminRoleID not in str(message.author.roles):
            await message.channel.send("You must be an administrator to use this command...")
            return

        await message.mentions[0].add_roles(discord.utils.get(message.guild.roles, name='Muted'))

        if(message.content.split(" ")[2] == "1"):
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minute.")

        else:
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minutes.")

        print("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minutes.")

        await asyncio.sleep(int(message.content.split(" ")[2]) * 60)

        if ("579453547976982566" in str(message.mentions[0].roles)):
            await message.mentions[0].remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
            print(str(message.mentions[0]) + " is now unmuted.")
            await message.channel.send(str(message.mentions[0]) + " has been unmuted. Please be a good user.")

        else:
            print("It seems that " + str(message.mentions[0]) + " was already unmuted by an admin. No message will be sent by me.")
