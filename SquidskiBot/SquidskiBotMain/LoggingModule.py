import datetime
import discord

class LoggingModule():

    async def logIt(self, tMessage, dMessage):
        print(tMessage)
        logChannel = dMessage.guild.get_channel(596857655994089482)

        # We need this to see if the bot is currently starting up, or we are performing normal functions now
        invokingUser = ""
        try:
            invokingUser = dMessage.author
        except:
            invokingUser = "Bot Startup"

        # Still checking for bot startup here
        invokingChannel = ""
        try:
            invokingChannel = dMessage.channel
        except:
            invokingChannel = "Bot Startup"

        embed = discord.Embed(title="**Squidbot Logs**", color=0x9370DB)
        embed.add_field(name="Logged Message:", value=f"`{tMessage}`", inline=False)
        embed.add_field(name="Invoking User:", value=f"`{invokingUser}`", inline=False)
        embed.add_field(name="In Channel:", value=f"`{invokingChannel}`", inline=False)
        embed.set_footer(text=f"{datetime.datetime.now()}")

        await logChannel.send(embed = embed)
