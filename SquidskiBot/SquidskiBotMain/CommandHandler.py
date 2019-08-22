import discord
import sys

# Makes the Commands and CSharp layers sections work
sys.path.append('./CasinoModule')
sys.path.append('./Commands')
sys.path.append('./csLayers')

# Commands
from apiworkshopsearch import apiworkshopsearch
from CasinoModule import CasinoModule
from bruhmoment import bruhmoment
from currency import currency
from fanfic import fanfic
from help import help
from helpadmin import helpadmin
from mute import mute
from pings import pings
from purge import purge
from rolepinger import rolepinger
from seinfeldme import seinfeldme
from squidskifact import squidskifact
from sws import sws

# CSharp Layers
from VDCsearch import VDCsearch


class CommandHandler():
    async def commandParser(self, message, globalCall):

        # Casino Module
        if (message.content.lower().startswith(globalCall + "c ")):
            gambleTime = CasinoModule()
            await gambleTime.commandReciever(message)
            return

        # Help message
        if (message.content.lower() == globalCall + "help"):
            myHelp = help()
            await message.channel.send(embed = await myHelp.myEmbed(message))
            return

        # Convert Currency
        if (message.content.lower().startswith(globalCall + "currency")):
            newCurrency = currency()
            await newCurrency.currencyConverter(message)
            return

        # Search workshop
        if (message.content.startswith((globalCall + 'sws'))):
            searchWorkshop = sws()
            await message.channel.send("Searching the workshop. Please wait...")
            searchIt = searchWorkshop.theMain(message.content)
            if not searchIt:
                await message.channel.send("That's a fat error from me dawg. The search came up empty.")
                return
            else:
                await message.channel.send(searchIt)
                return

        # Get random Seinfeld quote
        if (message.content.startswith((globalCall + 'seinfeldme'))):
            getSeinfeldQuote = seinfeldme()
            await getSeinfeldQuote.getQuote(message)
            return

        # Get random Squidski fact
        if (message.content.startswith((globalCall + 'squidskifact'))):
            squidFact = squidskifact()
            await message.channel.send(embed = await squidFact.getQuote(message))
            return

        # Give/Remove Pings role
        if (message.content.lower().startswith((globalCall + 'pings'))):
            myPings = pings()
            await myPings.changePingRoleState(message)
            return

        # Admin only commands (Administrator only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "helpadmin")):
            myAdminCommands = helpadmin()
            await myAdminCommands.checkPerms(message)
            return

        # Purge messages (Administrator Only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            myPurge = purge()
            await myPurge.purger(message)
            return

        # Ping the Pings role (Administrator Only)
        if (message.content.lower().startswith((globalCall + 'rolepinger'))):
            myPinger = rolepinger()
            await myPinger.pinger(message)
            return

        # Mute a bad user (Administrator Only)
        if (message.content.lower().startswith((globalCall + 'mute'))):
            myMuter = mute()
            await myMuter.mute_users(message)
            return

        # Checks if is bruh moment
        if (message.content.lower().startswith((globalCall + 'bruhmoment'))):
            myBruh = bruhmoment()
            await myBruh.isBruhMoment(message)
            return

       # Searches the Steam Workshop via the API
        if (message.content.lower().startswith((globalCall + 'wtest'))):
            mySAPI = apiworkshopsearch()
            args = message.content.split(" ")
            await mySAPI.requestInfo(message, args[1], " ".join(args[2:]))
            return

        # Pulls a random line from the Source Engine fanfictions
        if (message.content.lower().startswith((globalCall + 'fanfic'))):
            getFanfic = fanfic()
            await message.channel.send(embed = await getFanfic.getLine(message))
            return

        # Search VDC
        if (message.content.lower().startswith((globalCall + 'v'))):
            searchVDC = VDCsearch()
            await searchVDC.searchTheVDC(message)
            return