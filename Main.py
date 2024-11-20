import time
from selenium import webdriver 

from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.maximize_window()
# Open a webpagepip install selenium
driver.get("https://crm.testsjit.in/#/login")
# driver.find_element(By.CSS_SELECTOR,"#logemail").click()
driver.find_element(By.XPATH,"//input[@id='logemail']").send_keys("4")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("000")
driver.find_element(By.XPATH,"//input[@id='rememberMe']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success w-100']").click()
time.sleep(3)

