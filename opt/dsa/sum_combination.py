from audioop import add
from utils import clear 
clear()

def fn(arr, k):
  res = []
  if not arr or len(arr) == 0:
    return print(res)

  sorted(arr)
  combination = []
  findSumOfCombinations(arr, res, combination, 0, k)
  
  print(res)

def findSumOfCombinations(arr, res, row, index, sum): # How about permutations that sum up to k
  if sum == 0:
    res.append(row[:])
    return

  for i in range(index, len(arr)):
    if i != index and arr[i] == arr[i-1]:
      continue
    if (arr[i] > sum):
      break

    row.append(arr[i])
    findSumOfCombinations(arr, res, row, i + 1, sum - arr[i])
    row.pop()

fn([1, -1, 3, 7, 2, 35, 9], 10)
