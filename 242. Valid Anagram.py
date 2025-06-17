from typing import Counter


class Solution(object):
    def isAnagram(self, s, t):

        # Solution 1
        # Time Complexity: O(N)
        # Space Complexity: O(1) (for fixed alphabet), O(K) otherwise
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

        # Solution 2 T: O(S+T) and S: O(S+T)
        # Time Complexity: O(S + T), where S and T are the lengths of s and t.
        # Space Complexity: O(S + T), for storing the character counts.
        # return Counter(s) == Counter(t)

        # Solution 3 T: O(N log N), S: O(N)
        # Time Complexity: O(N log N), where N is the length of the strings (since sorting takes O(N log N)).
        # Space Complexity: O(N), due to the space required to store the sorted strings.
        # return sorted(s) == sorted(t)


solution = Solution()

s = "anagram"
t = "nagaram"
result = solution.isAnagram(s, t)
print(f"Is {s} & {t} Anagram: {result}")

s = "rat"
t = "car"
result = solution.isAnagram(s, t)
print(f"Is {s} & {t} Anagram: {result}")

s = "a"
t = "ab"
result = solution.isAnagram(s, t)
print(f"Is {s} & {t} Anagram: {result}")
