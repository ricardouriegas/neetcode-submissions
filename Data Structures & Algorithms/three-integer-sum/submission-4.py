class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # move i to a non duplicate number
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                summatory = (nums[l] + nums[r] + nums[i])
                if summatory > 0:
                    r -= 1
                elif summatory < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    # move l to a non duplicate number
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # move r to a non duplicate number
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        
        return result
