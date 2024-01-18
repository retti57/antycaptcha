"""Script to play with piano tails online game"""

import time
import pyautogui
import keyboard
from pynput import mouse
from bot_useful_functions import click_on_position


if __name__ == '__main__':
    R, G, B = 0, 0, 0
    x1, y1 = 820, 400
    x2, y2 = 920, 400
    x3, y3 = 1020, 400
    x4, y4 = 1120, 400
    mouse_controller = mouse.Controller()
    time.sleep(2)

    while keyboard.is_pressed('q') is False:
        if pyautogui.pixel(x1, y1)[0] == 0:
            click_on_position(mouse_controller, x1, y1)

        if pyautogui.pixel(x2, y2)[0] == 0:
            click_on_position(mouse_controller, x2, y2)

        if pyautogui.pixel(x3, y3)[0] == 0:
            click_on_position(mouse_controller, x3, y3)

        if pyautogui.pixel(x4, y4)[0] == 0:
            click_on_position(mouse_controller, x4, y4)
