from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1_element = browser.find_element(By.ID, "num1")
    num1 = number1_element.text
    num1 = int(num1)
    number2_element = browser.find_element(By.ID, "num2")
    num2 = number2_element.text
    num2 = int(num2)
    answer = str(num1 + num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
