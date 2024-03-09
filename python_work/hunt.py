import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

from threading import Thread

# GLOBAL scope
kb = Controller()
result = list()
threads = []
arrows = [Key.left, Key.up, Key.right, Key.down]
resv_attack_cnt = {
  "dosa_sim": {
    2: 3,
    1: 3,
    5: 3,
    4: 3,
    # 6: 1,
  },
  "dosa_gak": {
    2: 5,
    1: 4,
    5: 5,
    4: 4,
    6: 1,
  },
  "baek": {
    2: 0,
    1: 0,
    5: 0,
    4: 1,
    6: 2,
  },
}
monsters = {
  "dosa_sim": {
    3: [1,2,3,4]
    , 6: [1,2,3,4]
    , 9: [1,2,3]
    , 12: [1,2,3,4]
  },
  "dosa_gak": {
    3: [1,2,3,4]
    , 6: [1,2,3,4]
    , 9: [1,2,3]
    , 12: [1,2,3,4]
  },
  "baek": {
    3: [1,2]
    , 6: [1]
    , 9: [1,2]
    , 12: [1,2,3]
  },
}
monster = "dosa_gak"
interval = .02
img_found = ""

# do work on image recognition
def work(monster, dir, idx, result):
  global img_found
  global arrows
  image_path = f'python_work/img/{monster}/{dir}-{idx}.png'
  try:
    pos = pag.locateCenterOnScreen(image_path, confidence=.92, grayscale=True)
    img_found = f"{dir}-{idx}"
    print(f"{img_found} at ({pos.x},{pos.y}).")
    result.append(arrows[dir//3 - 1])
    return
  except pag.ImageNotFoundException:
    # print(f"{dir}_{idx} None")
    return

# initialize threads
def init_thread(monster):
  global result
  global monsters
  global threads

  result = list()
  threads = []
  for key, val in monsters[monster].items():
    for idx in val:
      threads.append(Thread(target=work, args=(monster, key, idx, result)))
  print("Threads init done.\n")


def init():
  global window
  global monster

  init_thread(monster)

  # focus on window
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
  global interval

  keyboard.press(key)
  time.sleep(interval)
  keyboard.release(key)
  time.sleep(interval)

def get_food():
  food_image = "python_work/img/food.png"
  try:
    pos_found = pag.locateCenterOnScreen(food_image, confidence=.93, grayscale=True)
    # 150 포만감 바 = 687-537
    # 248: 포만감 100%
    # 포만감-310 일때 길이: 225
    x_diff = pos_found.x-window.left
    if x_diff < 224:
      keyboard.press('alt')
      time.sleep(.05)
      for i in range(2):
        keyboard.press('2')
        time.sleep(.2)
        keyboard.release('2')
        time.sleep(.2)
      keyboard.release('alt')
  except pag.ImageNotFoundException:
    pass

def debuf(arrow):
  if img_found == "12-2" and monster == "dosa_gak":
    pag.moveTo(window.left + window.width*.43, window.top + window.height*.44)

  kb.press(arrow)
  time.sleep(.78)
  kb.release(arrow)
  time.sleep(.01)

  pressAndRelease('7')
  pressAndRelease('r')
  time.sleep(.01)
  # pressAndRelease('3')
  # pressAndRelease('r')
  # time.sleep(.01)
  # pressAndRelease('6')
  # pressAndRelease('r')
  # time.sleep(.01)

  # for k, v in resv_attack_cnt[monster].items():
  #   pressAndRelease(f"{k}")
  #   pag.click(button='right')
  pressAndRelease('`')
  mouse.press(button='right')
  time.sleep(.01)
  mouse.release(button='right')
  time.sleep(.01)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window
  global monster
  global resv_attack_cnt

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
  # elif event.name == ',':
  #   pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    pag.moveTo(window.left + window.width/2, window.top + window.height/2)
    arrow = start_arrowkey_thread()
    pressAndRelease('9')
    pressAndRelease('r')

    if arrow != None:
      debuf(arrow)
    else:
      print("image failed.")
      pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))
      init_thread(monster)


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

    init_thread(monster)

    time.sleep(1.7)

    # 1~2번 랜덤으로 
    # 1: 50%
    # 2: 50%
    get_food()
    # random.seed(datetime.now().timestamp())
    # n = random.randint(1, 2)

if __name__ == "__main__":
  init()

  keyboard.on_press(on_key_press)
  # Keep the program running until you press the Esc key
  # keyboard.add_hotkey('ctrl+c', quit)
  # keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
  keyboard.wait('ctrl+c')