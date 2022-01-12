import os
import math
os.system('clear')

def fn(arr, k):
  table = {}
  for i, v in enumerate(arr):
    diff = k - v
    if table.get(diff) != None:
      return print(table[diff], i)
    table[v] = i    
  print('N/A')

fn([1, -1, 3, 8, 5, 9, 2], 9)
