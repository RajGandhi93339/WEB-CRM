import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
# Open a webpagepip install selenium
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

findCheckBoxes = driver.find_elements(By.XPATH,"//div[@id='checkbox-example']//input")
print(findCheckBoxes)
for check_box in findCheckBoxes :
    check_box.click()
    # time.sleep(1)

blinkingText = driver.find_element(By.CLASS_NAME,"blinkingText")
print(blinkingText.get_attribute("href"))
# time.sleep(2)
dynamicDropdown = driver.find_element(By.XPATH,"//input[@type='text']")
dynamicDropdown.send_keys("ind")
# time.sleep(2)

dropDownOptions = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//div")
# print(f"First dropdown attribute value : {dropDownOptions.text}")
for index, option in enumerate(dropDownOptions) :
    # time.sleep(1)
    print(f"First dropdown {index+1} option : {option.text}")
    if "Indonesia" in option.text:
        # time.sleep(1)
        option.click()
        print("Click successfully")
        break
    else:
        print("Not matching option ")
time.sleep(3)
