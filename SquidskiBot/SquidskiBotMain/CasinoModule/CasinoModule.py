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
            jsonData = {}
            jsonData['UserData'] = []
            jsonData['UserData'].append({
                'squidCoins': '1000',
                'timesGambled': '0'
            })
            with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                json.dump(jsonData, outfile)
            await message.channel.send("Account Successfully Created! You have been given 1000 Squid Coins to start with. Now onto the gambling.")

        # Now that their stats definitely exist, let's load them up
        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json') as userStats:
            data = json.load(userStats)

        # Command Parser time
        if(len(message.content.split(" ")) == 1):
           await message.channel.send("No parameters were provided. Use `>c help` for a list of possible commands")
           return

        if (message.content.split(" ")[1].lower() == "help"):
            helpEmbed = discord.Embed(title=":moneybag: Squidski's Casino Help Menu :moneybag:", color=0xB22222)
            helpEmbed.add_field(name="Personal Statistics:", value=">c stats" , inline=False)
            helpEmbed.add_field(name="Roulette:", value=">c roulette <bet on number, color, or evens/odds> <coins bet amount>", inline=False)
            await message.channel.send(embed = helpEmbed)
            return

        elif (message.content.split(" ")[1].lower() == "stats"):
            statsEmbed = discord.Embed(title=f":moneybag: {message.author}'s Stats :moneybag:", color=0xB22222)
            statsEmbed.add_field(name="Squid Coins:", value=data["UserData"][0]["squidCoins"], inline=False)
            statsEmbed.add_field(name="Times Gambled:", value=data["UserData"][0]["timesGambled"], inline=False)
            await message.channel.send(embed = statsEmbed)
            return
     
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
                    data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                    if (userBetPhrase == evenOrOdd):
                        await message.channel.send(f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) + (userBetAmount *2)} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) + (userBetAmount * 2))
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        await message.channel.send(f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount)
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                elif(userBetPhrase == "black"):
                    data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                    if (chosenColor.lower() == userBetPhrase):
                        await message.channel.send(f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) + (userBetAmount *2)} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) + (userBetAmount * 2))
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        await message.channel.send(f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount)
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                elif(userBetPhrase == "red"):
                    data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                    if (chosenColor.lower() == userBetPhrase):
                        await message.channel.send(f'Congrats! Your correct bet has netted you {userBetAmount * 2} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) + (userBetAmount *2)} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) + (userBetAmount * 2))
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                        await message.channel.send(f'So close! Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount)
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                else:
                    data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                    if (chosenColor.lower() == userBetPhrase):
                        await message.channel.send(f'Wow! Your correct bet (somehow) has netted you {userBetAmount * 35} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) + (userBetAmount * 35)} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) + (userBetAmount * 35))
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        await message.channel.send(f'Why would you bet on green? Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount)
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
            else:
                data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount * 2)
                if (userBetNumber == rouletteChoice):
                        await message.channel.send(f'Wow! Your correct bet has netted you {userBetAmount * 35} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) + (userBetAmount * 35)} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) + (userBetAmount * 35))
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
                else:
                        await message.channel.send(f'Betting a singular number is probably not a good idea. Your incorrect bet has lost you {userBetAmount} Squid Coins for a total of {int(data["UserData"][0]["squidCoins"]) - userBetAmount} coins!')
                        data['UserData'][0]['squidCoins'] = str(int(data['UserData'][0]['squidCoins']) - userBetAmount)
                        data['UserData'][0]['timesGambled'] = str(int(data['UserData'][0]['timesGambled']) + 1)
                        os.remove(f'./CasinoModule/CasinoUsers/{currentUser}.json')
                        with open(f'./CasinoModule/CasinoUsers/{currentUser}.json', 'w') as outfile:
                            json.dump(data, outfile)
    
        else:
            await message.channel.send("Your casino command wasn't recognized. Do `>c help` and try again.")