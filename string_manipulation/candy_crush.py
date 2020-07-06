
def candyCrush(s):
    stack = []
    i = 0
    while i < len(s):
        if stack and stack[-1] == s[i]:
            char = stack.pop()
            while i < len(s) and s[i] == char:
                i += 1
        else:
            stack.append(s[i])
            i += 1

    return "".join(stack)


if __name__ == "__main__":
    print(candyCrush("abbbbbeaacd"))  # aecd
    print(candyCrush('aaaaabbaaaaaaaaa'))  # ''
    print(candyCrush("aaaabbacbb"))
