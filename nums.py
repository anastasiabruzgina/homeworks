from random import randint

n = int(input())
nums = [randint(1, n) for i in range(1, n + 1)]
def find_missing_nums(nums):
    normal_array = [i for i in range(1, n + 1)]
    a = list(filter(lambda i: i not in nums, normal_array))
    return aa
