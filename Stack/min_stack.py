from shared.utils import log_output

class Stack:

    def __init__(self):
        self.s1 = []
        self.ms1 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.ms1:
            self.ms1.append(val)
        else:
            min_ele = min(val, self.ms1[-1])
            self.ms1.append(min_ele)

    def pop(self) -> None:
        self.s1.pop()
        self.ms1.pop()

    def top(self) -> int:
        return log_output(self.s1[-1])

    def getMin(self) -> int:
        return log_output(self.ms1[-1])

if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(0)
    stack.getMin()
    stack.pop()
    stack.top()  
    stack.getMin()