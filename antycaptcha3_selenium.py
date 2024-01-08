import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def find_seed_info(text: list) -> str:
    for line in text:
        if 'Your seed is: ' in line.text:
            found_element = line.text.removesuffix('Your seed is: ').strip()
    return found_element


load_dotenv()
PATH = os.getenv('SELENIUM_CHROMEDRIVER_PATH')
with webdriver.Chrome(service=Service(executable_path=PATH)) as driver:
    # 1. open the link
    CAPTCHA_URL = 'https://antycaptcha.amberteam.pl/exercises/exercise3'
    driver.get(CAPTCHA_URL)

    seed_els = driver.find_elements(By.CLASS_NAME, "row")
    seed = find_seed_info(seed_els)
    print(seed)

    # 2. locate the <code> tag and read text from it
    code_tags = driver.find_elements(By.TAG_NAME, 'code')
    prompt = code_tags[0].text
    print(prompt)

    # 3. locate the expandable lists , click and choose <option> tag with text from 2.
    driver.find_element(By.ID, "s13").click()

    option_in_list = driver.find_elements(By.TAG_NAME, 'option')
    for element in option_in_list:
        if prompt in element.text:
            element.click()

    # 4. locate and click CHECK SOLUTION button
    solution = driver.find_element(By.ID, 'solution')
    solution.click()
