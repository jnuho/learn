import pyautogui as pag

a =pag.position()
pag.screenshot('python_work/1.png', region=(400,100, 1200, 1000))
# button7location = pag.locateCenterOnScreen('python_work/1.png', confidence=0.9, grayscale=True)
# print(button7location)

# button7location = pag.locateCenterOnScreen('python_work/dosa_sim_6.png', confidence=0.9, grayscale=True)
# print(button7location)


# https://pyautogui.readthedocs.io/en/latest/screenshot.html#grayscale-matching
try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_3.png', confidence=0.93)
  print(f"3 : {button7location}")
except pag.ImageNotFoundException:
  print("3 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_3_2.png', confidence=0.93)
  print(f"3_2 : {button7location}")
except pag.ImageNotFoundException:
  print("3_2 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_6.png', confidence=0.93)
  print(f"6 : {button7location}")
except pag.ImageNotFoundException:
  print("6 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_6_2.png', confidence=0.93)
  print(f"6_2 : {button7location}")
except pag.ImageNotFoundException:
  print("6_2 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_6_3.png', confidence=0.93)
  print(f"6_3 : {button7location}")
except pag.ImageNotFoundException:
  print("6_3 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_9.png', confidence=0.93)
  print(f"9 : {button7location}")
except pag.ImageNotFoundException:
  print("9 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_9_2.png', confidence=0.93)
  print(f"9_2 : {button7location}")
except pag.ImageNotFoundException:
  print("9_2 None")
  button7location=None

try:
  button7location = pag.locateCenterOnScreen('python_work/dosa_sim_12.png', confidence=0.93)
  print(f"12 : {button7location}")
except pag.ImageNotFoundException:
  print("12 None")
  button7location=None