from typing import List
from shared.utils import log_output

class Stack:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        s = []
        res = [0] * n
        for i in range(n):
            while s and temperatures[i] > temperatures[s[-1]]:
                idx = s.pop()
                res[idx] = i - idx
            s.append(i)
        
        return log_output(res)

if __name__ == '__main__':

    stack = Stack()

    temperatures = [30,38,30,36,35,40,28]
    stack.dailyTemperatures(temperatures)