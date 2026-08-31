class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        updated_s=list(s)
        updated_t=list(t)
        final_s=sorted(updated_s)
        final_t=sorted(updated_t)
        if (final_s == final_t):
            return True
        else:
            return False


        