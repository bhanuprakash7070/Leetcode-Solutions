class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # j starts from i+1 to avoid using same index
                if nums[i] + nums[j] == target:
                    return [i, j]

