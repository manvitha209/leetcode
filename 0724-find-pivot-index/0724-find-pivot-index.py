class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        left=0
        for i in range(len(nums)):
            sum+=nums[i]
        for i in range(len(nums)):
            right=sum-left-nums[i]
            if(left==right):
                return i
            left+=nums[i]
        return (-1)




















