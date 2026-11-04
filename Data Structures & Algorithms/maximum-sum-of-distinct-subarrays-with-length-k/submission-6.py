class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # implement sliding window function
        max_value = 0
        bag = defaultdict(int)
        sumatory = 0

        left = 0
        for i in range(len(nums)):
            sumatory += nums[i]
            bag[nums[i]] += 1


            if i > k - 1:
                bag[nums[left]] -= 1
                if bag[nums[left]] == 0:
                    bag.pop(nums[left])
                sumatory -= nums[left]
                left += 1

            if len(bag) == k:
                max_value = max(max_value, sumatory)
            
        return max_value
