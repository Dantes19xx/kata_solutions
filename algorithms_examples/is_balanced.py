from collections import deque


def is_open(br: str) -> bool:
    if br in ["(", "{", "["]:
        return True
    
    return False


def is_pair(top: str, br: str) -> bool:
    if (
        top == "(" and br == ")"
        or top == "{" and br == "}"
        or top == "[" and br == "]"
    ):
        return True
    
    return False


def is_balanced(s: str) -> bool:
    # ()({[]}())

    n: int = len(s)
    stack: deque[str] = deque()

    for i in range(n):
        if is_open(s[i]):
            stack.appendleft(s[i])
        else:
            if not len(stack) :
                return False
            
            if is_pair(stack[0], s[i]):
                stack.popleft()
            else:
                return False
    
    if not len(stack):
        return True
    
    return False
            



is_balanced("()]({[]}())")