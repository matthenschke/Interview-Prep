

def permutations(s):
    def helper(s, cur, used):
        if len(s) == len(cur):
            print(cur[::])
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                helper(s, cur + s[i], used)
                used[i] = False
    cur = ""
    used = [False] * len(s)
    helper(s, cur, used)
