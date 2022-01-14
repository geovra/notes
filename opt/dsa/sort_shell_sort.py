import math
from utils import data, clear
clear()

def fn(arr):
  gap = math.floor(len(arr) / 2)

  while gap >= 1:
    for i in range(len(arr) - gap):
      if (arr[i] > arr[i + gap]):
        arr[i], arr[i + gap] = arr[i + gap], arr[i]
    gap -= 1

  print(arr)

fn([1, -1, 9, 4, 2, 7, -2, 5, 6])

