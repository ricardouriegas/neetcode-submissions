class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        difference = 0
        for i in range(1, len(prices)):
            if prices[left] < prices[i]:
               difference = max(difference, prices[i] - prices[left]) 
            else:
                left = i
        
        return difference
