from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def __repr__(self) -> str:
        return str(self.container)

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def isempty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def reverse(self):
        return list(self.container)[::-1]    
    
class balanceParanthesis(Stack):
    def __init__(self, expression) -> bool:
        super().__init__()
        self.expression = expression

    def balancedParanthesis(self):
        mapping = {'{':'}',
                   '[':']',
                   '(':')'}
        
        for char in self.expression:
            if char in mapping.keys():
                self.push(char)

            elif char in mapping.values():
                if not self.container:
                    return False
                
                opening_value = self.pop()
                if mapping[opening_value] != char:
                    return False
                
        return len(self.container) == 0

if __name__ == "__main__":
    stack = balanceParanthesis("{[()]}")
    print(stack.balancedParanthesis())
