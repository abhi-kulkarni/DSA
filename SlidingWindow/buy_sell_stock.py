from typing import List
from shared.utils import log_output

class SlidingWindow:

    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return log_output(0)
        
        n = len(prices)
        max_profit = 0
        min_price = float("inf")

        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        
        return log_output(max_profit)
        
if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    prices = [10,1,5,6,7,1]

    sliding_window.maxProfit(prices)
