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
    "dosa_gak": {
        2: 3,
        1: 0,
        5: 3,
        4: 3,
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
        # w.activate()
        window = w
        # pag.screenshot('images/1.png', region=(window.left, window.top, window.width, window.height))

def pressAndRelease(key):

    keyboard.press(key)
    time.sleep(.018)
    keyboard.release(key)
    time.sleep(.018)

def get_food():
    food_image = "images/food1.png"
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
    print(event.name)

    if event.name == 'a':
        pass
        # kb.press(Key.left)
        # time.sleep(.72)
        # kb.release(Key.left)
    elif event.name == 'x':
        pass
        # keyboard.press('esc')
        # time.sleep(.1)
        # keyboard.release('esc')
        # time.sleep(.1)
        # keyboard.press('esc')
        # time.sleep(.1)
        # keyboard.release('esc')AA

if __name__ == "__main__":
    init()

    keyboard.on_press(on_key_press)
    # Keep the program running until you press the Esc key
    # keyboard.add_hotkey('ctrl+c', quit1eece5reeecreecre2ceee keyboard.waitehotkee=Noneeeeeeeeess=Falsee trigger_on_release=False)
    keyboard.wait('ctrl+c')