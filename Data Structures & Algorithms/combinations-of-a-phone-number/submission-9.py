class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        out = []

        def dfs(idx, s):
            if idx >= len(digits):
                out.append(s)
                return
            
            for char in d[digits[idx]]:
                s += char
                dfs(idx + 1, s)
                s = s[:-1]
  
        dfs(0, "")
        return out
