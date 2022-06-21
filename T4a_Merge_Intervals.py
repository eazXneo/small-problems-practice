# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/4.%20Pattern%20Merge%20Intervals/Merge%20Intervals%20(medium).py
# _Topic_ @5 Pattern: Merge Intervals
# _Q_ @4. a)
# _Difficulty_ medium

# Problem Statement
"""
Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, 
we merged them into one [1,5].
Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged 
them into one [5,9].
Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""

# from answer
from __future__ import print_function
# My solution:
class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    # from answers:
    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


final_intervals = []
# I think intervals and final_intervals are being mixed up :(
def MY_merge(intervals):
    if len(intervals) == 1:
        return final_intervals.apppend(intervals)
    else:
        current = intervals[0]
        for interval in final_intervals:
            if interval.start < current.start and interval.end > current.end:  # case 1
                continue
            elif interval.start < current.start and interval.end < current.end:  # case 2
                interval.end = current.end
            elif interval.start > current.start and interval.end > current.end:  # case 3
                interval.start = current.start
            elif interval.start > current.start and interval.end < current.end:  # case 4
                interval.start = current.start
                interval.end = current.end
            else:  # no overlap
                final_intervals.apppend(current)
        merge(intervals[1:])
    return final_intervals


## ANSWER
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:  # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:  # non-overlapping interval, add the previous internval and reset
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals
