class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # common way to do it:
        # nums.sort()
        # result = []

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         result.append(nums[i])

        # return result

        # using the list as a pile (saves storage but is trash in runtime)
        # i = 0
        
        # while i < len(nums):
        #     tmp = nums.pop(i)
        #     if len(nums) == 0 or i == len(nums):
        #         return nums
        #     if tmp == nums[i]:
        #         i += 1

        # return nums

        # without sorting
        result = []

        for i in nums:
            i = abs(i)
            if nums[i-1] < 0:
                result.append(i)
                continue

            nums[i-1] = -nums[i-1]

        return result
