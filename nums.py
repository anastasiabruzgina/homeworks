from random import randint

n = int(input())
nums = [randint(1, n) for i in range(1, n + 1)]
def is_here(i):
    return i not in nums
def find_missing_nums(nums):
    normal_array = [i for i in range(1, n + 1)]
    a = list(filter(is_here, normal_array))
    return a
