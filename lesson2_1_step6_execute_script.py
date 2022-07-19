from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)
check = browser.find_element(By.ID, "robotCheckbox")
check.click()
radio = browser.find_element(By.ID, "robotsRule")
radio.click()
button = browser.find_element(By.TAG_NAME, "button")
button.click()