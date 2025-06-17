class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()  # Hash set: For storing the unique elements
        for i in range(0, len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False


solution = Solution()

# Test Case 1
nums = [1, 2, 3, 1]
result = solution.containsDuplicate(nums)
print(f"Result of {nums} is {result}")

# Test Case 2
nums = [1, 2, 3, 4]
result = solution.containsDuplicate(nums)
print(f"Result of {nums} is {result}")
