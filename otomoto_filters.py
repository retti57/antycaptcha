import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def load_path():
    load_dotenv()
    return os.getenv('SELENIUM_CHROMEDRIVER_PATH')


class Search:
    def __init__(self, url, driver):
        self.url = url
        self.webdriver = driver

    def open_url_and_maximize_window(self):
        self.webdriver.get(self.url)
        self.webdriver.maximize_window()

    def click_advanced_search(self) -> bool:
        advanced_search = self.webdriver.find_element(By.XPATH, "//span[contains(text(), 'Wyszukiwanie zaawansowane')]")
        advanced_search.click()
        return advanced_search.text

    def _find_filter_sections(self):
        """Finds <div> tag containing filters"""
        xpath_query = "//form[@role='search']"

        filters = self.webdriver.find_element(By.XPATH, xpath_query)
        """ DZIAŁA """
        return filters

    def car_make(self, make_of_car):
        """ Selects given make of car """
        make = self.webdriver.find_element(By.XPATH, "//div[@data-testid='filter_enum_make']")
        make.click()

        input_tag = make.find_element(By.XPATH, "//input[@type='text'][@aria-label='Marka pojazdu']")
        input_tag.click()

        input_tag.send_keys(make_of_car.title())

        # find and click checkbox
        car = make.find_element(By.XPATH, f'//li//p[contains(text(),{make_of_car.title()})]')
        car_checkbox = car.find_element(By.XPATH, '//li//input[@type="checkbox"]')

        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//form[@role='search']//label[@data-testid='label']")
            )
        )
        car_checkbox.click()

        # find and click arrow Up
        if car_checkbox.is_selected():
            print('checkbox make selected')
            WebDriverWait(chrome_driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//form[@role='search']//div[@data-testid='filter_enum_make']//span")
                )
            )

            arrow_button = self.webdriver.find_element(
                By.XPATH,
                "//form//div[@data-testid='filter_enum_make']//span//button[@data-testid='arrow']"
            )

            if arrow_button.is_displayed():
                print("see arrow up make")
                arrow_button.click()
                # sleep(1)
    """ działa """

    def car_model(self, model_of_car):
        """ Selects given model of car """
        model = self.webdriver.find_element(By.XPATH, "//div[@data-testid='filter_enum_model']")
        model.click()

        input_tag_model = model.find_element(By.XPATH, "//input[@type='text'][@aria-label='Model pojazdu']")
        input_tag_model.click()

        input_tag_model.send_keys(model_of_car.title())
        # find and click checkbox
        car = model.find_element(By.XPATH, f'//li//p[contains(text(),{model_of_car.title()})]')
        car_checkbox = car.find_element(By.XPATH, '//li//input[@type="checkbox"]')

        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//form[@role='search']//label[@data-testid='label']")
            )
        )
        car_checkbox.click()



        # find and click arrow Up
        if car.is_selected():
            print('checkbox model selected')
            WebDriverWait(chrome_driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//form[@role='search']//div[@data-testid='filter_enum_model']//span")
                )
            )

            arrow_button = self.webdriver.find_element(
                By.XPATH,
                "//form//div[@data-testid='filter_enum_model']//span//button[@data-testid='arrow']"
            )

            if arrow_button.is_displayed():
                print("see arrow up model")
                arrow_button.click()
                # sleep(1)
    """ działa """

    def car_body_type(self, body_type):

        div_body_type = self.webdriver.find_element(By.XPATH, "//div[@data-testid='filter_enum_body_type']")
        div_body_type.click()

        fieldset_tag = div_body_type.find_element(By.XPATH, "//fieldset[@aria-label='Typ nadwozia']")
        fieldset_tag.click()

        ul_tag = WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//form[@role=\'search\']//div[@data-testid=\'filter_enum_body_type\']")
            )
        )
        ul_tag.click()
        # ul_tag = div_body_type.find_element(By.XPATH, '//ul[@class="ooa-dljx5f"]')

        for element in ul_tag:
            label = element.find_element(By.TAG_NAME, 'label')
            print(label)
            p_in_label = label.find_element(By.TAG_NAME, "p")
            print(p_in_label)
            if p_in_label.text in body_type:
                label_type_checkbox = label.find_element(By.XPATH, '//input[@type="checkbox"]')
                label_type_checkbox.click()
        # find and click checkbox
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                (By.XPATH,
                 "//form[@role='search']//div[@data-testid='filter_enum_body_type']//fieldset/input[@value]",
                 p_in_label.text)
            )
        )

        # find and click arrow Up
        if label_type_checkbox.is_selected():
            print('checkbox selected type')
            WebDriverWait(chrome_driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//form[@role='search']//div[@data-testid='filter_enum_body_type']//span")
                )
            )

            arrow_button = self.webdriver.find_element(
                By.XPATH,
                "//form//div[@data-testid='filter_enum_body_type']//span//button[@data-testid='arrow']"
            )

            if arrow_button.is_displayed():
                print("see arrow up type")
                arrow_button.click()
                sleep(1)



    def car_price(self, price_lowest=0.0, price_highest=200000.0):

        filters = self._find_filter_sections()
        price = filters.find_element(By.XPATH, "//div[@data-testid='filter_float_price']")
        price.click()
        price_low = filters.find_element(By.XPATH, "//div[@data-testid='range-from']").find_element(By.TAG_NAME,
                                                                                                    'input')
        price_low.send_keys(price_lowest)

        price_high = filters.find_element(By.XPATH, "//div[@data-testid='range-to']").find_element(By.TAG_NAME,
                                                                                                   'input')
        price_high.send_keys(price_highest)

    def car_year(self, lowest=1980, highest=2024):

        filters = self._find_filter_sections()
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
    search.open_url_and_maximize_window()

    WebDriverWait(chrome_driver, 15).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "span"))
    )
    search.click_advanced_search()

    WebDriverWait(chrome_driver, 15).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//form[@role='search']")
        )
    )


    search.car_make('Ford')

    # WebDriverWait(chrome_driver, 15).until(
    #     expected_conditions.presence_of_element_located(
    #         (By.XPATH, "//div[@data-testid='filter_enum_model']"))
    # )
    sleep(1)
    search.car_model('Mondeo')
    print('delay 2 for terminating')
    sleep(2)
    search.car_body_type('sedan')
#     search.car_price(20000,25000)
#     sleep(3)
#     search.car_year(2015, 2016)
#     sleep(3)
#
#     chrome_driver.send_key('ENTER')
#     sleep(5)
