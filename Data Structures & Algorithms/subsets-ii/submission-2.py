class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def func(arr, idx):
            out.append(arr.copy())

            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                func(arr + [nums[i]], i + 1)
            
        func([], 0)
        return out
