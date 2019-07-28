import asyncio
import discord
import json
import sys

class CheckIfInVoice():

    async def periodic(self, myClient):
        try:
            sys.setrecursionlimit(999999999)
            with open('settings.json') as json_file:
                settingsFile = json.load(json_file)
            myGuild = myClient.guilds[1]
            voiceChannel = discord.utils.get(myGuild.voice_channels, name="General", bitrate=64000)
            voiceRole = discord.utils.get(myGuild.roles, name="In Voice")
            whoHasTheVoiceRole = []
            iterations = 0
            while iterations < 5:
                memberList = voiceChannel.members
                for personConnected in memberList:
                    if settingsFile["voiceRole"] not in personConnected.roles:
                        await personConnected.add_roles(voiceRole)
                        whoHasTheVoiceRole.append(personConnected)
                for memberInVoiceList in whoHasTheVoiceRole:
                    if memberInVoiceList not in memberList:
                        await memberInVoiceList.remove_roles(voiceRole)
                await asyncio.sleep(1)
                iterations += 1
            await self.periodic(myClient)

        except:
            await self.periodic(myClient)
