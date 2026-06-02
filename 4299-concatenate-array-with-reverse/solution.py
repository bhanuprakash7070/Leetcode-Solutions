class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        tnums=[]
        for i in nums:
            tnums.append(i)
        for j in range(len(nums)-1,-1,-1):
            tnums.append(nums[j])
        return tnums
