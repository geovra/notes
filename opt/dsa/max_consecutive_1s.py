import os
import math
os.system('clear')

# The max number of consecutive 1s
def fn(arr):
  maxim = -math.inf # ... The max number of consecutive 1s
  count = 0 # ... The window running count
  
  for i, n in enumerate(arr):
    if n == 1:
      count += 1
    else:
      count = 0
    maxim = max(maxim, count)
    
    # count = count + 1 if n == 1 else 0
    # maxim = max(maxim, count)
  print(maxim)
  
fn([1, 1, 0, 1, 1, 1, 1, 1, 0])
