import requests
from shared.constants import VALID_IP_ADDRESSES_FILE


# validates all filtered ip_addresses with a simple scrape to confirm they work and returns list of valid ones
def validate_proxies():
    with open(VALID_IP_ADDRESSES_FILE, "r") as f:
        proxies = f.read().split("\n")

    sites_to_check = [
        "http://books.toscrape.com/",
        "http://books.toscrape.com/catalogue/books/fantasy_19/index.html",
        "http://books.toscrape.com/catalogue/books/history_32/index.html",
    ]

    validated_proxies = []

    counter = 0
    for site in sites_to_check:
        try:
            print(f"using the proxy: {proxies[counter]}")
            res = requests.get(
                site, proxies={"http": proxies[counter], "https": proxies[counter]}
            )
            print(res.status_code)
            if res.status_code == 200:
                validate_proxies.append(proxies[counter])
        except:
            print("failed")
        finally:
            counter += 1
            counter % len(proxies)
        print('mitch validated_proxies: ', validated_proxies)

validate_proxies()