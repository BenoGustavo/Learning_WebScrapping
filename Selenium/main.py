from makeChromeInstance import makeBrowser

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils import WAITING_TIME

chromeBrowser = makeBrowser()
chromeBrowser.get("https://www.google.com.br")

# Wait to find input on screen
searchInput = WebDriverWait(chromeBrowser, WAITING_TIME).until(
    # Finding an element on the screen
    expected_conditions.presence_of_element_located((By.ID, "APjFqb"))
)

# Write an text on the search bar
searchInput.send_keys("Faculdade Cesusc")
searchInput.send_keys(Keys.ENTER)

searchResults = chromeBrowser.find_element(By.ID, "search")
websiteLink = searchResults.find_elements(By.TAG_NAME, "a")
cesuscLink = websiteLink[0]
cesuscLink.click()

sleep(WAITING_TIME)
