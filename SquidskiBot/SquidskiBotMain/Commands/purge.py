import asyncio
import discord
from LoggingModule import LoggingModule

class purge():
    adminRoleID = "574763874201501696"

    # Administrator only. Can purge messages with globalCall + purge + (num of messages)
    async def purger(self, msg):
        log = LoggingModule()
        shortened = str(msg.content.lower().split(" ")[1])
        if self.adminRoleID in str(msg.author.roles):
            await msg.channel.purge(limit=(int(shortened) + 1))
            await msg.channel.send("Purged " + shortened + " messages.")
            await log.logIt(f"Purged {shortened} messages in {msg.channel}", msg)
            await asyncio.sleep(3)
            await msg.channel.purge(limit=1)
            await log.logIt("Deleted purge message", msg)
        else:
            await msg.channel.send("You must have the `Administrator` role to do this...")
            await log.logIt(f"Bad user tried to use the purge command...", msg)

