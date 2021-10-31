import random
from random import randint


def is_monotonic(nums):
    result = False
    increases = 0
    decreases = 0
    len_nums = len(nums)
    for i in range(len_nums - 1):
        if nums[i] > nums[i + 1]:
            decreases += 1
        elif nums[i] < nums[i + 1]:
            increases += 1

    if decreases == 0:
        result = True
    elif increases == 0:
        result = True

    return result


n = int(input())
nums = [randint(1, n) for i in range(n)]

#print(nums)
print(is_monotonic(nums))
