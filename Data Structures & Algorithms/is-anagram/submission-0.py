class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for i in s :
            freq[i]=freq.get(i,0) +1
        for i in t :
            if i not in freq:
                return False
            freq[i]-=1
        for value in freq.values():
            if(value!=0):
                return False    
        return True    