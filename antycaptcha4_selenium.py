import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def get_trail_set(chrome_driver) -> list:
    tags = []
    td_tags = chrome_driver.find_elements(By.TAG_NAME, "td")
    for tag in td_tags:
        if 'Trail' in tag.text:
            trail = tag.find_element(By.TAG_NAME, 'code').text
            for char in trail:
                if char.isdigit():
                    tags.append(char)

    return tags


def extract_answer_from_table(chrome_driver) -> list:
    tags = []
    td_tags = chrome_driver.find_elements(By.TAG_NAME, "td")
    for tag in td_tags:
        if 'group' in tag.text:
            tags.append(tag.find_element(By.TAG_NAME, 'code').text)
    return tags


def get_seed(chrome_driver):
    seed_el = chrome_driver.find_element(By.XPATH, "//div[contains(text(), 'seed')]")
    return seed_el.text


def extract_input_tag_text(chrome_driver) -> list:
    for tag in chrome_driver.find_elements(By.XPATH, '//*[@id="exercise4"]/div/div/div[1]/div'):
        lines = tag.text.split('\n')
        for line in lines:
            if 'Group' in line:
                lines.remove(line)

    return lines


def load_path():
    load_dotenv()
    return os.getenv('SELENIUM_CHROMEDRIVER_PATH')


with webdriver.Chrome(service=Service(executable_path=load_path())) as driver:
    CAPTCHA_URL = 'https://antycaptcha.amberteam.pl/exercises/exercise4'
    driver.get(CAPTCHA_URL)

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(), 'seed')]"))
    )
    print(get_seed(driver))

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='exercise4']/div/div/table/tbody"))
    )
    group_answer = extract_answer_from_table(driver)
    print(group_answer)
    trail_set = get_trail_set(driver)
    print(trail_set)

    for i in range(0, 4):
        elems = driver.find_element(By.CSS_SELECTOR, f'[value="v{trail_set[i] + str(i)}"]')
        elems.click()
        time.sleep(1)

    solution = driver.find_element(By.ID, 'solution')
    solution.click()
    time.sleep(1)
    if driver.find_element(By.ID, 'trail').find_element(By.TAG_NAME, 'code').text == 'OK. Good answer':
        print('OK. Good answer')

    else:
        print('exit with troubles')
