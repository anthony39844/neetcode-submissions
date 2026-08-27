class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        visited = set()

        def dfs(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    arr.append(nums[i])
                    dfs(arr)
                    arr.pop()
                    visited.remove(nums[i])
                
        dfs([])
        return out