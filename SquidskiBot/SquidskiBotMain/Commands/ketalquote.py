import codecs
import discord
import json
import random

class ketalquote():
    async def getQuote(self, message):
        data = json.load(codecs.open('./ketalquotes.json', 'r', 'utf-8-sig'))
        chosenQuote = random.choice(data["quoteList"])
        ketalEmbed = discord.Embed(title="Ketal Quote Generator", color=0x00FFFF)
        ketalEmbed.add_field(name="Quote:", value=chosenQuote["quote"], inline=False)
        ketalEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/342642223470608386/a76db7a1b97642687ebb7a1f015b07a5.png?size=512")
        ketalEmbed.set_footer(text=f'Ketal on {chosenQuote["ketalOn"]}')
        await message.channel.send(embed = ketalEmbed)
