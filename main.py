from selenium import webdriver
from time import sleep

chrome_browser = webdriver.Chrome(
    executable_path='C:\\Users\\aryan\\Downloads\\chromedriver.exe')
chrome_browser.get('https://mail.google.com')

email = chrome_browser.find_element_by_xpath('//input[@type="email"]')
email.send_keys('chatbot.email.2008@gmail.com')

email_next_button = chrome_browser.find_element_by_xpath('//button[@jsname="LgbsSe"]')
email_next_button.click()

password = chrome_browser.find_element_by_xpath('//input[@class="whsOnd zHQkBf"]')
password.send_keys('avayax12')

password_next_button = chrome_browser.find_element_by_xpath('//button[@jsname="LgbsSe"]')

# chrome_browser.get('https://web.whatsapp.com/')
# 
# sleep(5)
# 
# user_name = 'Private'

