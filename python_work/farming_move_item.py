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
    i = 0
    time.sleep(1)
    while i < 3:
      game_window = gw.getWindowsWithTitle('Gersang')[i]
      print(game_window)
      game_window.minimize()
      time.sleep(.5)
      game_window.restore()
      time.sleep(.5)
      # game_window.activate()
      moveto_l_click(243,448)
      moveto_l_click(601,437)
      pressAndRelease('j')
      pressAndRelease('2')
      moveto_l_click(343,455)
      moveto_l_click(860,437)
      moveto_l_click(990,519)
      moveto_l_click(989,599)
      moveto_l_click(406,455)
      moveto_l_click(860,436)

      time.sleep(.5)

      moveto_l_click(991,516)
      moveto_l_click(990,594)
      moveto_l_click(342,514)
      moveto_l_click(861,439)
      moveto_l_click(993,522)
      moveto_l_click(992,600)
      pressAndRelease('j')

      time.sleep(.5)

      moveto_l_click(960,407)
      moveto_l_click(605,424)
      moveto_l_click(736,505)
      moveto_l_click(735,579)
      moveto_l_click(896,474)
      moveto_l_click(601,420)
      moveto_l_click(731,503)
      moveto_l_click(733,577)
      pressAndRelease('j')
      moveto_l_click(378,375)
      i += 1

keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)