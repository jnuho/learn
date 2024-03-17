import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

def init():
  pag.FAILSAFE = False

def mouse_l_click(x, y):
  pag.moveTo(x,y)
  mouse.press(button='left')
  time.sleep(.1)
  mouse.release(button='left')
  time.sleep(.1)

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(.2)
    keyboard.release(key)
    time.sleep(.4)

# pyautogui의 keyboard press는 막힘
# def on_key_press(event):
#   if event.name == 'a':
#     pass

def eat():
  windows = gw.getWindowsWithTitle('Gersang')

  for w in windows:
    if w.title != 'Gersang':
      continue

    print(w)
    w.minimize()
    time.sleep(.5)
    w.restore()
    time.sleep(.5)
    # w.activate()
    # time.sleep(.5)

    # game_window.activate()


    for i in range(1):
      # mouse_l_click(w.left + (w.width*.5796), w.top + (w.height*.6261))
      pag.moveTo(w.left + (w.width*.5796), w.top + (w.height*.6261))
      time.sleep(.5)
      mouse.press(button='right')
      time.sleep(.1)
      mouse.release(button='right')
      time.sleep(.5)
      mouse_l_click(w.left + (w.width*.5194), w.top + (w.height*.5646))

      # 고고학 확인창
      # mouse_l_click(w.left + (w.width*.6165), w.top + (w.height*.5834))
      try:
        image_path = 'python_work/img/btn_ok.png'
        pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
        mouse_l_click(pos.x, pos.y)
        time.sleep(.03)

        image_path = 'python_work/img/btn_ok_yumul.png'
        pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
        mouse_l_click(pos.x, pos.y)
      except pag.ImageNotFoundException:
        print("image recognition failed")
        exit
        # return


if __name__ == "__main__":
  init()
  eat()

  # keyboard.on_press(on_key_press)

  # Keep the program running until you press the Esc key
  # keyboard.add_hotkey('ctrl+c', quit)
  # keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
  keyboard.wait('ctrl+c')

