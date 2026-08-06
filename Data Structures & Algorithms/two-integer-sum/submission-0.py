class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        length = len(nums)
        for i in range(0,length):
            for j in range(i+1,length):
                if(nums[i]+nums[j]==target):
                    l1.append(i)
                    l1.append(j)
                    return l1
