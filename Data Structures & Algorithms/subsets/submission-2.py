class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        def func(arr, idx):
            out.append(arr.copy())

            for i in range(idx, len(nums)):
                func(arr + [nums[i]], i + 1)
            
        func([], 0)
        return out
