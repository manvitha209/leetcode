class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # res=[]
        # nums=0
        # for i in range(len(nums)):
        #     nums+=1
        #     left=nums[i]<=10
        #     right=nums[i]>10
        #     res.append(nums)
        # return(res)
        left=[]
        middle=[]
        right=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]==pivot:
                middle.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
        return left+middle+right
