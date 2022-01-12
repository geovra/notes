import os
import math
os.system('clear')

# The count of palindromic substrings
def fn(s):
  res = 0
  
  for i in range(len(s)):
    def check(L, R):
      res = 0
      while L >= 0 and R < len(s) and s[L] == s[R]:
        res += 1 if L != R else 0 
        L -= 1
        R += 1
      return res

    res += check(i, i) # ... To find palindromes of odd length: aba, abbba
    res += check(i, i + 1) # ... To find palindromes of even length: aa, aabbaa

  print(res)
  
fn("1_aaBBaa_7")
