# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str):
        freq_map = {}
        window_start, matched_count = 0, 0
        res = []

        for x in p:
            if x not in freq_map:
                freq_map[x] = 0
            freq_map[x] += 1

        for window_end in range(len(s)):
            right_char = s[window_end]

            if right_char in freq_map:
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched_count += 1

            if matched_count == len(freq_map):
                res.append(window_start)

            if window_end >= len(p) - 1:
                left_char = s[window_start]
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched_count -= 1
                    freq_map[left_char] += 1
                window_start += 1

        return res
