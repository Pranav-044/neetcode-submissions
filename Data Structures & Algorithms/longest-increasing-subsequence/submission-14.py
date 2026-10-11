class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            element=nums[i]
            for j in range(i-1,-1,-1):
                if(element>nums[j]):
                    dp[i]= max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)






        
        


        
        
        