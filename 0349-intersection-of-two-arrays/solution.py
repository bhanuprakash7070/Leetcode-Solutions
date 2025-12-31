class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.nums1=nums1
        self.nums2=nums2
        r=[]
        for i in nums1:
            c1=nums1.count(i)
            c2=nums2.count(i)
            if (c1 and c2)>=1:
                if i not in r:
                    r.append(i)
        u=list(set(r))
        return u
        
