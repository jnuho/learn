import keyboard
import time
import datetime
import pygetwindow as gw

from pynput.keyboard import Key, Controller

kb = Controller()
count=0

def on_key_press(event):
  pass
  # if event.name == 'esc':
  #   print("esc")
  # elif event.name == 'ctrl+c':
  #   print("ctrl+c")

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(.2)
    keyboard.release(key)
    time.sleep(.4)

def do_work():
  global count
  # pyautogui의 keyboard press는 막힘
  while True:
    windows = gw.getWindowsWithTitle('Gersang')

    for window in windows:
      if window.title != 'Gersang':
        continue

      print(datetime.datetime.now())
      # if count == 0:
      window.minimize()
      time.sleep(.5)
      window.restore()
      time.sleep(.5)
      window.activate()
      time.sleep(.5)
      pressAndRelease('enter')
      pressAndRelease('1')
      pressAndRelease('enter')

      time.sleep(.5)
      count = count+1

    # 3분마다 enter 1
    time.sleep(3*60)

do_work()
# keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')
