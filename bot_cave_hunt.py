import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
from HundlerPoke import HundlerPoke
from utils import get_loot

PLAYER_POSITION = (686, 369)
BP_LOOT_POSITION1 = (1192, 663)

hundler_poke = HundlerPoke()
 

def key_code(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        get_loot(PLAYER_POSITION, BP_LOOT_POSITION1)
    if hasattr(key, 'char') and key.char == "e":
        hundler_poke.next()
    if hasattr(key, 'char') and key.char == "q":
        hundler_poke.previues()    
    
with Listener(on_press=key_code) as f:
    f.join() 