def is_num_palindrome(num: int):
    binary = []
    is_converted = False

    while not is_converted:
        num, rem = divmod(num, 2)
        binary.append(rem)
        if num == 0:
            is_converted = True

    start, end = 0, len(binary) - 1

    while start < end:
        if binary[start] != binary[end]:
            return False
        start += 1
        end -= 1
    return True
