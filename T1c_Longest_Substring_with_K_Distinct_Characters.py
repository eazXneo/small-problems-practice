# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/Maximum%20Sum%20Subarray%20of%20Size%20K%20(easy).py
# _Topic_ @1 Pattern: Sliding Window
# _Q_ @1. c)
# _Difficulty_ medium

# Problem Statement:
"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

# my solution
# broute force would be looking at all possible substrings -> O(n!)??
# try implementing sliding window instead.
# window is not fixed size (difficulty up..?)
# Idea: <- not bad, overall it seems right intuition with minor execution mistakes.
# have array
# have start and end
# add elem check if <=k distinct chars
# if yes increase max
# else delete from front until <=k?
def MY_longest_substring_with_k_distinct(_str, k):
    max_substring_length , current_max , curr_window_start = 0 , 0 , 0
    curr_substring = _str[0]
    curr_set = set(_str[0])

    for curr_window_end in range(1, len(_str)):
        curr_substring = curr_substring + _str[curr_window_end]
        curr_set.add(_str[curr_window_end])
        while len(curr_set) > k:
            # now invalid window.
            check = _str[curr_window_start]
            curr_substring = curr_substring[1:]
            # check if char still in substring
            if not (check in curr_substring):  # potentially O(n) work extra here? not sure.
                curr_set.discard(check)  # then can delete from set
            curr_window_start += 1
        # update the max substring length
        if len(curr_substring) > max_substring_length:
            max_substring_length = len(curr_substring)


    return max_substring_length


## ANSWER:
def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]  # char_frequency.pop(left_char)??
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end-window_start + 1)
    return max_length

""" Thoughts: 
Is mine less efficient by a whole asymtotic measurement 
or is it just a constant number of more calculations. Or same calcs??
I think mine does do a bit more because it actually "touches" each
element 3 times as opposed to adding and deleteing it from the "window". """

""" Asymptotics:
For sols: O(n) + while loop? -> O(n)+O(n){?} = O(n+n) = O(2n) = O(n)
    This is because inner while loop touches each elem once and runs for "each character" 
    (max. len-k chars though, more precisely, right?)
For mine: similar? Slightly more inefficient because no dict, instead traverse substring which could be O(n)??
    In which case, algo ok, but data struct improvement to be made?
Space Complexity 
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
#So they ignore the capacity used by initial array? In IADS, I don't think they did.
"""


# Additional code.
def main():
    print("My answer:")
    print("Length of the longest substring: " + str(MY_longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(MY_longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(MY_longest_substring_with_k_distinct("cbbebi", 3)))
    print("Extra?")
    print("Length of the longest substring: " + str(MY_longest_substring_with_k_distinct("araaar", 2)))

    print("Solutions:")
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()
