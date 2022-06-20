from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
