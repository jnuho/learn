import keyboard
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

import random
from datetime import datetime
from threading import Thread

# GLOBAL scope
kb = Controller()
result = list()
threads = []
monsters = {
  "dosa_sim": {
    3: [1,2,3]
    , 6: [1,2,3]
    , 9: [1,2,3]
    , 12: [1,2,3]
  },
  "dosa_gak": {
    3: [1,2,3]
    , 6: [1,2,3]
    , 9: [1,2,3]
    , 12: [1,2,3]
  }
}
monster = "dosa_sim"
# monster = "dosa_gak"
found = ""

# dir: 3,6,9,12
# left, up, right, down
def work(monster, dir, idx, result):
  global found
  image_path = f'python_work/img/{monster}/{dir}_{idx}.png'
  try:
    pos_found = pag.locateCenterOnScreen(image_path, confidence=.93, grayscale=True)
    print(f"image {dir}_{idx} : {pos_found} was found.")
    found = f"{dir}_{idx}"
    arrows = [Key.left, Key.up, Key.right, Key.down]
    result.append(arrows[dir//3 - 1])
    return
  except pag.ImageNotFoundException:
    # print(f"{dir}_{idx} None")
    return

def init_thread(monster):
  global result
  global monsters
  global threads

  # monsters = {
  #   "dosa_sim": {
  #     3: [1,2,3]
  #     , 6: [1,2,3]
  #     , 9: [1,2,3]
  #     , 12: [1,2,3]
  #   },
  #   "dosa_gak": {
  #     3: []
  #     , 6: []
  #     , 9: []
  #     , 12: []
  #   }
  # }

  result = list()
  threads = []
  for key, val in monsters[monster].items():
    for idx in val:
      threads.append(Thread(target=work, args=(monster, key, idx, result)))

  print(f"Thread init done. {datetime.now()}")

init_thread(monster)

window = None
windows = gw.getWindowsWithTitle('Gersang')

for w in windows:
  if w.title != 'Gersang':
    continue
  w.activate()
  window = w
  # pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))


def start_arrowkey_thread():
  global result
  global threads

  for t in threads:
    t.start()
  for t in threads:
    t.join()

  # print(f'Arrow key results={result}')
  if len(result) > 0:
    return result[0]
  else:
    return None

def pressAndRelease(key):
  keyboard.press(key)
  time.sleep(0.017)
  keyboard.release(key)
  time.sleep(0.017)

# def r_click(*kwargs):
#   pag.click(button='right') 
#   c = kwargs.get('thread', None)
#   if c != None:
#     init_thread()


# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window
  global monster

  if event.name == 'esc':
    init_thread(monster)
  elif event.name == 'a':
    kb.press(Key.left)
    time.sleep(.7)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.7)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.7)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.7)
    kb.release(Key.down)

  # screenshot
  elif event.name == 't':
    pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    arrow = start_arrowkey_thread()
    if arrow != None:
      if monster == "dosa_gak" and found == "12_2":
        pag.moveTo(window.left + window.width*5/12, window.top + window.height*5/12)
      else:
        pag.moveTo(window.left + window.width/2, window.top + window.height/2)
      kb.press(arrow)
      time.sleep(.78)
      kb.release(arrow)
    else:
      print("image failed.")
      pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

    pressAndRelease('8')
    pressAndRelease('r')
    pressAndRelease('3')
    pressAndRelease('r')

    pressAndRelease('2')
    pag.click(button='right') 
    time.sleep(.01)
    # pag.mouseDown(button='right')
    # pag.mouseUp(button='right'

    pressAndRelease('5')
    pag.click(button='right') 

    pressAndRelease('1')
    pag.click(button='right') 

    pressAndRelease('6')
    pag.click(button='right') 

    pressAndRelease('4')
    pag.click(button='right') 
    time.sleep(.01)

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
  # dosa_sim 6r 1rrrr 5rrrrr 2rrrrr 4rrrr
  # dosa_gak 6r 1rrrrr 5rrrrrr 2rrrrrr 4rrrrr
  elif event.name == 'e':
    pressAndRelease('6')
    pressAndRelease('r')
    # pressAndRelease('t')
    # kb.press(Key.ctrl)
    # pressAndRelease('t')
    # pressAndRelease('t')
    # kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('1')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('5')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('2')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('4')
    pressAndRelease('r')
    kb.press(Key.ctrl)
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    pressAndRelease('r')
    kb.release(Key.ctrl)
    time.sleep(0.01)

  elif event.name == 'x':
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')
    time.sleep(.1)
    keyboard.press('esc')
    time.sleep(.1)
    keyboard.release('esc')

    init_thread(monster)

    time.sleep(1.5)

    # 1~2번 랜덤으로 
    # 1: 50%
    # 2: 50%
    random.seed(datetime.now().timestamp())
    n = random.randint(1, 2)

    keyboard.press('alt')
    time.sleep(.05)
    for i in range(1,n+1):
      keyboard.press('2')
      time.sleep(.2)
      keyboard.release('2')
      time.sleep(.2)
      if i == n:
        keyboard.release('alt')

# mouse.on_right_click(on_right_mouse_click)

# def main():
keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

  # res = pag.locateOnScreen("edit.png")
  # print(res)

# if __name__ == "__main__":
#     main()