class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2):
            return False
        dp=set()
        dp.add(0)
        target=sum(nums)//2
        for i in range(len(nums)):
            curr=set()
            for t in dp:
                curr.add(t+nums[i])
                curr.add(nums[i])
            dp.update(curr)
            if(target in dp):
                return True
        return False