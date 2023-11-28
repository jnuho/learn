import keyboard
import mouse
import time
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

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(.2)
    keyboard.release(key)
    time.sleep(.4)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'a':
    time.sleep(1)

    windows = gw.getWindowsWithTitle('Gersang')

    for window in windows:
      if window.title != 'Gersang':
        continue

      print(window)
      window.minimize()
      time.sleep(.5)
      window.restore()
      time.sleep(.5)
      # game_window.activate()
      moveto_l_click(297,345)
      moveto_l_click(601,450)

      # MOVE ITEMS
      moveto_l_click(290, 467)
      moveto_l_click(688, 501)
      moveto_l_click(819, 589)
      moveto_l_click(818, 664)
      
      moveto_l_click(338, 464)
      moveto_l_click(688, 501)
      moveto_l_click(819, 589)
      moveto_l_click(818, 664)
      
      moveto_l_click(385, 464)
      moveto_l_click(688, 501)
      moveto_l_click(819, 589)
      moveto_l_click(818, 664)

      # 아이템버리기
      pressAndRelease('j')
      
      moveto_l_click(783, 198)
      moveto_l_click(607, 202)
      moveto_l_click(733, 276)
      moveto_l_click(745, 360)
      
      moveto_l_click(817, 198)
      moveto_l_click(607, 202)
      moveto_l_click(733, 276)
      moveto_l_click(745, 360)

      #다시시작
      pressAndRelease('j')
      moveto_l_click(297,345)

keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)