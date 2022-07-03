'''
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

# sliding window
def find_longest_substring(exl_string):
	window_start, max_length = 0, 0
	char_index_map = {}
	curr_len = 0
	# try O(n):
	for wind_end in range(len(exl_string)):  
		current_letter = exl_string[wind_end]
		# shorten the window to last found letter index
		if current_letter in char_index_map:
			max_length = max(max_length, curr_len)
			# shrink:
			first_repeated_char_index = char_index_map[current_letter]
			while window_start-1 < first_repeated_char_index:
				char_index_map.pop(exl_string[window_start])
				window_start += 1
				curr_len -= 1
			### continue here
		# no repeated chars...:
		char_index_map[current_letter] = wind_end
		curr_len += 1
	
	return max(max_length, curr_len)

def main():
	print(find_longest_substring("aabccbb"))
	print(find_longest_substring("abbbb"))
	print(find_longest_substring("abccde"))

main()