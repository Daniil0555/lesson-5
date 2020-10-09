from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


try:
    host = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(host)

    x_element = browser.find_element_by_css_selector('[id="num1"]').text
    y_element = browser.find_element_by_css_selector('[id="num2"]').text
    sum = str(int(x_element) + int(y_element))
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(sum)  # ищем элемент с текстом "Python"

    # input_value = browser.find_element_by_css_selector('[id="answer1"]')
    # input_value.send_keys(y)
    # check_box = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    # check_box.click()
    # radio_button = browser.find_element_by_css_selector('[id="robotsRule"]')
    # radio_button.click()
    submit_form = browser.find_element_by_css_selector('[type="submit"]')
    submit_form.click()
finally:
    time.sleep(10)
    browser.quit()


