# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/


def removeDuplicates(self, S: str) -> str:
    stack = []

    for char in S:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)
