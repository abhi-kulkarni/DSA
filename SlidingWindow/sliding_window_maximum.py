from collections import deque
from typing import List
from utils import log_output

class SlidingWindow:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        n = len(nums)
        res = []

        for i in range(n):

            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return log_output(res)
        

if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    nums = [1,2,1,0,4,2,6]
    k = 3

    sliding_window.maxSlidingWindow(nums, k)
