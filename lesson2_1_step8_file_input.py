from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Tony")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Montana")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("tonym88@gmail.com")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "text.txt")
file = browser.find_element(By.NAME, "file")
file.send_keys(file_path)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
