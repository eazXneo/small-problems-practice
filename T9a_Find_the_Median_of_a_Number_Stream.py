# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/9.%20Pattern%20Two%20Heaps/Find%20the%20Median%20of%20a%20Number%20Stream%20(medium).py
# _Topic_ @9 Pattern: Pattern Two Heaps
# _Q_ @9. a)
# _Difficulty_ medium
# Time taken until for own solution, without compiling the code: 

# Problem Statement
"""
Design a class to calculate the median of a number stream. The class should have the following two methods:
insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""

# My solution
from heapq import *
