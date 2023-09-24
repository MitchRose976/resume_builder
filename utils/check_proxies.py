import threading
import queue
import requests
from shared.constants import IP_ADDRESSES_FILE

q = queue.Queue()
valid_proxies = []

with open(IP_ADDRESSES_FILE, "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def get_valid_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            # checks if ip is valid
            res = requests.get(
                "http://ipinfo.io/json", proxies={"http": proxy, "https:": proxy}
            )
        except:
            continue
        if res.status_code == 200:
            print(proxy)


for _ in range(700):
    threading.Thread(target=get_valid_proxies).start()
