# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str):
        freq_map = {}
        window_start, matched_count, start = 0, 0, 0
        min_length = len(s) + 1

        for x in t:
            if x not in freq_map:
                freq_map[x] = 0
            freq_map[x] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]

            if right_char in freq_map:
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched_count += 1

            while matched_count == len(freq_map):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    start = window_start

                left_char = s[window_start]
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched_count -= 1
                    freq_map[left_char] += 1

                window_start += 1

        if min_length > len(s):
            return ''

        return s[start:start + min_length]
