import time 
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
email = "#email/username/phonenumber"
password = "#password"
driver.get("https://www.instagram.com/")

folder = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
folder.click()
folder = driver.find_element_by_xpath("//input[@name='username']")
folder.send_keys(email)
folder = driver.find_element_by_xpath("//input[@name='password']")
folder.send_keys(password)
folder = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
folder.click()

try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, "10s").until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load"
    )

folder = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[1]")
folder.click()
folder = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg")
folder.click()     
