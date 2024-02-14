import random
import keyboard
import time
from datetime import datetime
import pyautogui as pag
import pygetwindow as gw
from pynput.keyboard import Key, Controller
kb = Controller()

window = None

def do_init():
  global window
  
  for w in gw.getWindowsWithTitle('Gersang'):
    if w.title != 'Gersang':
      continue
    w.activate()
    window = w

do_init()

def on_key_press(event):
  global window
  global monster
  global resv_attack_cnt

  if event.name == 'esc':
    pass
  elif event.name == 'x':
    file = round(datetime.now().timestamp())
    pag.screenshot(f'python_work/s_{file}.png', region=(window.left, window.top, window.width, window.height))
    kb.press(Key.ctrl)
    kb.press('c')

    # 포만감
    # width = round(window.width*.2544)
    # height = round(window.height*(.857))
    # print(f"width : {width}")
    # print(f"height : {height}")
    # print(f"width : {width}")
    # print(f"height : {height}")
    # pag.screenshot(f'python_work/s_{file}.png', region=(
    #         window.left+58
    #         , window.top + height
    #         , width-78
    #         , (window.height-height)//4
    #         )
    #       )

keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')