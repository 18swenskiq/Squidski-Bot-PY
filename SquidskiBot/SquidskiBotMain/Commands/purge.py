import asyncio
import discord
import json
import sys
from LoggingModule import LoggingModule
from ErrorPrintingModule import ErrorPrintingModule

class purge():

    # Administrator only. Can purge messages with globalCall + purge + (num of messages)
    async def purger(self, msg):
        try:
            log = LoggingModule()
            shortened = str(msg.content.lower().split(" ")[1])
            with open('settings.json') as json_file:
                settingsFile = json.load(json_file)

            if settingsFile["adminRoleId"] in str(msg.author.roles):
                await msg.channel.purge(limit=(int(shortened) + 1))
                await msg.channel.send("Purged " + shortened + " messages.")
                await log.logIt(f"Purged {shortened} messages in {msg.channel}", msg)
                await asyncio.sleep(3)
                await msg.channel.purge(limit=1)
                await log.logIt("Deleted purge message", msg)
            else:
                await msg.channel.send("You must have the `Administrator` role to do this...")
                await log.logIt(f"Bad user tried to use the purge command...", msg)
        except:
            e = ErrorPrintingModule()
            await e.reportError(message, sys.exc_info()[0])

