import discord
from LoggingModule import LoggingModule
from ErrorPrintingModule import ErrorPrintingModule

class convert():

    async def convertUnits(self, message):
        try:
            log = LoggingModule()
            userInput = message.content.lower().split(" ")
            if len(userInput) == 1:
                await log.logIt("I wasn't given enough inputs for unit conversion", message)
                await message.channel.send("I was not given an input for unit conversion.")
                return
            userInput = message.content.lower().split(" ")[1]
            acceptedTypes = ["c", "f"]
            if userInput[-1] not in acceptedTypes:
                await log.logIt(f"Attempted to call convert with the input of {userInput} which I don't recognize", message)
                await message.channel.send(f"I am not familiar with that input. My accepted input types are {acceptedTypes}.")
                return
            if userInput[-1] == "c" or userInput[-1] == "f":
                await self.sendConversion(userInput, await self.convertTemp(userInput, message), message)

            else:
                await message.channel.send("You shouldn't see this message")
        except:
            e = ErrorPrintingModule()
            await e.reportError(message, sys.exc_info()[0])

    async def convertTemp(self, userInput, message):
        log = LoggingModule()
        try:
            print(userInput[:-1])
            float(userInput[:-1])
        except ValueError:
            await log.logIt(f"The user input of {userInput} doesn't appear to be valid.", message)
            return "undefined"      

        if userInput[-1] == "c":
            temp = int(userInput[:-1])
            await log.logIt("Conversion between c -> f was successful", message)
            return str((temp * 1.8) + 32) + "f"
        else:
            temp = int(userInput[:-1])
            await log.logIt("Conversion between f -> c was successful", message)
            return str((temp - 32) / 1.8) + "c"

    async def sendConversion(self, userInput, conversion, message):
        log = LoggingModule()
        await message.channel.send(f"`{userInput}` is `{conversion}`")
