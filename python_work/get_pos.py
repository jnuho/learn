import keyboard
import mouse
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

def get_gersang_window():
  windows = gw.getWindowsWithTitle('Gersang')
  for w in windows:
    if w.title == 'Gersang':
      return w
    else:
      continue
  return None

# pyautogui의 keyboard press는 막힘
def on_right_click():
  window = get_gersang_window()
  print(f"Gersang window size: {window.width}, {window.height}")
  pos = mouse.get_position()
  x_diff = pos[0]-window.left
  x_pct = round(x_diff / window.width * 100, 2)
  y_diff = pos[1]-window.top
  y_pct = round(y_diff / window.height * 100, 2)
  print(f"position (%): {x_pct}, {y_pct}")
  # 쇠고기등심 58.35, 24.84

  # 채집종료/시작 20.49, 43.41
  # 확인 50.1, 56.84
  # 왼쪽창 아이템 3개
  #   20.0, 57.47
  #   24.17, 57.47
  #   28.45, 57.47
  # 인벤창 옮기는 클릭 57.96, 62.61
  #   전체 70.68, 72.9
  #   확인 70.49, 82.94
  # 오른쪽 삭제버튼 85.24, 68.26
  # 오른쪽 창 아이템 2개 삭제시 클릭
  #   66.8, 24.72
      #  전체 79.9, 34.76
      #  확인 80.39, 44.29
  #   70.97, 24.72
  #     전체 84.17, 34.25
  #     확인 84.27, 44.04
  # 삭제하시겠습니까? 56.31, 56.21



  # pos = pag.position()
  # pag.screenshot('python_work/2.png', region=(game_window.left, game_window.top, game_window.width, game_window.height))

def on_click():
  print(mouse.get_position())
  # keyboard.press('ctrl+c')

mouse.on_right_click(on_right_click)

mouse.on_click(on_click)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')
