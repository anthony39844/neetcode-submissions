class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            s += i + "@ant@"
        
        return s
    def decode(self, s: str) -> List[str]:
        x = s.split("@ant@")
        return x[:len(x) - 1]