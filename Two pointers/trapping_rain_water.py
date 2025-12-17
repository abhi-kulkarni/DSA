from typing import List

class TwoPointers:

    def trap(self, heights: List[int]) -> int:

        max_a = 0
        s = []
        n = len(heights)

        for i in range(n):
            while s and heights[i] > heights[s[-1]]:
                idx = s.pop()
                if not s:
                    break
                w = i - s[-1] - 1
                h = min(heights[i], heights[s[-1]]) - heights[idx]
                max_a += (w * h)

            s.append(i)

        print(max_a)

        return max_a
    
if __name__ == '__main__':
    
    two_pointers = TwoPointers()
    
    heights = [0,2,0,3,1,0,1,3,2,1]
    two_pointers.trap(heights)