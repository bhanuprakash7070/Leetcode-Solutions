import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        m=0
        preGcd=[]
        for i in nums:
            m=max(m,i)
            preGcd.append(math.gcd(i,m))
        preGcd.sort()
        
        s=0
        l=0
        r=len(preGcd)-1
        while(l<r):
            s+=math.gcd(preGcd[l],preGcd[r])
            l+=1
            r-=1
            
            
        return s
            
    
            
    
