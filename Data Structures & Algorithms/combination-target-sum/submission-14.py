class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final=[]
        final_target=target
        def backtracking(index,target,store):
            if(index == len(nums) or target == 0):
                if(sum(store) == final_target):
                    final.append(store)
                return
            elif(target<0):
                return
            backtracking(index,target-nums[index],store+[nums[index]])
            backtracking(index+1,target,store)
        backtracking(0,target,[])
        return final

        