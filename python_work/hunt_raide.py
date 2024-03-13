import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

# GLOBAL scope
kb = Controller()
result = list()
threads = []
arrows = [Key.left, Key.up, Key.right, Key.down]
resv_attack_cnt = {
  "raide": {
    2: 2,
    1: 2,
    5: 2,
    4: 1,
  },
}
window = None
monster = "raide"
found = ""

def init():
  global window
  global monster

  # focus on window
  window = None
  windows = gw.getWindowsWithTitle('Gersang')

  for w in windows:
    if w.title != 'Gersang':
      continue
    w.activate()
    window = w
    # pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))


def pressAndRelease(key):

  keyboard.press(key)
  time.sleep(.0185)
  keyboard.release(key)
  time.sleep(.0185)

def debuf():
  pressAndRelease('7')
  pressAndRelease('r')
  time.sleep(.01)
  # pressAndRelease('3')
  # pressAndRelease('r')
  # time.sleep(.01)
  # pressAndRelease('6')
  # pressAndRelease('r')
  # time.sleep(.01)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window
  global monster
  global resv_attack_cnt

  if event.name == 'a':
    kb.press(Key.left)
    time.sleep(.71)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.71)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.71)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.71)
    kb.release(Key.down)

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':

    debuf()

    # for k, v in resv_attack_cnt[monster].items():
    #   pressAndRelease(f"{k}")
    #   pag.click(button='right')
    pressAndRelease('`')
    mouse.press(button='right')
    time.sleep(.01)
    mouse.release(button='right')
    time.sleep(.01)
    pressAndRelease('=')

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
  # dosa_sim 6r 1reee  5reeee  2reeee  4reee
  # dosa_gak 6r 1reeee 5reeeee 2reeeee 4reeee
  elif event.name == 'c':
    for k, v in resv_attack_cnt[monster].items():
      pressAndRelease(f"{k}")
      pressAndRelease('r')
      # print(f"r pressed")
      for _ in range(v):
        pressAndRelease('e')
      time.sleep(0.01)

  elif event.name == 'x':
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')
    time.sleep(.1)
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')

if __name__ == "__main__":
  init()

  keyboard.on_press(on_key_press)
  # Keep the program running until you press the Esc key
  # keyboard.add_hotkey('ctrl+c', quit)
  # keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
  keyboard.wait('ctrl+c')