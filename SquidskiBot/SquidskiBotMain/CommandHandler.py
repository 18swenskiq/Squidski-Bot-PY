import discord
import sys
from LoggingModule import LoggingModule

# Makes the commands section work
sys.path.append('./Commands')

# Commands
from apiworkshopsearch import apiworkshopsearch
from bruhmoment import bruhmoment
from fanfic import fanfic
from help import help
from helpadmin import helpadmin
from mute import mute
from pings import pings
from purge import purge
from rolepinger import rolepinger
from seinfeldme import seinfeldme
from sws import sws

class CommandHandler():
    async def commandParser(self, message, globalCall):

        # Help message
        if (message.content.lower() == globalCall + "help"):
            myHelp = help()
            await message.channel.send(embed = myHelp.myEmbed())
            log.logMessage("Sent help message for " + str(message.author))

        # Search workshop
        if (message.content.startswith((globalCall + 'sws'))):
            searchWorkshop = sws()
            await message.channel.send("Searching the workshop. Please wait...")
            searchIt = searchWorkshop.theMain(message.content)
            if not searchIt:
                await message.channel.send("That's a fat error from me dawg. The search came up empty.")
                log.logMessage(f"Workshop search came up empty for {message.content}")
            else:
                await message.channel.send(searchIt)

        # Get random Seinfeld quote
        if (message.content.startswith((globalCall + 'seinfeldme'))):
            getSeinfeldQuote = seinfeldme()
            await message.channel.send(getSeinfeldQuote.getQuote())
            log.logMessage("Sent a Seinfeld quote for " + str(message.author))

        # Give/Remove Pings role
        if (message.content.lower().startswith((globalCall + 'pings'))):
            myPings = pings()
            await myPings.changePingRoleState(message)

        # Admin only commands (Administrator only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "helpadmin")):
            myAdminCommands = helpadmin()
            await myAdminCommands.checkPerms(message)

        # Purge messages (Administrator Only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            myPurge = purge()
            await myPurge.purger(message)

        # Ping the Pings role (Administrator Only)
        if (message.content.lower().startswith((globalCall + 'rolepinger'))):
            myPinger = rolepinger()
            await myPinger.pinger(message)

        # Mute a bad user (Administrator Only)
        if (message.content.lower().startswith((globalCall + 'mute'))):
            myMuter = mute()
            await myMuter.mute_users(message)

        # Checks if is bruh moment
        if (message.content.lower().startswith((globalCall + 'bruhmoment'))):
            myBruh = bruhmoment()
            await myBruh.isBruhMoment(message)

       # Searches the Steam Workshop via the API
        if (message.content.lower().startswith((globalCall + 'wtest'))):
            mySAPI = apiworkshopsearch()
            args = message.content.split(" ")
            await mySAPI.requestInfo(message, args[1], " ".join(args[2:]))

        # Pulls a random line from the Source Engine fanfictions
        if (message.content.lower().startswith((globalCall + 'fanfic'))):
            getFanfic = fanfic()
            await message.channel.send(embed = getFanfic.getLine())