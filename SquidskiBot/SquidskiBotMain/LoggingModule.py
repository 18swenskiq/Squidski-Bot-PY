import datetime
import discord

class LoggingModule():

    async def logIt(self, tMessage, dMessage):
        print(tMessage)
        logChannel = dMessage.guild.get_channel(596857655994089482)
        await logChannel.send(f"{tMessage} - {datetime.datetime.now()}")
