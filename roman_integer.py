def romanToInt(self, s: str) -> int:
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = float('-inf')
    for letter in s:
        cur_val = table[letter]
        if cur_val > prev and prev != float('-inf'):
            num += (cur_val - prev) - prev
        else:
            num += cur_val
        prev = cur_val
    return num
