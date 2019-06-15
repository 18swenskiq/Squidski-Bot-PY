import asyncio
import discord

class mute():
    
    async def mute_users(self,message):
        await message.mentions[0].add_roles(discord.utils.get(message.guild.roles, name='Muted'))
        if(message.content.split(" ")[2] == 1):
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minute.")
        else:
            await message.channel.send("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minutes.")
        print("Muted " + str(message.mentions[0]) + " for " + message.content.split(" ")[2] + " minutes.")
        await asyncio.sleep(int(message.content.split(" ")[2]) * 60)
        await message.mentions[0].remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
        print(str(message.mentions[0]) + " is now unmuted.")
        await message.channel.send(str(message.mentions[0]) + " has been unmuted. Please be a good user.")
