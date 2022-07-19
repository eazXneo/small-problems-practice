# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/4.%20Pattern%20Merge%20Intervals/Insert%20Interval%20(medium).py
# _Topic_ @4 Pattern: Merge Intervales
# _Q_ @4. b)
# _Difficulty_ medium
# Time taken until for own solution, without compiling the code: 40 min

# Problem Statement
"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals 
to produce a list that has only mutually exclusive intervals.
Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], 
we merged them into [4,12].
Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""

# My solution:
def insert_interval(intervals, new_interval):
	# trivial: intervals is empty
	temp = len(intervals)
	if len(intervals)==0:
		intervals.append(new_interval)

	# insert new_interval into intervals.
	# trying basic approach
	new_interv_start = new_interval[0]
	new_interv_end = new_interval[1]
	for i in range(len(intervals)):
		interval = intervals[i]
		if interval[0] <= new_interv_end:
			new_interv_end = max(interval[1], new_interv_end)
		else:
			intervals.insert(i+1, new_interval)
			break
	if new_interval_start > intervals[-1][1]:
		intervals.append(new_interval)

	return intervals
