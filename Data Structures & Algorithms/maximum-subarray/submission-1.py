class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=0
        final=float("-inf")
        for i in nums:
            maximum+=i
            final=max(final,maximum)
            if(maximum<0):
                maximum=0
        return final


        