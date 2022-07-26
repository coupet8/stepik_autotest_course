import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_send_and_feedback(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()) - 1.0)
    browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(answer)
    browser.fnd_element(By.CSS_SELECTOR, ".submit-submission").click()
    button = WebDriverWait(browser, 5).until(
        EC.visiblity_of((By.CSS_SELECTOR, "p.smart-hints__hint"))
    )
    message = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert "Correct!" in message.text
