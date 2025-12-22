from typing import List
from shared.utils import log_output

class Stack:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        prev_time = 0
        fleets = 0

        cars = sorted(zip(position, speed) ,reverse=True)

        for pos, speed in cars:
            time = (target - pos) / speed
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return log_output(fleets)

        

if __name__ == '__main__':

    stack = Stack()

    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]

    stack.carFleet(target, position, speed)