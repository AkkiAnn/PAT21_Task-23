from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Set path to ChromeDriver executable
serv_obj=Service(r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# New instance of Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize browser window
driver.maximize_window()

# URL
driver.get("https://jqueryui.com/droppable/")

# Move to frame of draggable element
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))

# Drag Rectangular Box(White)
drag_1ne = driver.find_element(By.ID,"draggable")

# Drop Rectangular Box(Yellow)
drop_1ne = driver.find_element(By.ID,"droppable")

# Drag and Drop operation using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(drag_1ne,drop_1ne).perform()
time.sleep(4)

# Close the browser
driver.quit()