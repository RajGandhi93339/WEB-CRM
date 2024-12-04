import time
from selenium import webdriver
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
# Open a webpagepip install selenium
driver.get("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")
driver.implicitly_wait(5)
clickSearchtopboxButton = driver.find_element(By.ID,"globalnav-menubutton-link-search")
clickSearchtopboxButton.click()
# typingSelectDropdownValue.send_keys("Iphone 15")
time.sleep(3)
Search_box = driver.find_elements("xpath","//div//form[@class='globalnav-searchfield']")
print(type(Search_box))
print(Search_box)

Search_box.send('Iphone 15')
dropdown_options = driver.find_elements("xpath","//a[@class='globalnav-searchresults-list-link']//span[@class='globalnav-searchresults-list-text']")
print(type(dropdown_options))
time.sleep(3)
for index, option in enumerate(dropdown_options) :
    print(f"link present in {index+1} option : {option.get_attribute("href")}")
    print(f"link present in {index+1} option : {option.text}")

    if "India" in option.text:
        option.click()
        break
    else:
        print("India option is not fount....")

time.sleep(3)