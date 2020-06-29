# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


def lengthOfLongestSubstring(self, s: str) -> int:
    table = {}
    length = 0
    j = 0
    for i in range(len(s)):
        char = s[i]
        if char in table:
            j = max(j, table[char])
        length = max(length, i - j + 1)
        table[char] = i + 1

    return length
