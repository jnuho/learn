import pyautogui as pag
import pygetwindow as gw

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
# init()

def work():
  image_path = f"python_work/3.png"
  try:
    pos_found = pag.locateCenterOnScreen(image_path, confidence=.93, grayscale=True)
    print(f"found at ({pos_found.x},{pos_found.y}).")
    # result.append(arrows[dir//3 - 1])
    return
  except pag.ImageNotFoundException:
    # print(f"{dir}_{idx} None")
    print("ERROR")
    return

work()