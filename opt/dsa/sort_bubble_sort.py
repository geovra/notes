import math
from utils import data, clear

clear()

# Bubble sort with two opposite pointers
def bubbleSortShrinkingInterval(arr):
  sorted = 0
  maxim, maximFound = -math.inf, 0
  lft, rgt = 0, len(arr) - 1
  i, j, k = lft, rgt, 0
  
  check = 1
  while not sorted or not maximFound and lft <= rgt:
    if (i + 1 < rgt) and (arr[i] > arr[i + 1]):
      arr[i], arr[i + 1] = arr[i + 1], arr[i]
      check = 0
    i += 1
    
    if j - 1 > lft and arr[j - 1] > arr[j]:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      check = 0
    j -= 1
    
    if i == rgt and j == lft:
      lft += 1
      rgt -= 1
      maxim = max(maxim, arr[i])
      maximFound = 1
      sorted = 1 if check else 0
      check = 1
      i, j = j, i
      k += 1

  print(k, arr)

# bubbleSortShrinkingInterval([1, 18, 2, 27, 33, 3, 66, -1, 15 ])
bubbleSortShrinkingInterval(data()) # 247 loops for 1K items, 2534 loops for 10K items

# Bubble sort with two opposite pointers
def bubbleSortOppositePointers(arr):
  i, j, k = 0, len(arr) - 1, 0
  sorted = 0
  maxim, maximFound = -math.inf, 0
  
  check = 1
  while not sorted or not maximFound:
    if (i + 1 < len(arr)) and (arr[i] > arr[i + 1]):
      arr[i], arr[i + 1] = arr[i + 1], arr[i]
      check = 0
    i += 1
    
    if j - 1 > 0 and arr[j - 1] > arr[j]:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      check = 0
    j -= 1
    
    if i == len(arr) - 1 and j == 0:
      maxim = max(maxim, arr[i])
      maximFound = 1
      sorted = 1 if check else 0
      check = 1
      i, j = j, i
      
      k += 1

  print(k, arr)

# bubbleSortOppositePointers([1, 18, 2, 27, 33, 3, 66, -1, 15 ])
bubbleSortOppositePointers(data()) # 247 loops for 1K items, 2534 loops for 10K items
