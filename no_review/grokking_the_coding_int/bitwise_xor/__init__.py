'''
Following are some important properties of XOR to remember:

Taking XOR of a number with itself returns 0, e.g.,

1 ^ 1 = 0
29 ^ 29 = 0
Taking XOR of a number with 0 returns the same number, e.g.,

1 ^ 0 = 1
31 ^ 0 = 31
XOR is Associative & Commutative, which means:

(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
'''


def find_missing_number(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n - 1):
        x2 = x2 ^ arr[i]

    # missing number is the xor of x1 and x2
    return x1 ^ x2


# print('Missing number is: ' + str(find_missing_number([1, 5, 2, 6, 4])))


# Single Number (easy)
def find_single_number(arr):
    num = 0
    for n in arr:
        num ^= n

    return num


# print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
# print(find_single_number([7, 9, 7]))


# Two Single Numbers (medium)
def find_single_numbers(nums):
    n1xn2 = 0
    bit_0_group = []
    bit_1_group = []
    num1, num2 = 0, 0

    for n in nums:
        n1xn2 ^= n

    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    for n in nums:
        if n & rightmost_set_bit:
            bit_1_group.append(n)
        else:
            bit_0_group.append(n)

    for x in bit_1_group:
        num1 ^= x

    for x in bit_0_group:
        num2 ^= x

    return [num1, num2]


# print('Single numbers are:' +
#       str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
# print('Single numbers are: ' + str(find_single_numbers([2, 1, 3, 2])))


# Complement of Base 10 Number (medium)
def calculate_bitwise_complement(num):
    # count number of total bits in 'num'
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1
    # for a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
    # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
    # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
    # representation of '11' i.e., it has '2' least significant bits set to '1'
    all_bits_set = pow(2, bit_count) - 1

    # from the solution description: complement = number ^ all_bits_set
    return num ^ all_bits_set


# print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
# print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

# Problem Challenge 1 (hard)
def flip_and_invert_image(matrix):
    for row in matrix:
        start, end = 0, len(row) - 1
        while start < end:
            row[start], row[end] = row[end], row[start]
            start += 1
            end -= 1

        for i in range(len(row)):
            row[i] ^= 1

    return matrix


# print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
# print(flip_and_invert_image(
#     [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
