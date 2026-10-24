class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,mid,k=0,0,len(nums)-1
        while(mid<=k):
            if(nums[mid] == 0):
                nums[i],nums[mid] =nums[mid],nums[i] 
                mid+=1
                i+=1
            elif(nums[mid] == 1):
                mid+=1
            else:
                nums[mid],nums[k] = nums[k],nums[mid]
                k-=1
        
            



        """
        Do not return anything, modify nums in-place instead.
        """
        