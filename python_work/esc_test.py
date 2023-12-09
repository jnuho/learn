import keyboard
import time
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
    print('esc is pressed')
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')
    time.sleep(.1)
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')

    time.sleep(2)

    keyboard.press('alt')
    time.sleep(.02)
    keyboard.press('2')
    time.sleep(.02)
    keyboard.release('alt')
    time.sleep(.02)
    keyboard.release('2')
    time.sleep(.02)

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