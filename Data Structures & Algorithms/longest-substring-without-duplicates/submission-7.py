class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        bag = set()

        for r in range(len(s)):
            while s[r] in bag:
                bag.remove(s[l])
                l += 1
            bag.add(s[r])
            result = max(result, r - l + 1)
        
        return result