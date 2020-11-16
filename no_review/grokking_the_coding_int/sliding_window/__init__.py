import math


def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit
        # the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result

# 1 (easy)


def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        if windowEnd >= k - 1:
            max_sum = max(windowSum, max_sum)
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return max_sum

# 2 (easy)


def smallest_subarray_with_given_sum(s, arr):
    min_length = math.inf
    window_sum, window_start = 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        # shrink the window as small as possible until the 'window_sum'
        # is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0
    return min_length

# 3 (medium)


def longest_substring_with_k_distinct(string, k):
    used_chars = {}
    longest_len, window_start = 0, 0
    for window_end in range(len(string)):
        next_char = string[window_end]
        if next_char not in used_chars:
            used_chars[next_char] = 0
        used_chars[next_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct
        # characters in the char_frequency
        while len(used_chars) > k:
            left_char = string[window_start]
            used_chars[left_char] -= 1
            if used_chars[left_char] == 0:
                del used_chars[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        longest_len = max(longest_len, window_end - window_start + 1)

    return longest_len


# 4 (medium)
''' This problem follows the Sliding Window pattern
and is quite similar to Longest Substring with K Distinct Characters.
In this problem, we need to find the length of the longest subarray
with no more than two distinct characters (or fruit types!).
This transforms the current problem into Longest Substring
with K Distinct Characters where K=2.'''


def fruits_into_baskets(fruits):
    saved_fruits = {}
    longest_len, window_start = 0, 0
    for window_end in range(len(fruits)):
        next_fruit = fruits[window_end]
        if next_fruit not in saved_fruits:
            saved_fruits[next_fruit] = 0
        saved_fruits[next_fruit] += 1

        while len(saved_fruits) > 2:
            left_fruit = fruits[window_start]
            saved_fruits[left_fruit] -= 1
            if saved_fruits[left_fruit] == 0:
                del saved_fruits[left_fruit]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        longest_len = max(longest_len, window_end - window_start + 1)

    return longest_len


# 5 (hard)


def non_repeat_substring(string):
    saved_chars = {}
    max_len, window_start = 0, 0
    for window_end in range(len(string)):
        next_char = string[window_end]

        # if the map already contains the 'right_char', shrink the window
        # from the beginning so that
        # we have only one occurrence of 'right_char'
        if next_char in saved_chars:
            # this is tricky; in the current window, we will not have any
            # 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index
            # of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, saved_chars[next_char] + 1)

        # insert the 'right_char' into the map
        saved_chars[next_char] = window_end
        # remember the maximum length so far
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


# 6 Longest Substring with Same Letters after Replacement (hard)
# 7 Longest Subarray with Ones after Replacement (hard)

def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# 7 Longest Subarray with Ones after Replacement (hard) (see also 6)

def length_of_longest_subarray(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


''' Challenges '''

# 1


def find_permutation(str1, pattern):
    frequency_map = {}
    window_start, matched_count = 0, 0

    for _, x in enumerate(pattern):
        if x not in frequency_map:
            frequency_map[x] = 0
        frequency_map[x] += 1

    # our goal is to match all the characters from the 'char_frequency'
    # with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in frequency_map:
            frequency_map[right_char] -= 1
            if frequency_map[right_char] == 0:
                matched_count += 1

        if len(frequency_map) == matched_count:
            return True

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            if left_char in frequency_map:
                if frequency_map[left_char] == 0:
                    matched_count -= 1
                frequency_map[left_char] += 1
            window_start += 1

    return False


# 2 (see previous one)


def find_string_anagrams(str1, pattern):
    result_indexes = []
    frequency_map = {}
    window_start, matched_count = 0, 0

    for _, x in enumerate(pattern):
        if x not in frequency_map:
            frequency_map[x] = 0
        frequency_map[x] += 1

    # our goal is to match all the characters from the 'char_frequency'
    # with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in frequency_map:
            frequency_map[right_char] -= 1
            if frequency_map[right_char] == 0:
                matched_count += 1

        if len(frequency_map) == matched_count:
            result_indexes.append(window_end - len(frequency_map) + 1)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            if left_char in frequency_map:
                if frequency_map[left_char] == 0:
                    matched_count -= 1
                frequency_map[left_char] += 1
            window_start += 1
    return result_indexes


# 3
def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for _, x in enumerate(pattern):
        if x not in char_frequency:
            char_frequency[x] = 0
        char_frequency[x] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


def find_word_concatenation(str1, words):
    result_indices = []
    window_start, matched = 0, 0
    words_map = {}
    words_count = len(words)
    word_length = len(words[0])

    for _, x in enumerate(words):
        if x not in words_map:
            words_map[x] = 0
        words_map[x] += 1

    for window_end in range((len(str1) - words_count * word_length)+1):
        seen_words = {}
        substr = str1[window_start:window_end + 1]
        if substr in words_map:
            words_map[substr] -= 1
            if words_map[substr] >= 0:
                matched += 1
                if substr not in seen_words:
                    seen_words[substr] = 0
                seen_words[substr] += 1

    return result_indices


def max_sub_array_of_size_k_(k, arr):
    max_sum, window_start, window_sum = 0, 0, 0

    for window_end in range(len(arr)):
        right = arr[window_end]
        window_sum += right

        if window_end >= k - 1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


def smallest_subarray_with_given_sum_(s, arr):
    smallest_len = math.inf
    curr_sum, window_start = 0, 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]

        while curr_sum >= s:
            smallest_len = min(smallest_len, window_end - window_start + 1)
            curr_sum -= arr[window_start]
            window_start += 1

    if smallest_len == math.inf:
        return 0
    return smallest_len


def longest_substring_with_k_distinct_(string, k):
    max_len, window_start = 0, 0
    freq = {}

    for window_end in range(len(string)):
        right = string[window_end]
        if right not in freq:
            freq[right] = 0
        freq[right] += 1
        max_len += 1
        if len(freq) > k:
            left = string[window_start]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            window_start += 1
            max_len -= 1
    return max_len


def main():
    print(longest_substring_with_k_distinct_(
        ['A', 'B', 'C', 'B', 'B', 'C'], 2))
    # print(longest_substring_with_k_distinct_('araaci', 1))
    # print(longest_substring_with_k_distinct_('cbbebi', 3))


main()
