# https: // leetcode.com/problems/first-unique-character-in-a-string/solution/


def firstUniqChar(self, s: str) -> int:
    table = {}
    for char in s:
        if char not in table.keys():
            table[char] = 1
        else:
            table[char] += 1

    for i in range(len(s)):
        if table[s[i]] == 1:
            return i
    return -1
