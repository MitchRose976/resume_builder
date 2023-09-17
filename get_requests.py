import random
from fastapi import FastAPI

import requests
from bs4 import BeautifulSoup

app = FastAPI()

# list of user_agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
]


@app.get("/{url}")
async def get_data(url: str):
    session = requests.Session()
    session.headers.update({
        'User-Agent': random.choice(user_agents)
    })
    resp = session.get(f"{url}")
    if resp.status_code != 200:
        return {"error": f"bad status code {resp.status_code}"}
    soup = BeautifulSoup(resp.text, "html.parser")
    try:
        data = {
            "url": url,
            "data": soup.find("ul",{"class":"jobsearch-ResultsList css-0"})
        }
        return {"results": data}
    except KeyError:
        return {"error": "Unable to parse page"}
    