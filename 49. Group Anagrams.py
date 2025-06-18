# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

#     "eat" --> [1,0,0,0,1,...,1,...] --> group 1
#     "tea" --> [1,0,0,0,1,...,1,...] --> group 1
#     "ate" --> [1,0,0,0,1,...,1,...] --> group 1
#     "tan" --> [1,0,0,0,0,0,0,...,1,1,0,0,...] --> group 2
#     "nat" --> [1,0,0,0,0,0,0,...,1,1,0,0,...] --> group 2
#     "bat" --> [1,1,0,0,0,0,0,...,1,...] --> group 3

# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = defaultdict(list)  # Create dictionary for anagram

        for s in strs:
            count = [0] * 26  # [000000000000....0000]
            for c in s:
                count[ord(c)-ord("a")] += 1  # [01000001000000]
            # res[01000001000000] ==> Key available then add "eat"
            res[tuple(count)].append(s)
        return list(res.values())  # convert from collection values to list


# Time: O(M*N)
# Space: O(N*K)
solution = Solution()

# Test Case 1
strr = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strr)
print(f"Group Anagram value of {strr} is {result} ")

# Test Case 2
strr = [""]
result = solution.groupAnagrams(strr)
print(f"Group Anagram value of {strr} is {result} ")

# Test Case 3

strr = ["a"]
result = solution.groupAnagrams(strr)
print(f"Group Anagram value of {strr} is {result} ")
