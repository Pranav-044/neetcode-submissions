class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def backtracking(index,store):
            if(index == len(nums)):
                final.append(store)
                return
            backtracking(index+1,store+[nums[index]])
            backtracking(index+1,store)
        backtracking(0,[])
        return final

                
