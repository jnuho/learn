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

      for window in windows:
        if window.title != 'Gersang':
          continue

        window.minimize()
        time.sleep(.5)
        window.restore()
        time.sleep(.5)
        # game_window.activate()
        moveto_l_click(239,423)
        moveto_l_click(605,437)
        pressAndRelease('i')
        pressAndRelease('2')
        pressAndRelease('esc')
        pag.moveTo(701,471)
        time.sleep(.5)

        mouse_r_click()
        mouse_r_click()
        mouse_r_click()
        mouse_r_click()

        # pag.click(button='right') 
        # time.sleep(1)
        # pag.click(button='right') 
        # time.sleep(1)
        # pag.click(button='right') 
        # time.sleep(1)
        # pag.click(button='right') 
        # time.sleep(1)
        pressAndRelease('j')
        moveto_l_click(381,376)
        time.sleep(.5)

      time.sleep(25*60)


keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)