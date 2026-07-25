class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        print(candidates)
        def backtrack(start, arr, remaining):
            if remaining < 0:
                return
            if remaining == 0:
                nonlocal out
                out.append(arr.copy())
                return 
            
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, arr + [candidates[i]], remaining - candidates[i])
            
        backtrack(0, [], target)
        return out