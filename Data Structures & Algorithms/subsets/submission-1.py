class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(start, arr):
            nonlocal out
            out.append(arr.copy())

            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
            
        backtrack(0, [])
        return out