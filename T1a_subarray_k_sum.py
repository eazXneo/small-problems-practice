# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/1.%20Pattern%20Sliding%20Window/Maximum%20Sum%20Subarray%20of%20Size%20K%20(easy).py
# _Topic_ Pattern: Sliding Window
# _Q_ @1. a)
# _Difficulty_ easy

# Problem Statement:
"""
Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

# my solultion
def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here
    max_sum = 0

    for i in range(len(arr)-3):  # traverse the array
    	subarray = arr[i:i+3]  # take next group of k elems
    	subarray_sum = sum(subarray)  # sum these

    	max_sum = max(subarray_sum, max_sum)  # update max if new max

    return max_sum

## ANSWER:
def max_sub_array_of_size_k(k, arr):
  	max_sum, window_sum = 0, 0
  	window_start = 0

  	for window_end in range(len(arr)):
    	window_sum += arr[window_end]  # add the next element
    	# slide the window, we don't need to slide if we've not hit the required window size of 'k'
    	if window_end >= k-1:
      		max_sum = max(max_sum, window_sum)
      		window_sum -= arr[window_start]  # subtract the element going out
      		window_start += 1  # slide the window ahead
  	return max_sum

""" Thoughts: 
Is mine less efficient by a whole asymtotic measurement 
or is it just a constant number of more calculations. Or same calcs??
I think mine does do a bit more because it actually "touches" each
element 3 times as opposed to adding and deleteing it from the "window". """

""" Asymptotics:
For sols: O(n) -> one loop and constant time within
For mine: O(n) -> like above. Using built-in "sum" and "max".
"sum" will take O(k) time.
So actually O(kn)??
Looks like it
"""


# Additional code.
def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
