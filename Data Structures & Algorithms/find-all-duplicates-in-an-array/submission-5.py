class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # common way to do it:
        nums.sort()
        # result = []

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         result.append(nums[i])

        # return result

        # using the list as a pile
        i = 0
        
        while i < len(nums):
            tmp = nums.pop(i)
            if len(nums) == 0 or i == len(nums):
                return nums
            if tmp == nums[i]:
                i += 1

        return nums