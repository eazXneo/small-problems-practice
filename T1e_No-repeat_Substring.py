# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/No-repeat%20Substring%20(hard).py
# _Topic_ @1 Pattern: Sliding Window
# _Q_ @1. e)
# _Difficulty_ hard

# Problem Statement
'''
Given a string, find the length of the longest substring which has no
repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters
is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters
is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters
are "abc" & "cde".
'''

# My solution:
# sliding window
def find_longest_substring(exl_string):
    window_start, max_length = 0, 0
    char_index_map = {}
    curr_len = 0
    # try O(n):
    for wind_end in range(len(exl_string)):
        current_letter = exl_string[wind_end]
        # shorten the window to last found letter index
        if current_letter in char_index_map:
            max_length = max(max_length, curr_len)
            # shrink:
            first_repeated_char_index = char_index_map[current_letter]
            while window_start - 1 < first_repeated_char_index:
                char_index_map.pop(exl_string[window_start])
                window_start += 1
                curr_len -= 1
        ### continue here
        # no repeated chars...:
        char_index_map[current_letter] = wind_end
        curr_len += 1

    return max(max_length, curr_len)

## ANSWER
# approach 1
def non_repeat_substring(str):
    max_len, win_start = 0, 0
    dict_str = {}

    for win_end in range(len(str)):
        if str[win_end] not in dict_str:
            dict_str[str[win_end]] = 1
        else:
            dict_str[str[win_end]] += 1

        while len(dict_str) < sum(dict_str.values()):
            if dict_str[str[win_start]] == 1:
                del dict_str[str[win_start]]
            else:
                dict_str[str[win_start]] -= 1
            win_start += 1

        if len(dict_str) == sum(dict_str.values()):
            max_len = max(max_len, len(dict_str))
    return max_len

# approach 2 (cleaner?)
def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str)):
        right_char = str[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(find_longest_substring("aabccbb"))
    print(find_longest_substring("abbbb"))
    print(find_longest_substring("abccde"))


main()