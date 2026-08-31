class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for i in strs:
            string+=i+"`"
        return string


    def decode(self, s: str) -> List[str]:
        final=s.split("`")
        return final[:len(final)-1]
