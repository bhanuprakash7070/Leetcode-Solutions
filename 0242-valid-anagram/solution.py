class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f={}
        for ch in s:
            f[ch]=f.get(ch,0)+1
        for ch in t:
            if ch not in s:
                return False
            f[ch]-=1
        for v in f.values():
            if v!=0:
                return False
        return True        

