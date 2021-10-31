import random
from random import randint

def find_missing_nums(nums):
  norm = [d for d in range(1, len(nums)+1)]
  a = []
  for h in norm:
    if h not in nums:
      a.append(h)
  return a

n = int(input())
nums = [randint(1, n) for i in range(n)]

print(find_missing_nums(nums))