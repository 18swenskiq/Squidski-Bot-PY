using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Web;

namespace VDCSearch
{
    class Program
    {
        static void Main(params string[] searchTerm)
        {
            // Imagine copying the code you wrote for BotHATTwaffle into your own bot
            string onlyInput = "";
            try
            {
                onlyInput = searchTerm[0];
            }
            catch
            {
                Console.WriteLine("NRF");
                return;
            }
            onlyInput = HttpUtility.UrlEncode(onlyInput);
            string myString = VdcAsync(onlyInput).Result;
            Console.WriteLine(myString);
        }

        public static async Task<string> VdcAsync(string term)
        {
            string siteData = "";

            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("https://developer.valvesoftware.com/w/");
                HttpResponseMessage response = client.GetAsync($"api.php?action=opensearch&search={term}&limit=5&format=json").Result;
                response.EnsureSuccessStatusCode();
                siteData = response.Content.ReadAsStringAsync().Result;
            }

            term = HttpUtility.UrlDecode(term);
            List<string> dataArray = new List<string>();
            MatchCollection matches;

            if (siteData != $"[\"{term}\",[],[],[]]")
            {
                // Pull just the URLs that it gives from the GET request
                matches = Regex.Matches(siteData, @"\b((https?|ftp|file)://|(www|ftp)\.)[-A-Z0-9+()&@#/%?=~_|$!:,.;]*[A-Z0-9+()&@#/%=~_|$]", RegexOptions.IgnoreCase);
                foreach (Match match in matches)
                {
                    dataArray.Add(match.Value.ToString());
                }
            }

            if (siteData == $"[\"{term}\",[],[],[]]") return "NRF";
            else return string.Join(", ", dataArray.ToArray());

        }
    }
}
