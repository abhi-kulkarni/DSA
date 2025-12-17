from typing import List

class DSA:

    def trap(self, height: List[int]) -> int:

        max_a = 0
        s = []
        n = len(height)

        for i in range(n):
            while s and height[i] > height[s[-1]]:
                idx = s.pop()
                if not s:
                    break
                w = i - s[-1] - 1
                h = min(height[i], height[s[-1]]) - height[idx]
                max_a += (w * h)

            s.append(i)

        print(max_a)

        return max_a

    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        l = 0
        r = n-1

        max_a = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])

            max_a = max(max_a, w*h)

            if height[l] < height[r]:
                l +=1 
            else:
                r -= 1
        
        print(max_a)

        return max_a
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        n = len(s)
        m = {}
        l = 0
        
        for r in range(n):
            if s[r] in m and m[s[r]] >= l:
                l = m[s[r]] + 1
            
            m[s[r]] = r

            max_len = max(max_len, r-l+1)
        
        print(max_len)

        return max_len


if __name__ == '__main__':
    dsa = DSA()
    height = [0,2,0,3,1,0,1,3,2,1]
    dsa.trap(height)

    heights = [2,2,2]
    dsa.maxArea(heights)

    s = "zxyzxyz"
    dsa.lengthOfLongestSubstring(s)