# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/2.%20Pattern%20Two%20Pointers/Triplet%20Sum%20to%20Zero%20(medium).py
# _Topic_ @2 Pattern: Two Pointers
# _Q_ @2. b)
# _Difficulty_ medium

# Problem Statement:
"""
Problem Statement 
Given an array of unsorted numbers, 
find all unique triplets in it that add up to zero.
Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""

# my solution:
# unsorted!!
# is it worth sorting first, then two pointers???
# don't think so.
# why not sliding window? because not necessarily consecutive elems
# hash table implementation??
# options: 2+ve + 1-ve; 2-ve + 1+ve; x + 0 + -x
# go through everything, save zero, two hashtables???
def MYbruteForce_search_triplets(arr):  # INCORRECT!
    # NOW DUPLICATES LEFT.
    # f it, brute force first.
    options_list = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] == 0:
                    options_list.append([arr[i],arr[j],arr[k]])
    return options_list

def MY2_search_triplets(arr):  # DOES NOT TERMINATE!
    triplets = []
    num_map = {}
    arr.sort()
    left, right = 0, len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum>0:
            k = left+1
            while current_sum>0:
                if (current_sum+k == 0):
                    triplets.append([left,k,right])
                    break
                k+=1
        elif current_sum<0:
            k = right-1
            while current_sum<0:
                if (current_sum+k == 0):
                    triplets.append([left,k,right])
                    break
                k-=1
        elif current_sum==0:
            # find 0! <- shouldn't have to each time.
            k = left+1
            while k<right:
                if arr[k] == 0:
                    triplets.append([left,k,right])
                    break
                k+=1
    return triplets

def MYlast_search_triplets(arr):  # ERROR WHILE RUNNING
    # two pointers, one hashmap
    triplets = []
    left, right = 0, len(nums) - 1
    while left < right:
        twosum = arr[left] + arr[right]
        if (twosum not in num_map):
            num_map[twosum] = [pointer1, pointer2]
        
        if (0-arr[left] in num_map):
            triplets.append(num_map[0-arr[left]].append(left))
        elif (0-arr[right] in num_map):
            triplets.append(num_map[0-arr[right]].append(right))
        left+=1
        right+=1
    return triplets

## ANSWER: does seem to adapt the (2.a)) target sum pair kind of...?
# looks like you were "kind of getting in the right direction"?..?
# well with in-built sorting, but with the left<right....?
def search_triplets(arr):
    # THEY SORT!
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum

""" Asymptotics:
For mine 1: O(n^3) <- not ideal :(, 
    sorting first potentially better? with O(n^2 * log(n))
    my final: O(n) <- but probably one huge logic error to be honest.
For sols: O(n*log(n)) + O(n)*O(n) = O(n^2 +(!) n*log(n)) = O(n^2)
    sorting takes O(n*log(n)). search pair called 'n' times. 
    this looks at one less elem each time. so we have the O(n^2) for the for loop
    in search_triplets() and search_pair().
Space complexity:
    O(n) extra space for sorting. maybe +O(n) for the triplets space??
    Good job: sols say "Ignoring the space required for the output array, 
    the space complexity of the above algorithm will be O(N) 
    which is required for sorting."
"""


# Additional code.
def main():
    print("My answer:")
    print(MYbruteForce_search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(MYbruteForce_search_triplets([-5, 2, -1, -2, 3]))

    print("Solutions:")
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))

main()
