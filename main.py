from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from keepAlive import keep_alive
import os
import string
import random
import requests
import json
from selenium.webdriver.support.ui import WebDriverWait

def generate_email_login():
    # Generate a random string of lowercase letters
    login = ''.join(random.choices(string.ascii_lowercase, k=8))

    # Generate a random number between 1 and 9999
    number = random.randint(1, 9999)

    # Generate a random domain from a list of common email domains
    domains = ['brokerleads.ru', 'brokerleads.ru']
    domain = random.choice(domains)

    # Combine the login, number, and domain to form the email login
    email_login = f"{login}{number}@{domain}"

    return email_login

# Generate and print a random email login
print(generate_email_login())
random_email = generate_email_login()

chrome_options = Options()
#proxy_server_url = 'https://scraperapi.premium%3Dtrue:7a3eaf959519f885bb43b8e0842ac7df@proxy-server.scraperapi.com:8001'
#chrome_options.add_argument(f'--proxy-server={proxy_server_url}')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--incognito")
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
					 
					 
#driver = webdriver.Remote(
 #  command_executor="https://selenium-hub-production.up.railway.app/wd/hub", options=chrome_options);
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://my.lptracker.ru/#logout");
wait = WebDriverWait(driver, 55)
driver.get("https://my.lptracker.ru/login.php?mode=register");
wait = WebDriverWait(driver, 100)
## Finding Elements

input_box = driver.find_element(By.ID, "input_email")

## Typing and Clicking
wait = WebDriverWait(driver, 55)
input_box.send_keys(f"{random_email}")
wait = WebDriverWait(driver, 55)
input_box.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 55)
input_box2 = driver.find_element(By.ID, "input_password")

## Typing and Clicking
wait = WebDriverWait(driver, 55)
input_box2.send_keys("sergyn")
wait = WebDriverWait(driver, 55)
input_box2.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 55)
home_link = driver.find_element(By.ID, "js-register-button")
wait = WebDriverWait(driver, 55)
home_link.click()
home_link.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 100)
cookie = driver.get_cookies()
webhook_url = "https://webhook.site/6327c906-51e2-443b-a43d-2f6d17379dec"
payload = {"cookie": cookie}
response = requests.post(webhook_url, json=payload)
driver.get("https://my.lptracker.ru/login.php?mode=register");
wait = WebDriverWait(driver, 100)
## Finding Elements

input_box = driver.find_element(By.ID, "input_email")

## Typing and Clicking
wait = WebDriverWait(driver, 55)
input_box.send_keys(f"{random_email}")
wait = WebDriverWait(driver, 55)
input_box.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 55)
input_box2 = driver.find_element(By.ID, "input_password")

## Typing and Clicking
wait = WebDriverWait(driver, 55)
input_box2.send_keys("sergyn")
wait = WebDriverWait(driver, 55)
input_box2.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 55)
home_link = driver.find_element(By.ID, "js-register-button")
wait = WebDriverWait(driver, 55)
home_link.click()
home_link.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 100)
webhook_url = "https://webhook.site/6327c906-51e2-443b-a43d-2f6d17379dec"
payload = {"cookie": cookie}
response = requests.post(webhook_url, json=payload)
print(driver.get_cookies())
wait = WebDriverWait(driver, 55)
driver.get("https://my.lptracker.ru/#logout");
wait = WebDriverWait(driver, 55)
driver.quit()
