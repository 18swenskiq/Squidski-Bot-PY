import asyncio
import datetime
from datetime import datetime
import discord
import json
from os import listdir
from os import remove
import os.path
import random
class CasinoModule():

    async def commandReciever(self, message):
        # Scan all the user info files
        onlyFiles = [f for f in listdir('./CasinoModule/CasinoUsers')]
        onlyFiles = [os.path.splitext(x)[0] for x in onlyFiles]
        currentUser = str(message.author.id)

         # If the user has never used the casino, it will automatically make an account for them
        if(currentUser not in onlyFiles):
            await message.channel.send("You do not appear to have an account. Please wait a second while I open one for you.")
            jsonData = self.buildBaseJsonStats('100', '0', '0')
            self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', jsonData)
            await message.channel.send("Account Successfully Created! You have been given 1000 Squid Coins to start with. Now onto the gambling.")
        
        # Now that their stats definitely exist, let's load them up
        data = self.readFromFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json')

        # If still on version 1 (or 2) of the JSON data, upgrade it
        if ('versionNumber' not in data["UserData"][0]):
            await message.channel.send("Outdated user stats JSON detected. Upgrading...")
            updatedJson = self.buildBaseJsonStats(data["UserData"][0]["squidCoins"], data["UserData"][0]["timesGambled"], "0")
            self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', updatedJson)
            data = self.readFromFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json')
        else:
            if data["UserData"][0]["versionNumber"] == "v2":
                await message.channel.send("Outdated user stats JSON detected. Upgrading...")
                updatedJson = self.buildBaseJsonStats(data["UserData"][0]["squidCoins"], data["UserData"][0]["timesGambled"], "0")
                self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', updatedJson)
                data = self.readFromFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json')

        # Rate Limiting (Fuck you Peaches and Slimek for making this necessary)
        print(datetime.now())
        elapsedTime = datetime.now() - datetime.strptime(data["UserData"][0]["lastUsed"], "%Y-%m-%d %H:%M:%S.%f")
        elapsedTime = divmod(elapsedTime.days * 86400 + elapsedTime.seconds, 60)
        if (elapsedTime[1] < 2):
            await asyncio.sleep(.25)
            await message.channel.send("You have been rate limited! Please try again, but don't spam the command please k thx")
            return

        # Command Parser time
        if(len(message.content.split(" ")) == 1):
           await message.channel.send("No parameters were provided. Use `>c help` for a list of possible commands")
           return

        # Help Embed
        if (message.content.split(" ")[1].lower() == "help"):
            helpEmbed = discord.Embed(title=":moneybag: Squidski's Casino Help Menu :moneybag:", color=0xB22222)
            helpEmbed.add_field(name="Personal Statistics:", value=">c stats" , inline=False)
            helpEmbed.add_field(name="Roulette:", value=">c roulette <bet on number, color, or evens/odds> <coins bet amount>", inline=True)
            helpEmbed.add_field(name="Slots:", value=">c slots <2, 5, or 10>", inline=True)
            helpEmbed.add_field(name="Reset Coins to 100:", value=">c resetcoins", inline=False)
            await message.channel.send(embed = helpEmbed)
            return

        # Stats Embed
        elif (message.content.split(" ")[1].lower() == "stats"):
            statsEmbed = discord.Embed(title=f":moneybag: {message.author}'s Stats :moneybag:", color=0xB22222)
            statsEmbed.add_field(name="Squid Coins:", value=data["UserData"][0]["squidCoins"], inline=False)
            statsEmbed.add_field(name="Times Gambled:", value=data["UserData"][0]["timesGambled"], inline=True)
            statsEmbed.add_field(name="Coins Lost:", value=data["UserData"][0]["coinsLost"], inline=True)
            await message.channel.send(embed = statsEmbed)
            return
        
        # Roulette
        elif (message.content.split(" ")[1].lower() == "roulette"):
            userBetNumber = 0
            userBetPhrase = "none"
            userBetAmount = 0
            if(not len(message.content.split(" ")) == 4):
                await message.channel.send("Incorrect number of parameters for roulette! Type >c help to view proper syntax.")
                return
            try:
                int(message.content.split(" ")[2])
                if(int(message.content.split(" ")[2]) > 37):
                    await message.channel.send("Number is too high for roulette wheel! Wheel number must be between 1-37 inclusive")
                    return
                elif(int(message.content.split(" ")[2]) == 0):
                    await message.channel.send("0 does not exist on this wheel! Wheel number must be between 1-37 inclusive")
                    return
                else:
                    userBetNumber = int(message.content.split(" ")[2])
            except:
                if(message.content.split(" ")[2].lower() == "black"):
                    userBetPhrase = "black"
                elif(message.content.split(" ")[2].lower() == "red"):
                    userBetPhrase = "red"
                elif(message.content.split(" ")[2].lower() == "green"):
                    userBetPhrase = "green"
                elif(message.content.split(" ")[2].lower() == "evens" or message.content.split(" ")[2].lower() == "even"):
                    userBetPhrase = "evens"
                elif(message.content.split(" ")[2].lower() == "odds" or message.content.split(" ")[2].lower() == "odd"):
                    userBetPhrase = "odds"
                else:
                    await message.channel.send(f'{message.content.split(" ")[2]} is not a valid color or understood phrase on the wheel! Valid colors are black, red, or green (or bet on numbers). Other options are odds or evens.')
                    return
            try:
                int(message.content.split(" ")[3])
                if(int(message.content.split(" ")[3]) < 0):
                    await message.channel.send("You cannot place a negative bet!")
                    return
                if(int(message.content.split(" ")[3]) == 0):
                    await message.channel.send("Bet cannot be 0! Please bet an actual amount and stop wasting the casino's time.")
                    return
                elif(int(message.content.split(" ")[3]) > int(data['UserData'][0]['squidCoins'])):
                    await message.channel.send("You cannot bet more coins than you have! Please place a real bet and stop wasting the casino's time.")
                    return
                userBetAmount = int(message.content.split(" ")[3])
            except:
                await message.channel.send(f'{message.content.split(" ")[3]} is not a valid number! Please place a real bet next time.')
                return
            # Now its time to actually spin the roulette wheel
            rouletteChoice = random.randint(1, 37)
            chosenColor = ""
            evenOrOdd = "evens" if rouletteChoice % 2 == 0 else "odds"
            if(rouletteChoice in [2, 4, 6, 8, 10, 13, 15, 17, 19, 20, 22, 24, 26, 28, 31, 33, 35, 37]):
                chosenColor = "Red"
            elif(rouletteChoice == 1):
                chosenColor = "Green"
            else:
                chosenColor = "Black"

            # Build Roulette Embed
            rouletteEmbed = discord.Embed(title="Roulette Spin", color=0xB22222)
            rouletteEmbed.add_field(name="Number Landed On:", value=rouletteChoice, inline=False)
            rouletteEmbed.add_field(name="Color:", value=chosenColor, inline=False)
            await message.channel.send(embed = rouletteEmbed)

            # Check users bet
            if(userBetNumber is 0):
                # If the bet number is 0, that means they bet with a phrase
                if(userBetPhrase == "odds" or userBetPhrase == "evens"):
                    if (userBetPhrase == evenOrOdd):
                        await self.modifyCoins(message, data, userBetAmount, True, 2, currentUser, f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {(int(data["UserData"][0]["squidCoins"]) - userBetAmount) + (userBetAmount * 2)} coins!')
                    else:
                        await self.modifyCoins(message, data, userBetAmount, False, 0, currentUser, f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                elif(userBetPhrase == "black"):
                    if (chosenColor.lower() == userBetPhrase):
                        await self.modifyCoins(message, data, userBetAmount, True, 2, currentUser, f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {(int(data["UserData"][0]["squidCoins"]) - userBetAmount) + (userBetAmount * 2)} coins!')
                    else:
                        await self.modifyCoins(message, data, userBetAmount, False, 0, currentUser, f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                elif(userBetPhrase == "red"):
                    if (chosenColor.lower() == userBetPhrase):
                        await self.modifyCoins(message, data, userBetAmount, True, 2, currentUser, f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {(int(data["UserData"][0]["squidCoins"]) - userBetAmount) + (userBetAmount * 2)} coins!')
                    else:
                        await self.modifyCoins(message, data, userBetAmount, False, 0, currentUser, f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                else:
                    if (chosenColor.lower() == userBetPhrase):
                        await self.modifyCoins(message, data, userBetAmount, True, 35, currentUser, f'Congrats! Your correct bet has netted you {userBetAmount * 35} Squid Coins for a total of {(int(data["UserData"][0]["squidCoins"]) - userBetAmount) + (userBetAmount * 35)} coins!')
                    else:
                        await self.modifyCoins(message, data, userBetAmount, False, 0, currentUser, f'Why would you bet on green? Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
            else:
                if (userBetNumber == rouletteChoice):
                        await self.modifyCoins(message, data, userBetAmount, True, 35, currentUser, f'Congrats! Your correct bet has netted you {userBetAmount * 35} Squid Coins for a total of {(int(data["UserData"][0]["squidCoins"]) - userBetAmount) + (userBetAmount * 35)} coins!')
                else:
                        await self.modifyCoins(message, data, userBetAmount, False, 0, currentUser, f'Betting a singular number is probably not a good idea. Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')

        # Slots
        elif(message.content.split(" ")[1].lower() == "slots" or message.content.split(" ")[1].lower() == "slot"):
            if(not len(message.content.split(" ")) == 3):
               await message.channel.send("Incorrect number of parameters! Type `>c help` to view the correct usage.")
               return
            if(message.content.split(" ")[2] not in ["2", "5", "10"]):
                await message.channel.send(f"{message.content.split(' ')[2].lower()} is not a valid slot machine! Please pick either 2, 5, or 10")
                return
            with open(f'./CasinoModule/SlotsRollingJackpot.json') as jackpot:
                rollingJackpot = json.load(jackpot)
            slotOne = random.randint(0, 6)
            slotTwo = random.randint(0, 6)
            slotThree = random.randint(0, 6)
            userPayoutMultiplier = 1
            emoteList = [":apple:", ":lemon:", ":tangerine:", ":cherries:", ":grapes:", "<:squidski:581911303791050762>", ":seven:"]
            slotOneEmote = emoteList[slotOne]
            slotTwoEmote = emoteList[slotTwo]
            slotThreeEmote = emoteList[slotThree]
            if(slotOne == slotTwo == slotThree): 
                userPayoutMultiplier = [10, 25, 50, 100, 250, 500, 1000][slotOne]
                if(slotOne in [4, 5, 6]):
                    newJackpot = {}
                    newJackpot["rollingJackpot"] = "0"
                    self.writeToFileGeneric(f'./CasinoModule/SlotsRollingJackpot.json', newJackpot)
                    slotEmbed = discord.Embed(title=":moneybag: Squidski's Casino Slot Menu :moneybag:", color=0xB22222)
                    slotEmbed.add_field(name="Spin:", value=f"{slotOneEmote} - {slotTwoEmote} - {slotThreeEmote}" , inline=False)
                    slotEmbed.add_field(name="Current Jackpot:", value=int(rollingJackpot["rollingJackpot"]) + int(message.content.split(" ")[2]), inline=False)
                    await message.channel.send(embed = slotEmbed)
                    await self.modifyCoins(message, data, 1, True, int(rollingJackpot["rollingJackpot"]) + 1, currentUser, f'You have won the jackpot and won {int(rollingJackpot["rollingJackpot"]) + int(message.content.split(" ")[2])} additional Squidcoins! The jackpot has been reset to 0')
                    await self.modifyCoins(message, data, int(message.content.split(" ")[2]), True, userPayoutMultiplier, currentUser, f"Congrats! You've won {int(message.content.split(' ')[2]) * userPayoutMultiplier} Squidcoins!")
                else:
                    slotEmbed = discord.Embed(title=":moneybag: Squidski's Casino Slot Menu :moneybag:", color=0xB22222)
                    slotEmbed.add_field(name="Spin:", value=f"{slotOneEmote} - {slotTwoEmote} - {slotThreeEmote}" , inline=False)
                    slotEmbed.add_field(name="Current Jackpot:", value=int(rollingJackpot["rollingJackpot"]) + int(message.content.split(" ")[2]), inline=False)
                    await message.channel.send(embed = slotEmbed)
                    await self.modifyCoins(message, data, int(message.content.split(" ")[2]), True, userPayoutMultiplier, currentUser, f"Congrats! You've won {int(message.content.split(' ')[2]) * userPayoutMultiplier} Squidcoins!")
            else:
                slotEmbed = discord.Embed(title=":moneybag: Squidski's Casino Slot Menu :moneybag:", color=0xB22222)
                slotEmbed.add_field(name="Spin:", value=f"{slotOneEmote} - {slotTwoEmote} - {slotThreeEmote}" , inline=False)
                slotEmbed.add_field(name="Current Jackpot:", value=int(rollingJackpot["rollingJackpot"]) + int(message.content.split(" ")[2]), inline=False)
                await message.channel.send(embed = slotEmbed)
                newJackpot = {}
                newJackpot["rollingJackpot"] = int(rollingJackpot["rollingJackpot"]) + int(message.content.split(" ")[2])
                self.writeToFileGeneric(f'./CasinoModule/SlotsRollingJackpot.json', newJackpot)
                await self.modifyCoins(message, data, int(message.content.split(" ")[2]), False, 0, currentUser, f"Try again, and better luck next time! You lost {message.content.split(' ')[2]} Squidcoins!")

        # Reset coins to 100
        elif(message.content.split(" ")[1].lower() == "resetcoins"):
            newData = self.buildBaseJsonStats("100", data["UserData"][0]["timesGambled"], data["UserData"][0]["coinsLost"])
            self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', newData)
            await message.channel.send("Number of coins reset to 100!")
        else:
            await message.channel.send("Your casino command wasn't recognized. Do `>c help` and try again.")

    async def modifyCoins(self, dMessage, dataObj, userBetAmount, isWin, multiplier, currentUser, mMessage):
        if(isWin):
            await dMessage.channel.send(mMessage)
            dataObj['UserData'][0]['squidCoins'] = str((int(dataObj['UserData'][0]['squidCoins']) - userBetAmount) + (userBetAmount * multiplier))
            dataObj['UserData'][0]['timesGambled'] = str(int(dataObj['UserData'][0]['timesGambled']) + 1)
            dataObj['UserData'][0]['coinsLost'] = dataObj['UserData'][0]['coinsLost']
            dataObj['UserData'][0]['lastUsed'] = str(datetime.now())
            dataObj['UserData'][0]['versionNumber'] = dataObj['UserData'][0]['versionNumber']
            self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', dataObj)
            return
        else:
            await dMessage.channel.send(mMessage)
            dataObj['UserData'][0]['squidCoins'] = str(int(dataObj['UserData'][0]['squidCoins']) - userBetAmount)
            dataObj['UserData'][0]['timesGambled'] = str(int(dataObj['UserData'][0]['timesGambled']) + 1)
            dataObj['UserData'][0]['coinsLost'] = str(int(dataObj['UserData'][0]['coinsLost']) + userBetAmount)
            dataObj['UserData'][0]['lastUsed'] = str(datetime.now())
            dataObj['UserData'][0]['versionNumber'] = dataObj['UserData'][0]['versionNumber']
            self.writeToFileGeneric(f'./CasinoModule/CasinoUsers/{currentUser}.json', dataObj)
            return

    def writeToFileGeneric(self, filePath, dataToWrite):
        os.remove(filePath)
        with open(filePath, 'w') as outfile:
               json.dump(dataToWrite, outfile)

    def readFromFileGeneric(self, filePath):
        with open(filePath) as importedData:
            genericData = json.load(importedData)
        return genericData

    def buildBaseJsonStats(self, squidCoins, timesGambled, coinsLost):
        genericData = {}
        genericData['UserData'] = []
        genericData['UserData'].append({
            'squidCoins': f'{squidCoins}',
            'timesGambled': f'{timesGambled}',
            'coinsLost': f'{coinsLost}',
            'lastUsed': f'{datetime.now()}',
            'versionNumber': "v3"
        })
        return 