class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        visited = set()

        def func(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    arr.append(nums[i])
                    visited.add(nums[i])
                    func(arr)
                    visited.remove(nums[i])
                    arr.pop()

        func([])
        return out