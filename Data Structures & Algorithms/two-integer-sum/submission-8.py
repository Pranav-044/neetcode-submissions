class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for k,m in enumerate(nums):
            dictionary[m]=k
        for i,j in enumerate(nums):
            res=target-j
            if res in dictionary and i!=dictionary[res]:
                return [i,dictionary[res]]
            
            

            

        