from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices), 1):
            p = prices[i]
            
            if p <= buy:
                buy = p
            elif (p - buy) > profit:
                profit = p - buy
        
        return profit
