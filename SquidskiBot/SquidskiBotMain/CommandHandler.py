import discord
import sys

# Makes the commands section work
sys.path.append('./Commands')

# Commands
from bruhmoment import bruhmoment
from help import help
from pings import pings
from purge import purge
from seinfeldme import seinfeldme
from sws import sws

class CommandHandler():
    async def commandParser(self, message, globalCall):

        # Help message
        if (message.content.lower() == globalCall + "help"):
            myHelp = help()
            await message.channel.send(embed = myHelp.myEmbed())
            print("Sent help message for " + str(message.author))

        # Search workshop
        if (message.content.startswith((globalCall + 'sws'))):
            searchWorkshop = sws()
            await message.channel.send("Searching the workshop. Please wait...")
            searchIt = searchWorkshop.theMain(message.content)
            if not searchIt:
                await message.channel.send("That's a fat error from me dawg. The search came up empty.")
            else:
                await message.channel.send(searchIt)

        # Get random Seinfeld quote
        if (message.content.startswith((globalCall + 'seinfeldme'))):
            getSeinfeldQuote = seinfeldme()
            await message.channel.send(getSeinfeldQuote.getQuote())
            print("Sent a Seinfeld quote for " + str(message.author))

        # Give/Remove Pings role
        if (message.content.lower().startswith((globalCall + 'pings'))):
            myPings = pings()
            await myPings.changePingRoleState(message)

        # Purge messages (Administrator Only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            myPurge = purge()
            await myPurge.purger(message)

        # Checks if is bruh moment
        if (message.content.lower().startswith((globalCall + 'bruhmoment'))):
            myBruh = bruhmoment()
            await myBruh.isBruhMoment(message)