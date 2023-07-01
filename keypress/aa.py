#import keyboard
import pyautogui as pag

#def on_key_press(event):
  #if event.name == 'esc':
    #print('Esc key pressed')
  #elif event.name == 'ctrl':
    #print('Ctrl key pressed')
  #elif event.name == 'alt':
    #print('Alt key pressed')

#keyboard.on_press(on_key_press)

# Keep the program running until you press the Esc key
#keyboard.wait('esc')


res = pag.locateOnScreen("edit.png")
print(res)
