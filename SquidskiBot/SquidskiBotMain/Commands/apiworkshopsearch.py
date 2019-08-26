import discord
import json
import http3

class apiworkshopsearch():

    async def requestInfo(self, message, game, term):

        term = term.replace(" ", "+")
        # Get our game's appId (defaults to csgo if input was not known)
        appId = self.getGame(game)

        # Send the first GET request
        print("Getting workshop result #1...")
        client = http3.AsyncClient()
        firstResponse = await client.get(self.urlBuilder("*", appId, term))
        firstResponseData = firstResponse.text
        firstResponseData = json.loads(firstResponseData)
        nextCurs = firstResponseData['response']['next_cursor']

        # Set up some variables
        steamString = "https://steamcommunity.com/sharedfiles/filedetails/?id="
        myArray = []

        # Add our first GET results to the array
        myArray.append(steamString + firstResponseData['response']['publishedfiledetails'][0]['publishedfileid'])

        # Get the next 4 results 
        iters = 2
        try:
            while(iters != 6):
                print(f"Getting workshop result #{iters}")
                re = await client.get(self.urlBuilder(nextCurs, appId, term))
                myRe = re.text
                myRe = json.loads(myRe)
                myArray.append(steamString + myRe['response']['publishedfiledetails'][0]['publishedfileid'])
                nextCurs = myRe['response']['next_cursor']
                iters += 1
        except:
            print("This is a lazy way of dealing with less than 5 results. Should fix later")

        await message.channel.send(embed = self.embedBuilder(myArray, game, term))

    def embedBuilder(self, listResults, app, term):
        embed = discord.Embed(title="Workshop Results", description=f"Your results for {term} in {app}", color=0x00ff00)
        embed.add_field(name="test1",value=(listResults[0] if (len(listResults) > 0) else "No Results found"))
        embed.add_field(name="test2",value=(listResults[1] if (len(listResults) > 1) else "No Results found"))
        embed.add_field(name="test3",value=(listResults[2] if (len(listResults) > 2) else "No Results found"))
        embed.add_field(name="test4",value=(listResults[3] if (len(listResults) > 3) else "No Results found"))
        embed.add_field(name="test5",value=(listResults[4] if (len(listResults) > 4) else "No Results found"))
        return embed

    def getGame(self, game):
        game = game.lower()
        if(game == "csgo"): return 730
        elif(game == "gmod"): return 4000
        elif(game == "l4d"): return 550
        elif(game == "l4d2"): return 500
        elif(game == "tf2"): return 440
        elif(game == "portal2"): return 620
        elif(game == "portal"): return 620
        elif(game == "p2"): return 620
        else: return 730

    def urlBuilder(self, cursor, appId, term):
            myURL = "https://api.steampowered.com/IPublishedFileService/QueryFiles/v1/"
            myURL += "?key=F7DC6D9844D5D731A7DFCA54B6EB8578"
            myURL += "&query_type=10"
            # myURL += "&page=1"
            myURL += f"&cursor={cursor}"
            myURL += "&numberpage=10"
            # myURL += "&creator_appid=730"
            myURL += f"&appid={appId}"
            # myURL += "&requiredtags=map"
            myURL += "&excludedtags=Weapon+Finish"
            myURL += "&match_all_tags=1"
            myURL += "&required_flags=Map"
            myURL += "&omitted_flags=Weapon+Finish"
            myURL += f"&search_text={term}"
            myURL += "&filetype=0"
            # myURL += "child_publishedfileid=0"
            # myURL += "&days=7"
            myURL += "&include_recent_votes_only=0"
            # myURL += "&cache_max_age_seconds=10"
            # myURL += "&language=0"
            # myURL += "&required_kv_tags=test"
            # myURL += "&totalonly=0"
            # myURL += "&ids_only=1"
            # myURL += "&return_vote_data=0"
            myURL += "&return_tags=1"
            # myURL += "&return_kv_tags=0";
            # myURL += "&return_previews=0";
            # myURL += "&return_children=0";
            # myURL += "&return_short_description=0"
            # myURL += "&return_for_sale_data=0"
            # myURL += "&return_metadata=0"
            # myURL += "&return_playtime_stats=0"
            return myURL

