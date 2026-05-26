class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        l=len(nums)
        if l<=2:
            return -1
        nums.sort() 
        return nums[1]
