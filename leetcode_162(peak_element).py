class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        beg=0
        end=len(nums)-1
        while(beg<end):
            mid=(beg+end)//2
            if(nums[mid]>nums[mid+1]):
                end=mid
            else:
                beg=mid+1
        return beg
