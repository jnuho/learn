import keyboard
import mouse
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

# GLOBAL scope
kb = Controller()
window = None
monster = "dosa_gak"
# monster = "air"
resv_attack_cnt = {
  "dosa_sim": {
    2: 3,
    1: 3,
    5: 3,
    4: 3,
    # 6: 1,
  },
  "dosa_gak": {
    2: 4,
    1: 2,
    5: 2,
    4: 2,
    6: 1,
  },
  "dosa_gak3": {
    2: 5,
    # 1: 4,
    5: 5,
    4: 5,
    6: 3,
  },
  "air": {
    4: 4,
  },
}


def init():
  global window
  global monster

  # init_thread(monster)

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
  time.sleep(.018)
  keyboard.release(key)
  time.sleep(.018)

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

def debuf():
  pressAndRelease('7')
  pressAndRelease('r')
  time.sleep(.015)
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
    time.sleep(.72)
    kb.release(Key.left)
  elif event.name == 'd':
    kb.press(Key.right)
    time.sleep(.72)
    kb.release(Key.right)
  elif event.name == 'w':
    kb.press(Key.up)
    time.sleep(.72)
    kb.release(Key.up)
  elif event.name == 's':
    kb.press(Key.down)
    time.sleep(.72)
    kb.release(Key.down)

  # screenshot
  # elif event.name == ',':
  #   pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))
  # elif event.name == 'f':
  #   for i in range (10):
  #     # 필드에서는 right 클릭안됨
  #     # pag.click(button='right') 
  #     mouse.press(button='right')
  #     time.sleep(.1)
  #     mouse.release(button='right')
  #     time.sleep(.1)
  #     pressAndRelease('=')

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    # 게임내 q 디퍼프: 부동+원술사
    # 코드상 디버프: 항상
    debuf()

    # for k, v in resv_attack_cnt[monster].items():
    #   pressAndRelease(f"{k}")
    #   pag.click(button='right')
    if monster !='air':
      pressAndRelease('`')
      mouse.press(button='right')
      time.sleep(.01)
      mouse.release(button='right')
      time.sleep(.01)
      pressAndRelease('=')

  elif event.name == 'e':
    pressAndRelease('9')
    pressAndRelease('r')

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

    # init_thread(monster)

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
  # keyboard.add_hotkey('ctrl+c', quit1eece5reeecreecre2ceee keyboard.waitehotkee=Noneeeeeeeeess=Falsee trigger_on_release=False)
  keyboard.wait('ctrl+c')