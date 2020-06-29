# https://leetcode.com/problems/valid-parentheses/submissions/


def isValid(self, s: str) -> bool:

    table = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in table:
            top = stack.pop() if stack else None
            if table[char] != top:
                return False

        else:
            stack.append(char)

    return not stack
