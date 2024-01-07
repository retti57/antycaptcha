import time
import pyautogui
import keyboard
from pynput import mouse


def click_on_position(controller: mouse.Controller, x: int, y: int, count: int = 1):
    controller.position = (x, y)
    for num in range(count):
        controller.press(mouse.Button.left)
        time.sleep(0.01)
        controller.release(mouse.Button.left)


def copy_link():
    mouse_controller = mouse.Controller()
    click_on_position(mouse_controller, 200, 60, count=1)
    pyautogui.hotkey('ctrl', 'c')


def display_position():
    while keyboard.is_pressed('q') is False:
        mouse_controll = mouse.Controller()
        x, y = mouse_controll.position
        print(f'{x} , {y}')
