import keyboard
import os
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

# import psutil
import subprocess

# GLOBAL scope
kb = Controller()
def init():
  global window
  global monster

  # focus on window
  window = None
  windows = gw.getWindowsWithTitle('Calculator')

  for w in windows:
    if w.title == 'Calculator':
      w.activate()
      window = w

# at program start
init()

def pressAndRelease(key):
  keyboard.press(key)
  time.sleep(0.0185)
  keyboard.release(key)
  time.sleep(0.0185)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'a':
    # for proc in psutil.process_iter():
    #   proc.kill()
    os.system("taskkill /f /im CalculatorApp.exe")

keyboard.on_press(on_key_press)

keyboard.wait('ctrl+c')

# PoWErshell:
# get-appxpackage *calculator* -allusers
# C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2311.0.0_x64__8wekyb3d8bbwe\CalculatorApp.exe