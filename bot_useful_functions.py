import time
import pyautogui
import keyboard
from pynput import mouse


### mouse ###
def display_position():
    while keyboard.is_pressed('q') is False:
        mouse_controll = mouse.Controller()
        x, y = mouse_controll.position
        print(f'{x} , {y}')


def locate_item(item_path: str):
    """ Locate on open website window an item.
        Item ( a button or text field ) needs to be a path to image file,
        in order to be located on the screen """
    try:
        return pyautogui.locateOnScreen(item_path, confidence=0.8)
    except pyautogui.ImageNotFoundException as error:
        return error


def click_on_position(controller: mouse.Controller, x: int, y: int, count: int = 1):
    controller.position = (x+8, y+8)
    for num in range(count):
        controller.press(mouse.Button.left)
        time.sleep(0.01)
        controller.release(mouse.Button.left)

### keyboard ###
def press_keyboard_sequence(*keys):

    pyautogui.hotkey(*keys)
    pyautogui.press('enter')


def type_sentence(sentence: str):
    keyboard.write(sentence)
