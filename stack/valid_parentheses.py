from collections import deque


def is_open(br: str) -> bool:
    if br in ["(", "{", "["]:
        return True
    
    return False


def is_paired(top: str, br: str) -> bool:
    if (
        top == "(" and br == ")"
        or top == "{" and br == "}"
        or top == "[" and br == "]"
        ):
        return True
    
    return False


def isValid(s: str) -> bool:
    stack = deque()
    n: int = len(s)

    for i in range(n):
        if is_open(s[i]):
            stack.appendleft(s[i])
        else:
            if not len(stack):
                return False
            
            if is_paired(stack[0], s[i]):
                stack.popleft()

            else:
                return False
            
    if not len(stack):
        return True
    
    return False


class Solution:
    def __init__(self, s):
        self.s = s
        self.isValid()

    def is_open(self, br):
        if br in ["(", "{", "["]:
            return True
        
        return False


    def is_paired(self, top, br):
        if (
            top == "(" and br == ")"
            or top == "{" and br == "}"
            or top == "[" and br == "]"
            ):
            return True
        
        return False


    def isValid(self):
        stack = deque()
        n = len(self.s)

        for i in range(n):
            if self.is_open(self.s[i]):
                stack.appendleft(self.s[i])
            else:
                if not len(stack):
                    return False
                
                if self.is_paired(stack[0], self.s[i]):
                    stack.popleft()

                else:
                    return False
                
        if not len(stack):
            return True
        
        return False

