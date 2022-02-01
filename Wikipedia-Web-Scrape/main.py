from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "Insert File Path for Chrome Driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

SEARCH_TERM = "Python"

search = driver.find_element(By.NAME, "search")
search.send_keys(SEARCH_TERM)
search.send_keys(Keys.ENTER)

# driver.quit()
