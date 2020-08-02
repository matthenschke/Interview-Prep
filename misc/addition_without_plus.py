
# NOTE: does not work when sum is 0, i.e 1, -1


def Add(x, y):

    # Iterate till there is no carry
    while y != 0:
        print(y)
        # carry now contains common
        # set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1

    return x


print(Add(1, -1))


# def add(a, b):

#     while (b != 0):
#         print(b)
#         carry = a & b
#         a = a ^ b
#         b = carry << 1

#     return a


# print(add(-1, 1))
