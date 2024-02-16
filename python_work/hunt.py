import keyboard
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
    1: 3
    , 5: 3
    , 2: 3
    , 4: 3
    # , 6: 1
  },
  "dosa_gak": {
    1: 4
    , 5: 5
    , 2: 5
    , 4: 4
    , 6: 1
  },
  "baek": {
    1: 0
    , 5: 0
    , 2: 0
    , 4: 1
    , 6: 2
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
    3: [1,2,3]
    , 6: [1,2,3]
    , 9: [1,2,3]
    , 12: [1,2,3]
  },
  "baek": {
    3: [1,2]
    , 6: [1]
    , 9: [1,2]
    , 12: [1,2,3]
  },
}
monster = "dosa_gak"
found = ""

# do work on image recognition
def work(monster, dir, idx, result):
  global found
  global arrows
  image_path = f'python_work/img/{monster}/{dir}-{idx}.png'
  try:
    pos_found = pag.locateCenterOnScreen(image_path, confidence=.93, grayscale=True)
    found = f"{dir}-{idx}"
    print(f"{found} at ({pos_found.x},{pos_found.y}).")
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

# at program start
init()

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
  time.sleep(0.0185)
  keyboard.release(key)
  time.sleep(0.0185)

def get_food():
  food_image = "python_work/img/food.png"
  try:
    pos_found = pag.locateCenterOnScreen(food_image, confidence=.93, grayscale=True)
    # pag.moveTo(window.left + window.width/2, window.top + window.height/2)
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

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window
  global monster
  global resv_attack_cnt

  # if event.name == 'esc':
  #   init_thread(monster)
  if event.name == 'a':
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
  elif event.name == ',':
    pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    pag.moveTo(window.left + window.width/2, window.top + window.height/2)
    arrow = start_arrowkey_thread()
    if arrow != None:
      if monster == "dosa_gak" and found == "12-2":
        pag.moveTo(window.left + window.width*5/12, window.top + window.height*5/12)
      else:
        pag.moveTo(window.left + window.width/2, window.top + window.height/2)
      kb.press(arrow)
      time.sleep(.78)
      kb.release(arrow)
      time.sleep(.01)

      # debuff skills
      pressAndRelease('7')
      pressAndRelease('r')
      time.sleep(.01)
      pressAndRelease('3')
      pressAndRelease('r')
      time.sleep(.01)
      pressAndRelease('6')
      pressAndRelease('r')

      pressAndRelease('2')
      pag.click(button='right')
      time.sleep(.01)

      pressAndRelease('5')
      pag.click(button='right')

      pressAndRelease('1')
      pag.click(button='right')

      # pressAndRelease('6')
      # pag.click(button='right')

      pressAndRelease('4')
      pag.click(button='right')
      time.sleep(.01)
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
      if k == 6:
        pressAndRelease('t')
      else:
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

    time.sleep(1.5)

    # 1~2번 랜덤으로 
    # 1: 50%
    # 2: 50%
    get_food()
    # random.seed(datetime.now().timestamp())
    # n = random.randint(1, 2)

    # keyboard.press('alt')
    # time.sleep(.05)
    # for i in range(1,n+1):
    #   keyboard.press('2')
    #   time.sleep(.2)
    #   keyboard.release('2')
    #   time.sleep(.2)
    #   if i == n:
    #     keyboard.release('alt')

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