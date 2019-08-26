import discord

class help():

    # Builds a discord embed object to display as the help message
    async def myEmbed(self, message):
        embed = discord.Embed(title="Squidski-Bot PY", description="I am a bot made by Squidski#9545. I can do multiple things and I am still in development", color=0x00ff00)
        embed.add_field(name="Search Workshop", value=">sws <game> <type> <search term>", inline=False)
        embed.add_field(name="Get Random Seinfeld Quote", value=">seinfeldme", inline=False)
        embed.add_field(name="Subscribe or Unsubscribe from pings", value=">pings", inline=False)
        embed.add_field(name="Check if something is a bruh moment", value=">bruhmoment", inline=False)
        embed.add_field(name="Get a random fact about Squidski", value=">squidskifact", inline = False)
        embed.add_field(name="Get a random line from an SE Discord fanfic", value=">fanfic", inline = False)
        embed.add_field(name="Get a ketal quote", value=">ketalquote", inline= False)
        embed.add_field(name="Admin only commands", value=">helpadmin",inline=False)
        await message.channel.send(embed = embed)


