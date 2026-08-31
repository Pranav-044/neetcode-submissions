from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += str(len(i)) + "#" + i
        return string

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            string_start_index = j + 1
            string_end_index = j + 1 + length
            
            final.append(s[string_start_index:string_end_index])
            
            i = string_end_index
            
        return final