class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        arr = []

        def func(idx):
            if idx > len(nums):
                return
            
            out.append(arr.copy())
            
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                func(i + 1)
                arr.pop()
        
        func(0)
        return out