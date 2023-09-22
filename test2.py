from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import random

BASE_WEBSITE_URL = 'https://ca.indeed.com/'
ROLE_TO_SEARCH_FOR = ['react', 'developer']
LOCATION_TO_SEARCH_FOR = 'Mississauga'
FORMATTED_URL = f''
WEBSITE_URL = "https://ca.indeed.com/jobs?q=react+developer&l=Mississauga%2C+ON&from=searchOnHP&vjk=a26c35a8ed7ad327"
# PATH_TO_CHROME_DRIVER = '/usr/local/bin/chromedriver/chromedriver-linux64'
PATH_TO_CHROME_DRIVER = "/usr/bin/chromedriver"

IP_ADDRESSES_FILE = 'assets/ip_addresses.txt'

list_of_ips = []

with open(IP_ADDRESSES_FILE, 'r') as file:
    for line in file:
        # Remove leading and trailing whitespace and append to the list
        ip_address = line.strip()
        list_of_ips.append(ip_address)


# Function to get a random IP address from list_of_ips
def get_random_ip():
    return random.choice(list_of_ips)

proxy_ip = get_random_ip()

# Configure Selenium with the proxy IP
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy_ip}')

# Create a webdriver instance with the configured options
driver = webdriver.Chrome(executable_path=PATH_TO_CHROME_DRIVER, options=chrome_options)
driver.get(WEBSITE_URL)

# Grab all job posting cards on page
matches = driver.find_elements_by_tag_name("li")

for match in matches:
    if match.text != "":
        print("mitch match: ", match.text)

# Close the webdriver after each iteration
driver.quit()



