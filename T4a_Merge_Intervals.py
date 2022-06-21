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
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    # from answers:
    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# trying do brute-force.
final_intervals = []
# I think intervals and final_intervals are being mixed up :(
# abandoning recursion currently and the weirdly incorrect interval classification
def MY_merge(intervals):  # at least it runs?
    if len(intervals) == 1:
        return final_intervals.apppend(intervals)
    else:
        current = intervals[0]
        for interval in intervals:
            if interval is current:
                continue
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
                final_intervals.append(current)
        merge(intervals[1:])
    return final_intervals

# incorrect. abandonded
def MY2_merge(intervals):  # try 2
    final_intervs = []
    # choose one, go through list adding on.
    # finally append to final_intervs
    # delete from intervals and start over
    current = intervals[0]
    while len(intervals) != 0:
        for interv in intervals:
            # check (+ merge?)
            if interv.start < current.start and interv.end > current.start:
                new_interv = Interval(interv.start, max(interv.end, current.end))
                final_intervs.append(new_interv)
                intervals.remove(current)
                intervals.remove(interv)
            elif interv.start > current.start and interv.start < current.end:
                new_interv = Interval(current.start, max(interv.end, current.end))
                final_intervs.append(new_interv)
                intervals.remove(current)
                intervals.remove(interv)
            else: # no overlap
                continue
        if current == intervals[0]:
            if len(intervals) != 1:
                current = intervals[1]
            else:
                final_intervs.append(intervals[0])
                intervals.pop(0)
        else:
            current = intervals[0]
    # check final invterval
    return final_intervs

## ANSWER
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)  # SORTING N*LOG(N)!!

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

    # add the last interval  # what??
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals

""" Asymptotics:
For sols: O(n * log(n)) -> sorting + for loop (O(n))
For mine: n/a
Space complexity: O(n) -> store solution (and sorting). ok.
"""


# Additional code
def main():
    print("My answer (INCORRECT! probably need way of comparing intervals for euality.):")
    print("Merged intervals: ", end='')
    for i in MY2_merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()
    print("Merged intervals: ", end='')
    for i in MY2_merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()
    print("Merged intervals: ", end='')
    for i in MY2_merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

    print("Solutions:")
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()
    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()
