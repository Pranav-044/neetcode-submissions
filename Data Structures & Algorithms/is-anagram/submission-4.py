class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for j1_initial in set(s):
            dict1[j1_initial]=0
        for j2_initial in set(t):
            dict2[j2_initial]=0
        for i1_initial in s:
            dict1[i1_initial]+=1
        for i2_initial in t:
            dict2[i2_initial]+=1
        if(dict1 == dict2):
            return True
        else:
            return False
        


        