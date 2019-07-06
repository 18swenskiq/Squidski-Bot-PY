import discord

class LoggingModule():

    async def logMessage(self, logText, scope):
        logChannel = scope.guild.get_channel(596857655994089482)
        print(logText)
        await logChannel.send(logText)