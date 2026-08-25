class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []

        def dfs(idx, remaining, arr):
            if remaining < 0:
                return
            if remaining == 0:
                out.append(arr.copy())
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                dfs(i, remaining - nums[i], arr)
                arr.pop()
            
        dfs(0, target, [])
        return out