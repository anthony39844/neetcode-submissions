class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def backtrack(arr, remaining, start):
            if remaining == 0:
                out.append(arr.copy())
                return
            
            for i in range(start,len(nums)):
                if remaining - nums[i] >= 0:
                   backtrack(arr + [nums[i]], remaining - nums[i], i)

        backtrack([], target, 0)
        return out