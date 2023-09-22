from selenium import webdriver

BASE_WEBSITE_URL = 'https://ca.indeed.com/'
ROLE_TO_SEARCH_FOR = ['react', 'developer']
LOCATION_TO_SEARCH_FOR = 'Mississauga'
FORMATTED_URL = f''
WEBSITE_URL = "https://ca.indeed.com/jobs?q=react+developer&l=Mississauga%2C+ON&from=searchOnHP&vjk=a26c35a8ed7ad327"
# PATH_TO_CHROME_DRIVER = '/usr/local/bin/chromedriver/chromedriver-linux64'
PATH_TO_CHROME_DRIVER = "/usr/bin/chromedriver"

driver = webdriver.Chrome(executable_path=PATH_TO_CHROME_DRIVER)
driver.get(WEBSITE_URL)

matches = driver.find_elements_by_tag_name("li")

for match in matches:
    if match.text != "":
        print("mitch match: ", match.text)

driver.quit()
