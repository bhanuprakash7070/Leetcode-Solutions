class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=len(nums)
        l=0
        h=s-1
        while l<=h:
            m=l+((h-l)//2)
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        return -1


