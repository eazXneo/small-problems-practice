# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/Maximum%20Sum%20Subarray%20of%20Size%20K%20(easy).py
# _Topic_ @1 Pattern: Sliding Window
# _Q_ @1. b)
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
# Idea: 
# have array
# have start and end
# add elem check if <=k distinct chars
# if yes increase max
# else delete from front until <=k?
def longest_substring_with_k_distinct(_str, k):
	max_substring_length , current_max , curr_window_start = 0 , 0 , 0
	curr_substring = _str[0]
	curr_set = set(_str[0])

	for curr_window_end in range(len(str)):
		curr_substring = curr_substring + _str[curr_window_end]
		curr_set.add(_str[curr_window_end])
		while len(curr_set) >= k:
			# now invalid window.
			check = curr_substring[curr_window_start]
			curr_substring -= curr_substring[curr_window_start]
			if not (check in curr_substring):
				curr_set.discard(check)
			curr_window_start += 1
	

	return max_substring_length
