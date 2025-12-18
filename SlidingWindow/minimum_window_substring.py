from collections import Counter
from utils import log_output

class SlidingWindow:

    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return log_output("")
        
        have = {}
        need = Counter(t)

        formed = 0
        required = len(need)
        
        l = 0
        n = len(s)

        res = float("inf"), 0, 0

        for r in range(n):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1
            
            while formed == required:

                if r - l + 1 < res[0]:
                    res = r - l + 1, l, r
                
                have[s[l]] -= 1

                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                
                l += 1
        
        if res[0] != float("inf"):
            return log_output(s[res[1]: res[2]+1])
        
        return log_output("")
        

if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    s = "OUZODYXAZV"
    t = "XYZ"
    sliding_window.minWindow(s, t)
