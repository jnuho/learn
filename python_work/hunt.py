import keyboard
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

import random
from datetime import datetime

kb = Controller()

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(0.02)
    keyboard.release(key)
    time.sleep(0.02)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'a':
    kb.press(Key.left)
    time.sleep(.65)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.65)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.65)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.65)
    kb.release(Key.down)

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    pressAndRelease('8')
    pressAndRelease('r')
    pressAndRelease('3')
    pressAndRelease('r')

    pressAndRelease('2')
    pag.click(button='right') 
    time.sleep(.01)
    # pag.mouseDown(button='right')
    # pag.mouseUp(button='right')

    pressAndRelease('5')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('1')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('6')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('4')
    pag.click(button='right') 
    time.sleep(.01)

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
  elif event.name == 'e':
    pressAndRelease('6')
    pressAndRelease('r')
    # pressAndRelease('t')
    # kb.press(Key.ctrl)
    # pressAndRelease('t')
    # pressAndRelease('t')
    # kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('1')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('5')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('2')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('4')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

  elif event.name == 'x':
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')
    time.sleep(.1)
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')

    time.sleep(2.0)

    # 1~2번 랜덤으로 
    # 1: 66%
    # 2: 33%
    random.seed(datetime.now().timestamp())
    n = random.randint(0, 2)
    if n < 2:
      n = 1

    keyboard.press('alt')
    time.sleep(.05)
    for i in range(1,n+1):
      keyboard.press('2')
      time.sleep(.2)
      keyboard.release('2')
      time.sleep(.2)
      if i == n:
        keyboard.release('alt')

windows = gw.getWindowsWithTitle('Gersang')
if len(windows) > 0:
  game_window = windows[0]
  game_window.activate()
else:
  print("Gersang not running!")
  exit(1)

keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)