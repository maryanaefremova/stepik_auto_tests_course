from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)
    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    
    for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
        browser.find_element(By.CSS_SELECTOR, selector).click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()