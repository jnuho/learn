import random
import keyboard
import time
from datetime import datetime
import pyautogui as pag
import pygetwindow as gw

resv_attack_cnt = {
  "dosa_sim": {
    6: 0
    , 1: 3
    , 5: 4
    , 2: 4
    , 4: 3
  },
  "dosa_gak": {
    6: 0
    , 1: 4
    , 5: 5
    , 2: 5
    , 4: 4
  },
  "baek": {
    6: 0
    , 1: 1
    , 5: 2
    , 2: 2
    , 4: 1
  },
}
monster = "baek"

# if monster =="baek":
#   resv_attack_cnt[monster][]
for k, v in resv_attack_cnt[monster].items():
  print(f"{k},{v}")
  if k == 4:
    print(f"6, 999")


for _ in range(3):
  print('dsds')