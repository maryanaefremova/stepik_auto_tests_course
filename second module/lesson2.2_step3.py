from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    x2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    y = int(x1) + int(x2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()