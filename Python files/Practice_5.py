import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.oneplus.in/")
element = driver.find_element("xpath","//a[text()='Store']")
actions = ActionChains(driver,250)
actions.move_to_element(element).perform()
time.sleep(10)
print("CLOSE SUCCESSFULLY............")
driver.quit()

