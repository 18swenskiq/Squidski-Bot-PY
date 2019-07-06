import discord

class helpadmin():
    adminRoleID = "574763874201501696"

    async def checkPerms(self,message):
        if self.adminRoleID in str(message.author.roles):
            await message.channel.send(embed = self.myEmbed())
        else:
            await message.channel.send("Only admins are allowed to see the secret admin commands.")


    def myEmbed(self):
        embed = discord.Embed(title="Squidski-Bot PY", description="Welcome to the secret admin help", color=0x00ff00)
        embed.add_field(name="Mute bad users", value=">mute <user> <minutes>", inline=False)
        embed.add_field(name="Purge messages", value=">purge <amount of messages>", inline=False)
        embed.add_field(name="Ping the pings role", value=">rolepinger", inline=False)
        return embed

