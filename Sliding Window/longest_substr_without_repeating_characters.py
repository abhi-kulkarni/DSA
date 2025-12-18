from utils import log_output
class SlidingWindow:

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
        
        return log_output(max_len)


if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    s = "zxyzxyz"
    sliding_window.lengthOfLongestSubstring(s)