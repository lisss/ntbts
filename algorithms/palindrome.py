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


class Solution:
    # https://leetcode.com/problems/valid-palindrome/
    def isPalindrome(self, s: str):
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True

    # https://leetcode.com/problems/valid-palindrome-ii/

    def check_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def validPalindrome(self, s: str):
        start, end = 0, len(s) - 1
        allowed_to_delete = True

        while start < end:
            ch_start, ch_end = s[start], s[end]
            if ch_start != ch_end:
                if allowed_to_delete:
                    allowed_to_delete = False
                    return self.check_palindrome(s, start + 1, end) \
                        or self.check_palindrome(s, start, end - 1)
                else:
                    return False
            start += 1
            end -= 1

        return True
