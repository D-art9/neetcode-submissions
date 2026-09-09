class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in (nums):
            freq[i]=freq.get(i,0)+1
        topk={}
        sortedfreq=sorted(freq.items(),
        key=lambda x:x[1],
        reverse=True)
        topk=[]
        for i in range(k):
            topk.append(sortedfreq[i][0])
        return topk