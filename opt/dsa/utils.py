import os
import numpy
from random import random, randrange, seed

def data(n = 10):
  arr = []
  for i in range(0, n):
    arr.append(randrange(-6, 61))
  # return numpy.random.randint(1000, size=(1, 2000))[0]
  return arr

def clear():
  os.system('clear')
