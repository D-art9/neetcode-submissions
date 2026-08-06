class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        count=0
        sett=set()
        res=0
        
        for  r in  range(0,len(s)):
            while(s[r] in sett):
                sett.remove(s[l])
                l=l+1
            sett.add(s[r])
            res=max(res,r-l+1)

        return res
        