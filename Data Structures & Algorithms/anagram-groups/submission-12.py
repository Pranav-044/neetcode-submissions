from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary=defaultdict(list)
        for i in strs:
            array=[0]*27
            for k in i:
                array[ord(k)-ord("a")]+=1
            dictionary[tuple(array)].append(i)
        res=list(dictionary.values())
        print(res)
        return res
            

        
        