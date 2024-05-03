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
  global monster

  # focus on window
  window = None
  windows = gw.getWindowsWithTitle('Gersang')

  for w in windows:
    if w.title != 'Gersang':
      continue
    # w.activate()
    window = w

def pressAndRelease(key):
  keyboard.press(key)
  time.sleep(.0183)
  keyboard.release(key)
  time.sleep(.0183)

def get_food():
  food_image = "images/food.png"
  try:
    pos_found = pag.locateCenterOnScreen(food_image, confidence=.93, grayscale=True)
    # 150 포만감 바 = 687-537
    # 248: 포만감 100%
    # 포만감-310 일때 길이: 225
    x_diff = pos_found.x-window.left
    # if x_diff < 224:
    if x_diff < 234:
      keyboard.press('alt')
      time.sleep(.05)
      for i in range(1):
        keyboard.press('2')
        time.sleep(.2)
        keyboard.release('2')
        time.sleep(.2)
      keyboard.release('alt')
  except pag.ImageNotFoundException:
    print("NOT FOUND")


def on_key_press(event):
  global window

  if event.name == 'x':
    food_image = "images/food.png"
    try:
      pos_found = pag.locateCenterOnScreen(food_image, confidence=.93, grayscale=True)
      x_diff = pos_found.x-window.left
      print(x_diff)
    except pag.ImageNotFoundException:
      print("NOT FOUND")



if __name__ == "__main__":
  init()

  keyboard.on_press(on_key_press)
  keyboard.wait('ctrl+c')