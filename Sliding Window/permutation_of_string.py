from utils import log_output

class SlidingWindow:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        has_inclusion = False

        if n1 > n2:
            return log_output(has_inclusion)
        
        l = 0
        count1 = [0]*26
        count2 = [0]*26

        a = ord('a')
        
        for i in range(n1):
            count1[ord(s1[i]) - a] += 1
        
        for r in range(n2):
            count2[ord(s2[r]) - a] += 1
            if r - l + 1 > n1:
                count2[ord(s2[l]) - a] -= 1
                l += 1
            
            if count1 == count2:
                has_inclusion = True
                break
        
        return log_output(has_inclusion)
        

if __name__ == '__main__':
    
    sliding_window = SlidingWindow()

    s1 = "abc"
    s2 = "lecabee"
    sliding_window.checkInclusion(s1, s2)