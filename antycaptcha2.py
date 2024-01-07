from time import sleep

from bot_useful_functions import *
from bs4 import BeautifulSoup
import httpx
from pynput import mouse


class CaptchaBot:

    def __init__(self, web_link):
        self.web_link = web_link
        self.mouse_controller = mouse.Controller()
        self.text_field = 'typing_field.png'
        self.solution = 'solution.png'
        self.good_answer = 'good_answer.png'
        self.button1 = 'b1_button.png'
        self.button2 = 'b2_button.png'

    def items(self) -> list:
        return [
            self.text_field,
            self.solution,
            self.good_answer,
            self.button1,
            self.button2
        ]

    def get_code_tags(self) -> tuple:
        """ Given response from site parses to find <code> tag.
        Within the tags are prompts that are extracted into tuple of 4 elements."""
        resp = httpx.get(self.web_link, verify=False)
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        code_tags = soup.find_all('code')
        sentence, field_to_fill_with_sentence, button_to_press, expected_output = (tag.text for tag in code_tags)

        return sentence, field_to_fill_with_sentence, button_to_press, expected_output

    def click_on_item(self, item_path: str):
        """ Clicks on location of given item """
        try:
            x, y, *_ = locate_item(item_path)
            self.mouse_controller.position = x, y
            sleep(.2)
            click_on_position(self.mouse_controller, x, y)
        except pyautogui.ImageNotFoundException:
            print('see nothing')

    def final_step(self):
        """ Checks if solution is correct"""
        x, y, *_ = locate_item(self.solution)
        click_on_position(self.mouse_controller, x, y)

        if locate_item(self.good_answer) is not None:
            keyboard.press('q')
            keyboard.release('q')
            print('End of program. Good answer met.')


if __name__ == '__main__':
    seed = 'c265819e-6ed3-4ea6-9753-5a554d5a6481'
    bot = CaptchaBot(f'https://antycaptcha.amberteam.pl/exercises/exercise2?seed={seed}')

    prompt, field, button, output = bot.get_code_tags()
    if button.lower().strip() == 'b1':
        button = bot.button1
    elif button.lower().strip() == 'b2':
        button = bot.button2

    sleep(2)
    # locate_item(bot.text_field)
    bot.click_on_item(bot.text_field)
    press_keyboard_sequence('ctrl', 'a')
    pyautogui.press('del')
    type_sentence(prompt)
    bot.click_on_item(button)
    bot.final_step()
