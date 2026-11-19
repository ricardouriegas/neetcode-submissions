class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        difference = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
               difference = max(difference, prices[right] - prices[left]) 
            else:
                left = right
        
        return difference
