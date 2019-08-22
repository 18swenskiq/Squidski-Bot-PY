import discord
import json
import http3

class currency():
    async def currencyConverter(self, message):
        messageArray = message.content.split(" ")
        if(not len(message.content.split(" ")) == 3):
           await message.channel.send("Incorrect number of parameters! Format currency requests as `>currency <amount> <currency code>`")
           return
        try:
            int(message.content.split(" ")[1])
        except:
            await message.channel.send(f"{message.content.split(' ')[1]} is not a valid number!")
            return
        if(message.content.split(" ")[2].upper() not in ["CAD", "HKD","ISK","PHP","DKK","HUF","CZK","AUD","RON","SEK","IDR","INR","BRL","RUB","HRK","JPY","THB","CHF","EUR","SGD","PLN","BGN","TRY","CNY","NOK","NZD","ZAR","USD","MXN","ILS","GBP","KRW","MYR"]):
            await message.channel.send(f"{message.content.split(' ')[2]} is an unknown currency type!")
            return
        await message.channel.send("Making GET request, please hold...")
        curStats = await self.makeTheRequest(message.content.split(" "))
        USD = round(curStats["rates"]["USD"] * int(messageArray[1]), 2)
        AUD = round(curStats["rates"]["AUD"] * int(messageArray[1]), 2)
        ZAR = round(curStats["rates"]["ZAR"] * int(messageArray[1]), 2)
        BGN = round(curStats["rates"]["BGN"] * int(messageArray[1]), 2)
        PLN = round(curStats["rates"]["PLN"] * int(messageArray[1]), 2)
        NZD = round(curStats["rates"]["NZD"] * int(messageArray[1]), 2)
        GBP = round(curStats["rates"]["GBP"] * int(messageArray[1]), 2)
        EUR = int(message.content.split(" ")[1])
        if ("EUR" in curStats["rates"]): EUR = round(curStats["rates"]["EUR"] * int(messageArray[1]), 2)
        sendMessage = f"```py\nConverting {message.content.split(' ')[1]} {message.content.split(' ')[2].upper()}:\n"
        sendMessage += f"United States Dollar: {USD}\n"
        sendMessage += f"Australian Dollar:    {AUD}\n"
        sendMessage += f"South African Rand:   {ZAR}\n"
        sendMessage += f"Bulgarian Lev:        {BGN}\n"
        sendMessage += f"Polish złoty:         {PLN}\n"
        sendMessage += f"New Zealand Dollar:   {NZD}\n"
        sendMessage += f"Euro:                 {EUR}\n"
        sendMessage += f"Great Britain Pound:  {GBP}\n"
        sendMessage += "```"
        await message.channel.send(sendMessage)       
        
    async def makeTheRequest(self, infoList):
        client = http3.AsyncClient()
        response = await client.get(f"https://api.exchangeratesapi.io/latest?base={infoList[2].upper()}")
        responseData = response.text
        responseData = json.loads(responseData)
        return responseData