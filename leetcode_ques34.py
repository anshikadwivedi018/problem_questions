class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        b=[]
        flag=0
        for i in range(len(nums)):
            if(nums[i]==target):
                b.append(i)
                flag+=1
        if flag==0:
            b.append(-1)
            b.append(-1)
            return b
        else:
            return (min(b),max(b))
