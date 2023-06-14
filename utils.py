import pyautogui

def move_and_click(position, side_button, click= 1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks= click )

def get_loot(PLAYER_POSITION, BP_LOOT_POSITION1 ):
    move_and_click(PLAYER_POSITION, 'right')
    move_and_click(BP_LOOT_POSITION1, 'left', 2)