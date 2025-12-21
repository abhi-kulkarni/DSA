from typing import List
from shared.utils import log_output

class Stack:
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []
        for token in tokens:
            if token not in "+-*/":
                s.append(int(token))
            else:
                op1 = s.pop() # right
                op2 = s.pop() # left
                if token == "+":
                    s.append(op2+op1)
                elif token == "-":
                    s.append(op2-op1)
                elif token == "*":
                    s.append(op2*op1)
                elif token == "/":
                    s.append(int(op2/op1))

        return log_output(s[0])

if __name__ == '__main__':

    stack = Stack()

    tokens = ["1","2","+","3","*","4","-"]
    stack.evalRPN(tokens)

    