import random
import time
from datetime import datetime

import pyautogui as pag

for i in range(20):
  random.seed(datetime.now().timestamp())
  time.sleep(1)
  n = random.randint(1, 100)
  print(f"Random Number{i}: {n}")