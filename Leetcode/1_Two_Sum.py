class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_dict = {}  # to store numbers and their indices
        for i, num in enumerate(nums):
            x = target - num
            if x in indices_dict:
                return [indices_dict[x], i]
            else:
                indices_dict[nums[i]] = i
        # return [-1, -1]
