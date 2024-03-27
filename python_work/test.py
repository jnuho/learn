import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

# GLOBAL scope
kb = Controller()
window = None

def init():
  global window
  windows = gw.getWindowsWithTitle('Gersang')

  for w in windows:
    if w.title != 'Gersang':
      continue
    w.activate()
    window = w

def pressAndRelease(key):

  keyboard.press(key)
  time.sleep(.018)
  keyboard.release(key)
  time.sleep(.018)


# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window

  if event.name == 'enter':
    print("dsds")

if __name__ == "__main__":
  init()

  keyboard.on_press(on_key_press)
  # Keep the program running until you press the Esc key
  # keyboard.add_hotkey('ctrl+c', quit)
  # keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
  keyboard.wait('ctrl+c')