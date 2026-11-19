class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        minimun_difference = 0
        for i in range(1, len(prices)):
            if prices[left] > prices[i]:
                left = i
            elif prices[left] < prices[i]:
               minimun_difference = max(minimun_difference, prices[i] - prices[left]) 
            else:
                left = i
        
        return minimun_difference
