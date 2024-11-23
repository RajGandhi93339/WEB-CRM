import time
from selenium import webdriver
from selenium.webdriver.common.by   import By

driver = webdriver.Chrome()
driver.maximize_window()
# Open a webpagepip install selenium
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#example 1 tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
time.sleep(2)

#example 2 [attribute=value]
driver.find_element(By.CSS_SELECTOR,"[value='radio2']").click()
time.sleep(3)

#example 3 [input#id]
driver.find_element(By.CSS_SELECTOR,"input#displayed-text").send_keys("DEMO TEXT")
time.sleep(3)

#example 4 [input.classvalue]
clickbutton = driver.find_element(By.CSS_SELECTOR,"input#alertbtn")
clickbutton.click()
time.sleep(3)

