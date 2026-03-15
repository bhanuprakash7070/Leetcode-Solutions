class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if n>999:
            c=n-999
            return c
        else:
            return 0
                
