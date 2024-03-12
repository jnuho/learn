import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

from threading import Thread

# GLOBAL scope
kb = Controller()
img_found = ""

def init():
  global window
  global monster

  # init_thread(monster)

  # focus on window
  window = None
  windows = gw.getWindowsWithTitle('Gersang')

  for w in windows:
    if w.title != 'Gersang':
      continue
    w.activate()
    window = w
    # pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

# do work on image recognition
def work():
  image_path = 'python_work/img/yuk_add.png'
  try:
    pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
    return
  except pag.ImageNotFoundException:
    # print(f"{dir}_{idx} None")
    return


def pressAndRelease(key):
  keyboard.press(key)
  time.sleep(0.0185)
  keyboard.release(key)
  time.sleep(0.0185)

def mouse_l_click(x, y):
  pag.moveTo(x,y)
  mouse.press(button='left')
  time.sleep(.2)
  mouse.release(button='left')
  time.sleep(.5)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window

  if event.name == ',':
    for i in range(5):
      try:
        image_path = 'python_work/img/yuk_add.png'
        pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
        mouse_l_click(pos.x, pos.y)
        time.sleep(.01)

        image_path = 'python_work/img/yuk_ok1.png'
        pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
        mouse_l_click(pos.x, pos.y)
        time.sleep(.01)

        image_path = 'python_work/img/yuk_ok2.png'
        pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
        mouse_l_click(pos.x, pos.y)
        time.sleep(.02)
        # return
      except pag.ImageNotFoundException:
        print("image recognition failed")
        # return



  # screenshot
  # elif event.name == ',':
  #   pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))


if __name__ == "__main__":
  init()

  keyboard.on_press(on_key_press)
  # Keep the program running until you press the Esc key
  # keyboard.add_hotkey('ctrl+c', quit)
  # keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
  keyboard.wait('ctrl+c')