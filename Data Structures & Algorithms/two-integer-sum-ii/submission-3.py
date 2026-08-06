class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size=len(numbers)
        l=0
        r=size-1
        summ=0
        l1=[]
        while(l<r):
            summ=numbers[l]+numbers[r]
            if(summ==target):
                l1.append(l+1)
                l1.append(r+1)
                return(l1)
            if summ>target:
                r=r-1
            if summ<target:
                l=l+1


      
        