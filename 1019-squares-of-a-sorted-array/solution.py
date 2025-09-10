class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums=[x*x for x in nums]
        s=sorted(sq_nums)
        return s
