import keyboard
import time
import datetime
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()


def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(.2)
    keyboard.release(key)
    time.sleep(.4)

# pyautogui의 keyboard press는 막힘
count=0
while True:
  windows = gw.getWindowsWithTitle('Gersang')

  for window in windows:
    if window.title != 'Gersang':
      continue

    # if count == 0:
    window.minimize()
    window.restore()

    time.sleep(.5)
    pressAndRelease('enter')
    pressAndRelease('1')
    pressAndRelease('enter')

    time.sleep(.5)
    count = count+1

  # 10분마다 enter 1
  time.sleep(10*60)

