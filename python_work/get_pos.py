import keyboard
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

# pyautogui의 keyboard press는 막힘
def on_key_press():
  print(mouse.get_position())
  # keyboard.press('ctrl+c')

windows = gw.getWindowsWithTitle('Gersang')

mouse.on_click(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)