import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
# Open a webpagepip install selenium
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# click elements
driver.find_element(By.XPATH,"//input[@value='radio2']").click()

# Clear elements and send key function of elements
driver.find_element(By.XPATH,"//input[@id='name']").send_keys('KAMLESH')
driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys('SURESH')

# Element text copy
alert_example = driver.find_element(By.XPATH,"//legend[text()='Suggession Class Example']")
alert_example_text = alert_example.text
print(alert_example_text)

# select multiple checkbox
# FIND ELEMENTS FUNCTION USE
# XPATH CREATE (Input[Starts-with(@attribute,'commonValue')]
check_boxes = driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")

#ELements check box value print
# print(check_boxes)
# length check of check boxes
# print(len(check_boxes))

#for loop using
for check_box in check_boxes :
    if  check_boxes.index(check_box)+1 > 3:
        check_box.click()

# XPATH CREATE (Input[Starts-with(@attribute,'commonValue')]
deselect_check_boxes = driver.find_elements(By.XPATH,"(//input[starts-with(@name,'checkBoxOption')])[position()<3]")

for check_box in deselect_check_boxes :
    check_box.click()

# select dropdown 
static_dropdown = driver.find_element(By.ID,"dropdown-class-example")
select = Select(static_dropdown)
# time.sleep(3)
select.select_by_index(2)
# time.sleep(3)
select.select_by_visible_text("Option1")

# NotImplementedError
# time.sleep(3)
# select.select_by_value("Option3")

# find get attribute values
blinking_link = driver.find_element(By.CLASS_NAME,"blinkingText")

print(blinking_link.get_attribute("href"))

typingSelectDropdownValue = driver.find_element("xpath","//input[@placeholder='Type to Select Countries']")
typingSelectDropdownValue.click()
typingSelectDropdownValue.send_keys("India")
time.sleep(2)
clickValue = driver.find_element("xpath","(//li[@class='ui-menu-item']//div[text()='India'])")
clickValue.click()
time.sleep(10)