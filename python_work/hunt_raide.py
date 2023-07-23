import keyboard
import time
import pyautogui as pag
import pygetwindow as gw

from pynput.keyboard import Key, Controller
kb = Controller()

def pressAndRelease(key):
    keyboard.press(key)
    time.sleep(0.02)
    keyboard.release(key)
    time.sleep(0.02)

# pyautogui의 keyboard press는 막힘
def on_key_press(event):
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

  # q(허영): 8r  3r  2-rc  5-rc  6-rc  4-rc  `
  elif event.name == 'q':
    pressAndRelease('8')
    pressAndRelease('r')
    pressAndRelease('3')
    pressAndRelease('r')

    pressAndRelease('2')
    pag.click(button='right') 
    time.sleep(0.01)

    pressAndRelease('5')
    pag.click(button='right') 
    time.sleep(0.01)

    pressAndRelease('6')
    pag.click(button='right') 
    time.sleep(0.01)

    pressAndRelease('4')
    pag.click(button='right') 
    time.sleep(0.01)
    pag.mouseUp(button='right')
    print('허영')

  # e(딜-예약시전): 6r LC[rrrr] 2r LC[rrr] 5r LC[rrrr] 4r LC[rrr] `
  elif event.name == 'e':
    pressAndRelease('6')
    pressAndRelease('r')
    keyboard.press('ctrl')
    time.sleep(0.01)
    pressAndRelease('r')
    pressAndRelease('r')
    keyboard.release('ctrl')
    time.sleep(0.01)

    pressAndRelease('2')
    pressAndRelease('r')
    keyboard.press('ctrl')
    time.sleep(0.01)
    pressAndRelease('r')
    pressAndRelease('r')
    keyboard.release('ctrl')
    time.sleep(0.01)

    pressAndRelease('5')
    pressAndRelease('r')
    keyboard.press('ctrl')
    time.sleep(0.01)
    pressAndRelease('r')
    pressAndRelease('r')
    keyboard.release('ctrl')
    time.sleep(0.01)

    pressAndRelease('4')
    pressAndRelease('r')
    keyboard.press('ctrl')
    time.sleep(0.01)
    pressAndRelease('r')
    pressAndRelease('r')
    keyboard.release('ctrl')
    time.sleep(0.01)

    print('예약시전')

  elif event.name == 'space':
    pressAndRelease('esc')
    pressAndRelease('esc')
    time.sleep(2)
    keyboard.press('alt')
    pressAndRelease('2')
    keyboard.release('alt')
  elif event.name == 'end':
    print('end key pressed')
  # elif event.name == 'esc':
  #   print('Esc key pressed')
  # elif event.name == 'ctrl':
  #   print('Ctrl key pressed')
  # elif event.name == 'alt':
  #   print('Alt key pressed')

game_window = gw.getWindowsWithTitle('Gersang')[0]
game_window.activate()
keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
# keyboard.add_hotkey('ctrl+c', quit)
# keyboard.wait(hotkey=None, suppress=False, trigger_on_release=False)
keyboard.wait('ctrl+c')

# res = pag.locateOnScreen("edit.png")
# print(res)