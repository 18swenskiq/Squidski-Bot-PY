import asyncio
import discord
import json

class CheckIfInVoice():

    async def periodic(self, myClient):
        with open('settings.json') as json_file:
            settingsFile = json.load(json_file)
        # voiceChannel = settingsFile["voiceChannel"]
        myGuild = myClient.guilds[1]
        print(myGuild)
        voiceChannel = discord.utils.get(myGuild.voice_channels, name="General", bitrate=64000)
        voiceRole = discord.utils.get(myGuild.roles, name="In Voice")
        whoHasTheVoiceRole = []
        while True:
            memberList = voiceChannel.members
            for personConnected in memberList:
                if settingsFile["voiceRole"] not in personConnected.roles:
                    await personConnected.add_roles(voiceRole)
                    whoHasTheVoiceRole.append(personConnected)
            for memberInVoiceList in whoHasTheVoiceRole:
                if memberInVoiceList not in memberList:
                    await memberInVoiceList.remove_roles(voiceRole)
            await asyncio.sleep(5)


