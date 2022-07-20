# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/4.%20Pattern%20Merge%20Intervals/Insert%20Interval%20(medium).py
# _Topic_ @4 Pattern: Merge Intervals
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

# ANSWER
# looks smart. I think that was my first approach and then I doubted myself
def insert(intervals, new_interval):
	merged = []
	i, start, end = 0, 0, 1
	# skip (and add to output) all intervals that come before the 'new_interval'
	while i < len(intervals) and intervals[i][end] < new_interval[start]:
		merged.append(intervals[i])
		i += 1
	# merge all intervals that overlap with 'new_interval'
	while i < len(intervals) and intervals[i][start] <= new_interval[end]:
		new_interval[start] = min(intervals[i][start], new_interval[start])
		new_interval[end] = max(intervals[i][end], new_interval[end])
		i += 1
	# insert the new_interval
	merged.append(new_interval)
	# add all the remaining intervals to the output
	while i < len(intervals):
		merged.append(intervals[i])
		i += 1
	return merged

""" Asymptotics:
For sols: O(n) <- goes through 'intervals' once 
For mine: O(n) <- I tried.
Space complexity: O(n) <- adding new interval to already existing intervals is at worst n+1 space 
	where n is the number of intervals in 'intervals'
"""


# Additional code
def main():
	print("My answer:")
	print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6])))
	print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10])))
	print("Intervals after inserting the new interval: " + str(insert_interval([[2, 3], [5, 7]], [1, 4])))

	print("Solutions:")
	print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
	print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
	print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

main()
