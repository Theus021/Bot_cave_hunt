import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
from HundlerPoke import HundlerPoke
from utils import get_loot
from utils import move_and_click

PLAYER_POSITION = (686, 369)
BP_LOOT_POSITION1 = (1192, 663)
LIST_ATTACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
BATTLE_POSITION = (1245, 128)

hundler_poke = HundlerPoke()
auto_cast = True
 

def key_code(key):
    global auto_cast
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        move_and_click(BATTLE_POSITION, 'left')
        for attack in LIST_ATTACK:
            pyautogui.press(attack)

    if hasattr(key, 'char') and key.char == "e":
        hundler_poke.next()

    if hasattr(key, 'char') and key.char == "q":
        hundler_poke.previues()  

    if hasattr(key, 'char') and key.char == "2":   
        get_loot(PLAYER_POSITION, BP_LOOT_POSITION1) 
    
    if hasattr(key, 'char') and key.char == "1":  
       if auto_cast == True:
            for attack in LIST_ATTACK:
                pyautogui.keyDown(attack)
            auto_cast = False    
       else :     
            for attack in LIST_ATTACK:
                pyautogui.keyUp(attack)

with Listener(on_release=key_code) as f:
    f.join() 