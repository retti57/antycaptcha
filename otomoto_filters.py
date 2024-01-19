import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait



def load_path():
    load_dotenv()
    return os.getenv('SELENIUM_CHROMEDRIVER_PATH')


class Search:
    def __init__(self, url, driver):
        self.url = url
        self.webdriver = driver

    def open_url(self):
        self.webdriver.get(self.url)

    def click_advanced_search(self) -> bool:
        advanced_search = self.webdriver.find_element(By.XPATH, "//span[contains(text(), 'Wyszukiwanie zaawansowane')]")
        advanced_search.click()
        return advanced_search.text

    def _find_filters_section(self):
        filters = self.webdriver.find_element(By.TAG_NAME, "section")

        return filters

    def car_make(self, make_of_car):

        filters = self._find_filters_section()
        first_filter_div = filters.find_element(By.XPATH, "//div[@data-testid='filter_enum_make']")
        first_filter_div.click()
        checkbox_wrappers = filters.find_elements(By.XPATH, "//div[@data-testid='checkbox-wrapper']")

        for element in checkbox_wrappers:
            if make_of_car in element.text:
                element.click()
                """ Klika już dobrze """
                sleep(2)
            # label_make = label.find_element(By.XPATH, f'//p[contains(text(),{make_of_car}')
        #     print(label_make)
        #     input_box = label.find_element(By.TAG_NAME, 'input')
        #     input_box.click()
        #     # self.webdriver.send_key('ENTER')
        # return make_of_car

    def car_model(self, model_of_car):

        filters = self._find_filters_section()
        models = filters.find_element(By.XPATH, "//div[@data-testid='filter_enum_model']")
        models.click()

        for element in models.find_elements(By.TAG_NAME, 'li'):
            label = element.find_element(By.TAG_NAME, 'label')
            if label.find_element(By.TAG_NAME, 'p').text == model_of_car:
                label.click()
                return model_of_car

    def car_body_type(self, body_type):

        filters = self._find_filters_section()
        body_type = filters.find_element(By.XPATH, "//div[@data-testid='filter_body_type']")
        body_type.click()

        for element in body_type.find_elements(By.TAG_NAME, 'li'):
            label = element.find_element(By.TAG_NAME, 'label')
            if label.find_element(By.TAG_NAME, 'p').text == body_type:
                label.click()
                return body_type

    def car_price(self, price_lowest=0.0, price_highest=200000.0):

        filters = self._find_filters_section()
        price = filters.find_element(By.XPATH, "//div[@data-testid='filter_float_price']")
        price.click()
        price_low = filters.find_element(By.XPATH, "//div[@data-testid='range-from']").find_element(By.TAG_NAME,
                                                                                                    'input')
        price_low.send_keys(price_lowest)

        price_high = filters.find_element(By.XPATH, "//div[@data-testid='range-to']").find_element(By.TAG_NAME,
                                                                                                   'input')
        price_high.send_keys(price_highest)

    def car_year(self, lowest=1980, highest=2024):

        filters = self._find_filters_section()
        year = filters.find_element(By.XPATH, "//div[@data-testid='filter_float_year']")
        year.click()
        year_low = filters.find_element(By.XPATH, "//div[@data-testid='range-from']").find_element(By.TAG_NAME, 'input')
        year_low.send_keys(lowest)

        year_high = filters.find_element(By.XPATH, "//div[@data-testid='range-to']").find_element(By.TAG_NAME,
                                                                                                  'input')
        year_high.send_keys(highest)


load_path()
# example_url = "https://www.otomoto.pl/osobowe/toyota/avensis/seg-sedan/od-2010?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_fuel_type%5D%5B0%5D=petrol&search%5Bfilter_enum_fuel_type%5D%5B1%5D=petrol-lpg&search%5Bfilter_enum_generation%5D=gen-iii-2009&search%5Bfilter_float_price%3Afrom%5D=10000&search%5Bfilter_float_price%3Ato%5D=40000&search%5Bfilter_float_year%3Ato%5D=2015&search%5Border%5D=filter_float_price%3Aasc&search%5Badvanced_search_expanded%5D=true"

with webdriver.Chrome(service=Service(executable_path=load_path())) as chrome_driver:
    URL = 'https://www.otomoto.pl/'
    search = Search(url=URL, driver=chrome_driver)
    search.open_url()

    # /html/body/div[6]/form/div/div/div[2]/div/div/ul/li[118]/  div/label/p

    # div/label/p == marka auta

    # //*[@id="__next"]/div/div/div/main/div[2]/article/article/fieldset/form/section[2]/button[2]
    WebDriverWait(chrome_driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "span"))
    )
    search.click_advanced_search()
    # print(search.click_advanced_search())
    sleep(3)

    search.car_make('Audi')
    sleep(3)
    # search.car_model('A6')
    # sleep(3)
#     search.car_price(20000,25000)
#     sleep(3)
#     search.car_year(2015, 2016)
#     sleep(3)
#
#     chrome_driver.send_key('ENTER')
#     sleep(5)