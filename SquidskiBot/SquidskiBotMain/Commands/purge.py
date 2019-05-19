import asyncio
import discord

class purge():
    adminRoleID = "574763874201501696"

    async def purger(self, msg):
        shortened = str(msg.content.lower().split(" ")[1])
        if self.adminRoleID in str(msg.author.roles):
            await msg.channel.purge(limit=(int(shortened) + 1))
            await msg.channel.send("Purged " + shortened + " messages.")
            print("Purged " + shortened + " messages in " + str(msg.channel))
            await asyncio.sleep(3)
            await msg.channel.purge(limit=1)
            print("Deleted purge message")
        else:
            await msg.channel.send("You must have the `Administrator` role to do this...")
            print(str(msg.author) + " tried to use the purge command...")

