class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        t=x
        if(x<0):
           x=-1*x
        while(x!=0):
           r=x%10
           s=s*10+r
           x=x//10
        if s>2**31-1 or s<-(2**31):
            return 0
        if(t<0):
           s=-1*s
        print(s)   
        return s
