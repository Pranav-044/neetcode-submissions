import math
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maximum=0
        l=nums[0:k]
        r=len(nums)-k
        final=[max(l)]
        for i in range(r):
            l[i]=-math.inf
            l.append(nums[i+k])
            final.append(max(l))
        return final




        