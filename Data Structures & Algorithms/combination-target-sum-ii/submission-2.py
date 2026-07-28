class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def func(arr, idx, remaining):
            if remaining == 0:
                out.append(arr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i != idx and candidates[i] == candidates[i - 1] or remaining - candidates[i] < 0:
                    continue
                arr.append(candidates[i])
                func(arr, i + 1, remaining - candidates[i])
                arr.pop()
        
        func([], 0, target)
        return out
