class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ch=''
        s=0
        c=0
        
        for ch in events:
        
            if ch=="W":
                c+=1
            if ch=="WD" or ch=="NB":
                s+=1
            elif ch in {"0","1","2","3","4","6"}:
                s=s+int(ch)
            if c==10:
                break
        return [s,c]
