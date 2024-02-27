import keyboard
import mouse
import time
import datetime
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

def moveto_l_click(x, y):
  pag.moveTo(x,y)
  mouse.press(button='left')
  time.sleep(.2)
  mouse.release(button='left')
  time.sleep(.5)


def mouse_r_click():
  mouse.press(button='right')
  time.sleep(.2)
  mouse.release(button='right')
  time.sleep(1)

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(.2)
    keyboard.release(key)
    time.sleep(.4)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'a':
    while True:
      time.sleep(1)
      print(datetime.datetime.now())

      windows = gw.getWindowsWithTitle('Gersang')

      for w in windows:
        if w.title != 'Gersang':
          continue

        w.minimize()
        time.sleep(.5)
        w.restore()
        time.sleep(.5)
        w.activate()
        time.sleep(.5)

        moveto_l_click(w.left + (w.width*.2049), w.top + (w.height*.4341))
        moveto_l_click(w.left + (w.width*.501), w.top + (w.height*.5684))
        pressAndRelease('esc')
        pressAndRelease('i')

        # Food
        pag.moveTo(w.left + (w.width*.5835), w.top + (w.height*.2484))
        time.sleep(.5)

        mouse_r_click()
        mouse_r_click()
        mouse_r_click()
        mouse_r_click()

        time.sleep(.5)
        pressAndRelease('j')
        time.sleep(.3)
        moveto_l_click(w.left + (w.width*.2049), w.top + (w.height*.4341))
        moveto_l_click(w.left + (w.width*.501), w.top + (w.height*.5684))
        time.sleep(.3)
        pressAndRelease('j')

      time.sleep(25*60)


keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)