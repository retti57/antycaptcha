""" You need to copy whole url link to current exercise , with your seed number
in order to maintain proper functionality.
This is ment to be working on visible browser window """

from more_itertools import batched
from time import sleep
import pyautogui
import pynput.mouse as mouse
import keyboard
from bot_useful_functions import click_on_position
import httpx
import re


solution = 'solution.png'
good_answer = 'good_answer.png'
button1 = 'b1_button.png'
button2 = 'b2_button.png'


def find_trail_set(html: str):
    trail_set = "Trail set to: <code>[A-Za-z0-9]+</code>"
    trail_set: str = re.findall(trail_set, html)[0].split()[-1]

    return trail_set.removeprefix('<code>').removesuffix('</code>')


def seq_to_buttons(seq) -> list:
    button_to_b = {'b1': button1, 'b2': button2}

    temp_list = []
    for tup in list(batched(seq, 2)):
        new_seq = f'{tup[0]}{tup[1]}'
        temp_list.append(button_to_b[new_seq])

    return temp_list


def find_button(button: str):
    try:
        return pyautogui.locateOnScreen(button, confidence=0.8)
    except pyautogui.ImageNotFoundException as error:
        return error


def click_mouse_with_sequence(seq: list|tuple):
    mouse_controller = mouse.Controller()

    sleep(.2)
    for button in seq:
        # if given image not found on screen the output is None
        try:
            x, y, *_ = find_button(button)
            print(f'x:{x} , y:{y}')
            mouse_controller.position = (x, y)
            sleep(0.5)
            click_on_position(mouse_controller, x, y)

        except pyautogui.ImageNotFoundException:
            print('see nothing')
    else:
        x, y, *_ = find_button(solution)
        click_on_position(mouse_controller, x, y)

        if find_button(good_answer) is not None:
            keyboard.press('q')
            keyboard.release('q')
            print('End of program. Good answer met.')


if __name__ == '__main__':
    """ paste your link below"""
    link = r'https://antycaptcha.amberteam.pl/exercises/exercise1?seed=5a322af9-044a-450a-96c9-c9076eaa10fe'
    resp = httpx.get(link, verify=False)
    html = resp.text
    set_to_sequence = find_trail_set(html)
    seq = seq_to_buttons(set_to_sequence)
    click_mouse_with_sequence(seq)
