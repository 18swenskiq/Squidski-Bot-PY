import asyncio
import discord

class ChiefMuteInsurance():
    async def the_muter(self, msg):
        await msg.author.add_roles(discord.utils.get(msg.guild.roles, name='Muted'))
        await msg.channel.send("For pinging Ch(i)ef, " + str(msg.author)[:-5] + " has been muted for 5 mintues.")
        print(str(msg.author) + " was muted because they pinged Ch(i)ef.")
        await asyncio.sleep(300)
        await msg.author.remove_roles(discord.utils.get(msg.guild.roles, name='Muted'))
        print(str(msg.author) + " was unmuted after 5 minutes for muting Ch(i)ef.")
        await msg.channel.send(str(msg.author)[:-5] + " has been unmuted after pinging Ch(i)ef. Please don't ping Ch(i)ef.")

