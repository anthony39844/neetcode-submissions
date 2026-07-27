class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def func(arr, visited):

            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            
            for i in nums:
                if i not in visited:
                    visited.add(i)
                    func(arr + [i], visited)
                    visited.remove(i)

        func([], set())
        return out