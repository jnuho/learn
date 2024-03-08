import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'f':
    for i in range (20):
      # 필드에서는 right 클릭안됨
      # pag.click(button='right') 
      mouse.press(button='right')
      time.sleep(.1)
      mouse.release(button='right')
      time.sleep(.1)
      # mouse.click('left')
      # mouse.press(button='left')
      # time.sleep(.1)
      # mouse.release(button='left')


game_window = gw.getWindowsWithTitle('Gersang')[0]
game_window.activate()
keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)