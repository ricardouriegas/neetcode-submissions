class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        bag = set(nums)
        result, count = 0, 0

        for i in nums:
            if i - 1 in bag:
                continue
            else:
                while i in bag:
                    i += 1
                    count += 1

                result = max(result, count)
                count = 0

        return result
