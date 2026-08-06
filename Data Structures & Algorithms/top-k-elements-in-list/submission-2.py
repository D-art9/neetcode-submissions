class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
         freq[num] = freq.get(num, 0) + 1

        # Sort the dictionary items by frequency in descending order
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Take the first k elements from the sorted list
        for i in range(k):
            ans.append(sorted_freq[i][0])
                
        return ans