import random
import time
from datetime import datetime

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
}

count = 0
for key, val in resv_attack_cnt["dosa_gak"].items():
  count = 0
  # print(key,val)
  for _ in range(val):
    count=count+1
  print(f"{key}: {count}")
  # for idx in val:
  #   print(idx)
