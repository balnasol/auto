from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link='https://suninjuly.github.io/alert_accept.html'
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser=webdriver.Chrome()
    browser.get(link)
    clik=browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    clik.click()
    allert=browser.switch_to.alert
    allert.accept()
    X=browser.find_element(By.ID,'input_value')
    x=X.text
    y=calc(x)
    sen=browser.find_element(By.ID,'answer')
    sen.send_keys(y)
    submit=browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
    submit.click()
    new_alert=browser.switch_to.alert.text
    print(new_alert)
    
    
    
finally:
    time.sleep(4)
    browser.quit()