class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def func(arr, idx, remaining):
            if remaining == 0:
                out.append(arr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if remaining - candidates[i] < 0:
                    return
                if i != idx and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                func(arr, i + 1, remaining - candidates[i])
                arr.pop()
        1, 2, 2, 4, 5, 6, 9
        func([], 0, target)
        return out
