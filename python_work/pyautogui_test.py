import pyautogui as pag
from pynput.keyboard import Key, Controller
import pygetwindow as gw
import time

kb = Controller()

a =pag.position()
pag.screenshot('python_work/1.png', region=(400,100, 1200, 1000))
# button7location = pag.locateCenterOnScreen('python_work/1.png', confidence=0.9, grayscale=True)
# print(button7location)

windows = gw.getWindowsWithTitle('Gersang')
for window in windows:
  if window.title != 'Gersang':
    continue
  game_window = windows[0]
  game_window.activate()
  print(game_window)