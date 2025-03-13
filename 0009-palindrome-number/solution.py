class Solution(object):
    def isPalindrome(self,x):
        if(x<0):
            return False
        t=x
        s=0
        while(x!=0):
            r=x%10
            s=s*10+r
            x=x//10
        if(s==t):
            return True
        else:
            return False
    
        
        
