class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []

        def dfs(arr, idx, remain):
            if remain < 0:
                return
            
            if remain == 0:
                out.append(arr.copy())

            for i in range(idx, len(candidates)):
                if i != idx and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                dfs(arr, i + 1, remain - candidates[i])
                arr.pop()

        dfs([], 0, target)
        return out