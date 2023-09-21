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
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def generate_email_login():
  # Generate a random string of lowercase letters
  login = ''.join(random.choices(string.ascii_lowercase, k=8))

  # Generate a random number between 1 and 9999
  number = random.randint(1, 9999)

  # Generate a random domain from a list of common email domains
  domains = [
    '78ndv.online', '78ndv.ru', '78real.online', '78real.ru', '78zhk.online',
    '78zhk.ru', '812.best', '812estate.online', '812estate.ru',
    '812flat.online', '812flat.ru', '812.house', '812zhk.online', '812zhk.ru',
    'esteats.online', 'esteats.ru', 'flatsk.online', 'flatsk.ru',
    'gk.812flat.online', 'guruspb.ru', 'kvartal.rest', 'm2.m2spb.online',
    'm2spb.online', 'm2spb.ru', 'm2.zhkneva.ru', 'm.78ndv.online',
    'm.78ndv.ru', 'm.78real.online', 'm.78real.ru', 'm.78zhk.online',
    'm.78zhk.ru', 'm.812estate.online', 'm.812estate.ru', 'm.812flat.ru',
    'm.812zhk.ru', 'm.esteats.online', 'm.esteats.ru', 'metr.rest',
    'm.flatsk.online', 'm.flatsk.ru', 'm.m2spb.online', 'm.m2spb.ru',
    'm.ndvsp.online', 'm.ndvsp.ru', 'm.nevazhk.online', 'm.nevazhk.ru',
    'm.onzhk.online', 'm.onzhk.ru', 'm.skzhk.online', 'm.skzhk.ru',
    'm.spbzh.online', 'm.tondv.online', 'm.tondv.ru', 'm.tozhk.online',
    'm.tozhk.ru', 'm.zhk-78.online', 'm.zhk78.online', 'm.zhk-78.ru',
    'm.zhk78.ru', 'm.zhk812.online', 'm.zhk812.ru', 'm.zhkneva.online',
    'm.zhkneva.ru', 'm.zhkon.online', 'n812.store', 'ndvsp.online', 'ndvsp.ru',
    'nevazhk.online', 'nevazhk.ru', 'onzhk.online', 'onzhk.ru', 'skzhk.online',
    'skzhk.ru', 'spb.jnv.ru', 'spbzh.online', 'spbzh.ru', 'tondv.online',
    'tondv.ru', 'tozhk.online', 'tozhk.ru', 'zhk-78.online', 'zhk78.online',
    'zhk-78.ru', 'zhk78.ru', 'zhk812.online', 'zhk812.ru', 'zhkneva.online',
    'zhkneva.ru'
  ]
  domain = random.choice(domains)

  # Combine the login, number, and domain to form the email login
  email_login = f"{login}{number}@{domain}"

  return email_login


# Generate and print a random email login
print(generate_email_login())
random_email = generate_email_login()

chrome_options = Options()
#PROXY = "http://b04145127ef1fc36a3c2a6ee941b4b33396ebab9:premium_proxy=true@proxy.zenrows.com:8001"  #  HOST:PORT
#proxy_server_url = 'http://mEmUza:SYEHeb1KujAr@gg.mobileproxy.space:64297'
#chrome_options.add_argument(f'--proxy-server={proxy_server_url}')
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("ignore-certificate-errors")
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Firefox(proxy=proxy)

driver.get("https://my.lptracker.ru/login.php?mode=register")
wait = WebDriverWait(driver, 100)
## Finding Elements

input_box = driver.find_element(By.ID, "input_email")

## Typing and Clicking
wait = WebDriverWait(driver, 55)
input_box.send_keys(f"{random_email}")
wait = WebDriverWait(driver, 55)
#input_box.send_keys(Keys.ENTER)
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
driver.get_cookies()
cookies = driver.get_cookies()

# Convert cookies to a single-line string
cookie_string = '; '.join(
  [f"{cookie['name']}={cookie['value']}" for cookie in cookies])

print(cookie_string)

webhook_url = "https://webhook.site/6327c906-51e2-443b-a43d-2f6d17379dec"
payload = {
  "cookie": cookies,
  "email": random_email,
  "cookiestring": cookie_string
}
response = requests.post(webhook_url, json=payload)
wait = WebDriverWait(driver, 100)
driver.get("https://my.lptracker.ru/login.php?mode=register")
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
driver.get_cookies()
cookies = driver.get_cookies()

# Convert cookies to a single-line string
cookie_string = '; '.join(
  [f"{cookie['name']}={cookie['value']}" for cookie in cookies])

print(cookie_string)

webhook_url = "https://webhook.site/6327c906-51e2-443b-a43d-2f6d17379dec"
payload = {
  "cookie": cookies,
  "email": random_email,
  "cookiestring": cookie_string
}
response = requests.post(webhook_url, json=payload)
print(driver.get_cookies())
wait = WebDriverWait(driver, 55)

# Example usage
driver.get_cookies()
cookies = driver.get_cookies()

# Convert cookies to a single-line string
cookie_string = '; '.join(
  [f"{cookie['name']}={cookie['value']}" for cookie in cookies])

print(cookie_string)

webhook_url = "https://webhook.site/6327c906-51e2-443b-a43d-2f6d17379dec"
payload = {
  "cookie": cookies,
  "email": random_email,
  "cookiestring": cookie_string
}
response = requests.post(webhook_url, json=payload)
wait = WebDriverWait(driver, 55)
driver.quit()
