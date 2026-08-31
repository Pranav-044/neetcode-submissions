class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1={}
        dictionary2={}
        for i in s:
            dictionary1[i]=dictionary1.get(i,0)+1
        for j in t:
            dictionary2[j]=dictionary2.get(j,0)+1
        if(dictionary1 == dictionary2):
            return True 
        else:
            return False


        