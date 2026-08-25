class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(arr, idx):
            out.append(arr.copy())
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                dfs(arr, i + 1)
                arr.pop()
            
        dfs([], 0)
        return out