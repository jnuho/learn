import keyboard
import mouse
import time
import os
import pyautogui as pag
import pygetwindow as gw
from pywinauto import Application
import subprocess

from pynput.keyboard import Key, Controller


kb = Controller()
window = None

# a =pag.position()
# pag.screenshot('python_work/1.png', region=(400,100, 1200, 1000))
# button7location = pag.locateCenterOnScreen('python_work/1.png', confidence=0.9, grayscale=True)
# print(button7location)


def kill_others():

  # focus on window
  # windows = gw.getWindowsWithTitle('MINGW64:/c/Users/user/Repos')
  windows = gw.getWindowsWithTitle('MINGW64')

  for _, w in enumerate(windows):
    # Connect to the application using pywinauto and get the process ID
    app = Application().connect(handle=w._hWnd)
    pid = app.process
    
    # Kill the process
    os.system(f'taskkill /PID {pid} /F')



def open():
  path = 'C:\Program Files\Git\git-bash.exe'
  os.system('start "" "' + path+ '"')
  time.sleep(1.5)

  window = gw.getWindowsWithTitle('MINGW64')[0]
  window.maximize()
  window.activate()
  pag.write("tmux")
  keyboard.press("enter")
  time.sleep(.1)
  keyboard.release("enter")

  exit(0)


def configure():
  keyboard.press("ctrl")
  time.sleep(.5)
  keyboard.press("a")
  time.sleep(.5)
  keyboard.release("a")
  time.sleep(.5)
  keyboard.release("ctrl")
  time.sleep(.5)
  keyboard.press("shift")
  time.sleep(.5)
  keyboard.press("5")
  time.sleep(.5)
  keyboard.release("5")
  time.sleep(.5)
  keyboard.release("shift")
  time.sleep(.5)
  pag.write("tmux")


if __name__ == "__main__":
  kill_others()

  open()

  # configure()
