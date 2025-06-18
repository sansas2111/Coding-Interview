# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Step 1: Count frequencies

# [1, 1, 1, 2, 2, 3]
#    |
#    v
# {1:3, 2:2, 3:1}

# Step 2: Heapify (min-heap of size k=2)
# Push (3, 1) -> Heap: [(3, 1)]
# Push (2, 2) -> Heap: [(2, 2), (3, 1)]
# Push (1, 3) -> Heap: [(1, 3), (3, 1), (2, 2)]
#   Heap size > 2 -> Pop (1, 3) -> Heap: [(2, 2), (3, 1)]

# Step 3: Pop k elements from heap
# Pop (2, 2) -> res = [2]
# Pop (3, 1) -> res = [2, 1]

# Return [2, 1]

import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}  # create dictionary

        for num in nums:
            # Capture the frquency nums {1: 3, 2: 2, 3: 1}
            count[num] = 1 + count.get(num, 0)

        heap = []

        for num in count.keys():
            # Add heap data structure like 	[(1, 3), (3, 1), (2, 2)]
            heapq.heappush(heap, (count[num], num))
            # Heap size > 2, pop	[(2, 2), (3, 1)] (removes (1, 3))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            # Heap Before Pop	Popped	Result List [(2, 2), (3, 1)] ==> 	[2, 1]
            res.append(heapq.heappop(heap)[1])

        return res
