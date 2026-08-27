class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def dfs(idx, arr):
            out.append(arr.copy())

            if idx >= len(nums):
                return 
            
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                dfs(i + 1, arr)
                arr.pop()
        
        dfs(0, [])
        return out
