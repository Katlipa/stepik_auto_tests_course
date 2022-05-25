from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Kate")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Katt")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.ry")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'answer.txt')
    add_file = browser.find_element_by_id("file")
    add_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
