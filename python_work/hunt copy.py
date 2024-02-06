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

windows = gw.getWindowsWithTitle('Gersang')
for window in windows:
  if window.title != 'Gersang':
    continue
  game_window = windows[0]
  game_window.activate()
  pag.screenshot('python_work/1.png', region=(game_window.left, game_window.top, game_window.width, game_window.height))

# dir: 3,6,9,12
# left, up, right, down
def work(monster, dir, idx, result):
  image_path = f'python_work/img/{monster}_{dir}_{idx}.png'
  try:
    pos_found = pag.locateCenterOnScreen(image_path, confidence=.93, grayscale=True)
    print(f"{dir}_{idx} : {pos_found}")
    arrows = [Key.left, Key.up, Key.right, Key.down]
    result.append(arrows[dir//3 - 1])
    return
  except pag.ImageNotFoundException:
    # print(f"{dir}_{idx} None")
    return

result = list()

threads = [
  Thread(target=work, args=("dosa_sim", 3, 1, result))
  , Thread(target=work, args=("dosa_sim", 3, 2, result))
  , Thread(target=work, args=("dosa_sim", 3, 3, result))
  , Thread(target=work, args=("dosa_sim", 6, 1, result))
  , Thread(target=work, args=("dosa_sim", 6, 2, result))
  , Thread(target=work, args=("dosa_sim", 6, 3, result))
  , Thread(target=work, args=("dosa_sim", 9, 1, result))
  , Thread(target=work, args=("dosa_sim", 9, 2, result))
  , Thread(target=work, args=("dosa_sim", 9, 3, result))
  , Thread(target=work, args=("dosa_sim", 12, 1, result))
  # TODO: 9시인경우에, 12_2가 9_2와 중복. 12_2를 다시 캡쳐하기!
  , Thread(target=work, args=("dosa_sim", 12, 2, result))
  , Thread(target=work, args=("dosa_sim", 12, 3, result))
]

def get_arrow_key():
  for t in threads:
    if t.is_alive() == False:
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
  time.sleep(0.02)
  keyboard.release(key)
  time.sleep(0.02)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  if event.name == 'a':
    kb.press(Key.left)
    time.sleep(.67)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.67)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.67)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.67)
    kb.release(Key.down)

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    pag.moveTo(game_window.left + game_window.width/2, game_window.top + game_window.height/2)
    pag.screenshot('python_work/1.png', region=(game_window.left, game_window.top, game_window.width, game_window.height))

    arrow=get_arrow_key()
    if arrow != None:
      kb.press(arrow)
      time.sleep(.77)
      kb.release(arrow)
    else:
      print("Image recognition failed!")

    pressAndRelease('8')
    pressAndRelease('r')
    pressAndRelease('3')
    pressAndRelease('r')

    pressAndRelease('2')
    pag.click(button='right') 
    time.sleep(.01)
    # pag.mouseDown(button='right')
    # pag.mouseUp(button='right')

    pressAndRelease('5')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('1')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('6')
    pag.click(button='right') 
    # time.sleep(.01)

    pressAndRelease('4')
    pag.click(button='right') 
    time.sleep(.01)

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
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
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('5')
    pressAndRelease('r')
    kb.press(Key.ctrl)
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
    kb.release(Key.ctrl)
    time.sleep(0.01)

    pressAndRelease('4')
    pressAndRelease('r')
    kb.press(Key.ctrl)
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

    time.sleep(2.0)

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