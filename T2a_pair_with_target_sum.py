# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/2.%20Pattern%20Two%20Pointers/Pair%20with%20Target%20Sum%20(easy).py
# _Topic_ @2 Pattern: Two Pointers
# _Q_ @2. a)
# _Difficulty_ easy

# Problem Statement:
"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""


# my solution: brute force: look at all pairs.
# smarter: look at only pairs only up to sum, since list is sorted?
def MY_pair_with_targetsum(arr, target_sum):
    # two forls to point at two items
    for i in range(len(arr)):
        # start at i, and so i==j won't happen, also avoids some repeats.
        for j in range(i, len(arr)):
            # if sum is greater than target, no need to continue looking.
            if arr[i] + arr[j] > target_sum:
                break
            if arr[i] + arr[j] == target_sum:  # found a pair of indices
                return [i, j]


## ANSWER
def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]  # if nothing found!


""" Asymptotics:
For mine: hard to tell for my own code somehow.
    originally would be repeating work. with second for loop 
    running for less each time, now still O(n^2) work I think. Not ideal.
    Why is this still happening. insead of j touching each elem once, 
    It touches them 1,2,3,..,n-1 times I think. Better than looking at 
    all pairs but still O(n^2) :(
For sols: the two pointers come from opposite ends until they meet.
    => every iteration they move towards each other by one so  = O(n)
Kind of binary search style?
Space complexity is O(1), just the two pointers for any size of arr
"""


# Additional code.
"""
An Alternate approach (2)
Read more here: https://emre.me/coding-patterns/two-pointers/
"""

def ALT_pair_with_targetsum(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]

""" Notes for alt. approach
size of "arr" = n
Time complexity: O(n) <- looks at each elem once.
Space complexity: O(n) <- need to have hashtable size of array (worst case apparently)
    so space complexity in avg. case is what??
    --> because this "hashTable" is actually a dictionary. So basically "Python ver. of HashTable",
    since in Java HashTable is a dictionary right?
"""

def main():
    print("My answer:")
    print(MY_pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(MY_pair_with_targetsum([2, 5, 9, 11], 11))
    print("Extra?")
    print(MY_pair_with_targetsum([2, 3], 2))

    print("Solutions:")
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
    print("Alternative solution")
    print(ALT_pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(ALT_pair_with_targetsum([2, 5, 9, 11], 11))


main()
