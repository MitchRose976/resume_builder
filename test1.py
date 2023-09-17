import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

from get_requests import get_data

l = []
o = {}

# indeed url
target_url = "https://ca.indeed.com/jobs?q=react+developer&l=Mississauga%2C+ON&from=searchOnHP&vjk=a26c35a8ed7ad327&advn=5830728964398605"


# content = pd.read_html(target_url)
# print("mitch content: ", content)

# response
async def main():
    resp = await get_data(target_url)
    print("mitch resp: ", resp)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
# resp = requests.get(
#     target_url,
#     headers={
#         "User-Agent": random.choice(user_agents),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
#         "Cache-Control": "no-cache",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#     },
# )


# soup = BeautifulSoup(resp.text, "html.parser")
# allData = soup.find("ul", {"class": "jobsearch-ResultsList css-0"})
# print("mitch allData: ", allData)
# allLiTags = allData.find_all("div", {"class": "cardOutline"})
# print("mitch allLiTags: ", allLiTags)
