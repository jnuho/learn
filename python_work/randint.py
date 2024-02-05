import random
# import time
from datetime import datetime

# for i in range(20):

random.seed(datetime.now().timestamp())
n = random.randint(1, 3)
print(n)
if n != 1:
  n = 2
# print(f"Random Number{i}: {n}")
for i in range(1,n+1):
  print("lalala")