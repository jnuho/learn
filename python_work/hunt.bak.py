import keyboard
import time
import random
from datetime import datetime
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

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
    time.sleep(.8)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.8)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.8)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.8)
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
    time.sleep(.01)

    pressAndRelease('6')
    pag.click(button='right') 
    time.sleep(.01)

    pressAndRelease('4')
    pag.click(button='right') 
    time.sleep(.01)
    pag.mouseUp(button='right')

    print('허영')

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
  elif event.name == 'e':
    pressAndRelease('6')
    pressAndRelease('r')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    time.sleep(0.01)

    pressAndRelease('2')
    pressAndRelease('r')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    time.sleep(0.01)

    pressAndRelease('5')
    pressAndRelease('r')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    time.sleep(0.01)

    pressAndRelease('4')
    pressAndRelease('r')
    pressAndRelease('e')
    pressAndRelease('e')
    pressAndRelease('e')
    time.sleep(0.01)

    print('예약시전')

  elif event.name == 'space':

    pressAndRelease('esc')
    pressAndRelease('esc')
    time.sleep(2)

    # food 1 or 2 times
    random.seed(datetime.now().timestamp())
    # food_cnt = random.randint(1,2)

    for i in range(2):
      keyboard.press('alt')
      time.sleep(.02)
      keyboard.press('2')
      time.sleep(.02)
      keyboard.release('alt')
      time.sleep(.02)
      keyboard.release('2')
      time.sleep(.02)

game_window = gw.getWindowsWithTitle('Gersang')[0]
game_window.activate()
keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)