
def intToRomanConv(num):
    vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    syms = ['I', 'IV', 'V', 'IX', 'X', 'XL',
            'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'
            ]
    i = 12
    while num:
        q = num // vals[i]
        print(syms[i] * q, end="")
        num %= vals[i]
        i -= 1


intToRomanConv(101)
