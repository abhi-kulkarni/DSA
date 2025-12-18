from utils import log_output

class SlidingWindow:

    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        l = 0
        max_len = 0
        m = {}
        max_fc = 0
        
        for r in range(n):
            m[s[r]] = m.get(s[r], 0) + 1
            max_fc = max(max_fc, m[s[r]])

            while (r - l + 1) - max_fc > k:
                m[s[l]] -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return log_output(max_len)
        
if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    s = "XYYX"
    k = 2
    sliding_window.characterReplacement(s, k)
