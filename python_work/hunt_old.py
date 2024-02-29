import keyboard
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller

from threading import Thread

# GLOBAL scope
kb = Controller()
resv_attack_cnt = {
  "dosa_sim": {
    1: 3,
    5: 3,
    2: 3,
    4: 3,
    # 6: 1,
  },
  "dosa_gak": {
    1: 4,
    5: 5,
    2: 5,
    4: 4,
    6: 1,
  },
  "baek": {
    1: 0,
    5: 0,
    2: 0,
    4: 1,
    6: 2,
  },
}
monster = "dosa_gak"


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

# at program start
init()

def pressAndRelease(key):
  keyboard.press(key)
  time.sleep(0.0185)
  keyboard.release(key)
  time.sleep(0.0185)

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
  # debuff skills
  pressAndRelease('7')
  pressAndRelease('r')
  # time.sleep(.01)
  pressAndRelease('3')
  pressAndRelease('r')
  # time.sleep(.01)
  pressAndRelease('6')
  pressAndRelease('r')
  # time.sleep(.01)

  pressAndRelease('5')
  pag.click(button='right')

  pressAndRelease('2')
  pag.click(button='right')

  pressAndRelease('1')
  pag.click(button='right')

  # pressAndRelease('6')
  # pag.click(button='right')

  pressAndRelease('4')
  pag.click(button='right')

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
  global window
  global monster
  global resv_attack_cnt

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
  # elif event.name == ',':
  #   pag.screenshot('python_work/1.png', region=(window.left, window.top, window.width, window.height))

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    debuf()

  elif event.name == 'e':
    pressAndRelease('9')
    pressAndRelease('r')

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

    # init_thread(monster)

    time.sleep(1.7)

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