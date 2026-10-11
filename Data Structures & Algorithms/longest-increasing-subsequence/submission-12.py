class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            element=nums[i]
            setter=set()
            for j in range(i-1,-1,-1):
                if(element>nums[j] and nums[j] not in setter):
                    dp[i]= max(dp[i],dp[j]+1)
                    setter.add(nums[j])
        print(dp)
        return max(dp)






        
        


        
        
        