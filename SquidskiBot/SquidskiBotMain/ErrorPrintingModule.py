import datetime
import discord
import json

class ErrorPrintingModule(object):
    
    async def reportError(self, message, e):
        with open('settings.json') as json_file:
            settingsFile = json.load(json_file)

        logChannel = message.guild.get_channel(settingsFile["loggingChannel"])


        embed = discord.Embed(title="**Squidbot Error:**", color=0xFF0000)
        embed.add_field(name="Error Message:", value=f"{e}", inline=False)
        embed.add_field(name="Invoking User:", value=f"{message.author}", inline=False)
        embed.add_field(name="In Channel:", value=f"{message.channel}", inline=False)
        embed.add_field(name="Message ID:", value=f"{message.id}")
        embed.set_footer(text=f"{datetime.datetime.now()}")

        await logChannel.send("<@66318815247466496>")
        await logChannel.send(embed = embed)
