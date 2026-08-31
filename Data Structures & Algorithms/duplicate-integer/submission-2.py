class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary={}
        for j in set(nums):
            dictionary[j]=0
        
        for i in nums:
            dictionary[i]+=1
            if dictionary[i]>1:
                return True
        return False

            
        