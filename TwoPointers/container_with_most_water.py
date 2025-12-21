from typing import List
from shared.utils import log_output

class TwoPointers:

    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        l = 0
        r = n-1

        max_a = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])

            max_a = max(max_a, w*h)

            if heights[l] < heights[r]:
                l +=1 
            else:
                r -= 1
        
        return log_output(max_a)
    
if __name__ == '__main__':
    
    two_pointers = TwoPointers()

    heights = [2,2,2]
    two_pointers.maxArea(heights)