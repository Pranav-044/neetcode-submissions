class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=sorted(zip(position,speed),reverse=True)
        stack=[]
        for pos,speed in arr:
            time=(target-pos)/speed
            while not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)