# Given an array of integers nums and an integer target,
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j
# that satisfy the condition.

class Solution(object):
    def twosumusinghashmap(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            # print(f"i&n: {i, n}")
            diff = target - n
            # print(f"diff: {diff}")
            if diff in prevMap:
                # print(f"[prevMap[diff], i]: {[prevMap[diff], i]}")
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
                # print(f"n, i: {n, i}")

    # Only for Sorted Array

    def twosumusingtwopointer(self, nums, target):
        left = 0
        right = len(nums)-1
        sum = 0
        sortednums = sorted(nums)
        while (left < right):
            sum = sortednums[left] + sortednums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twosumusinghashmap(nums, target)
print(f"result of twosumusinghashmap={nums} & target={target}; is {result}")

result = solution.twosumusingtwopointer(nums, target)
print(f"result of twosumusingtwopointer={nums} & target={target}; is {result}")


nums = [3, 2, 4]
target = 6
result = solution.twosumusinghashmap(nums, target)
print(f"result of twosumusinghashmap={nums} & target={target}; is {result}")
