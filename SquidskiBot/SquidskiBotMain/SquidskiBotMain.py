# Packages
import discord
import sys
import logging

# Various other files
from ChiefMuteInsurance import ChiefMuteInsurance

# Makes the commands section work
sys.path.append('./Commands')

# Commands
from help import help
from pings import pings
from seinfeldme import seinfeldme
from sws import sws

# This string can be modified to change what prefix the bot responds to
globalCall = ">"

# Administrator role ID
adminRoleID = "574763874201501696"

# Initialization alerts
print("The call symbol for the bot is " + globalCall)
print("Successfully imported help command module")
print("Successfully imported pings command module")
print("Successfully imported seinfeldme command module")
print("Successfully imported sws command module")

# Logger setup
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Here's where the magic happens
class MyClient(discord.Client):

    # Checking if message author is the bot
    async def is_me(self, m):
        mybool = m.author == client.user
        return await myBool  

    # Adds Pings role on join
    async def on_member_join(member):
        await member.add_roles(discord.utils.get(message.guild.roles, name='Pings'))
        print(str(member) + " was given the pings role!")

    # Initializes stuff
    async def on_ready(self):
        print('Logged on as', self.user)

    # Respond to messages starts here
    async def on_message(self, message):
        if message.author == self.user:
            return

        # Help message
        if (message.content.lower() == globalCall + "help"):
            myHelp = help()
            await message.channel.send(embed = myHelp.myEmbed())
            print("Sent help message for " + str(message.author))

        # Good night response
        if (message.content.lower() in ["good night","gn","goodnight"]):
            await (message.channel.send("Good night " + str(message.author)[:-5]))

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

        # Mute if ping chief
        if ("<@259158530131623938>" in message.content):
            chiefMute = ChiefMuteInsurance()
            await chiefMute.the_muter(message)

        # Give/Remove Pings role
        if (message.content.lower().startswith((globalCall + 'pings'))):
            myPings = pings()
            await myPings.changePingRoleState(message)

        # Purge messages (Administrator Only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            shortened = str(message.content.lower().split(" ")[1])
            if adminRoleID in str(message.author.roles):
                await message.channel.purge(limit=(int(shortened) + 1))
                await message.channel.send("Purged " + shortened + " messages.")
                print("Purged " + shortened + " messages in " + str(message.channel))
                time.sleep(3)
                await message.channel.purge(limit=1, check=self.is_me)
                print("Deleted purge message")
            else:
                await message.channel.send("You must have the `Administrator` role to do this...")
                print(str(message.author) + " tried to use the purge command...")

# Instantiate client
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
print("Successfully read bot token")
tokenReader.close()
