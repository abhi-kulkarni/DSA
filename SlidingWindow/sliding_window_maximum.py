from collections import deque
from typing import List
from shared.utils import log_output

class SlidingWindow:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        d = deque()
        n = len(nums)

        res = []

        for i in range(n):

            while d and d[0] <= i - k:
                d.popleft()
            
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            
            d.append(i)

            if i >= k-1:
                res.append(nums[d[0]])
        
        return log_output(res)
        

if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    nums = [1,2,1,0,4,2,6]
    k = 3

    sliding_window.maxSlidingWindow(nums, k)
