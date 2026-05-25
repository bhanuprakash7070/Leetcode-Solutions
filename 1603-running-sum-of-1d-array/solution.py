class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs=0
        ans=[]
        for i in range(0,len(nums)):
            rs+=nums[i]
            ans.append(rs)
        return ans
