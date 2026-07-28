class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def func(arr, remaining, idx):
            if remaining == 0:
                out.append(arr.copy())
                return
            
            if remaining > 0:
                for i in range(idx, len(nums)):
                    arr.append(nums[i])
                    func(arr, remaining - nums[i], i)
                    arr.pop()
            
        func([], target, 0)
        return out