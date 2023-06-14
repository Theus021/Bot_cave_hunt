import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard

PLAYER_POSITION = (686, 369)
BP_LOOT_POSITION1 = (1192, 663)


def move_and_click(position, side_button, click= 1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks= click )

def get_loot():
    move_and_click(PLAYER_POSITION, 'right')
    move_and_click(BP_LOOT_POSITION1, 'left', 2)
    

def key_code(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        get_loot()

    print(key)
    
    
with Listener(on_press=key_code) as f:
    f.join() 