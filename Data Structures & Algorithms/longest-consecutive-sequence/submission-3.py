class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        out = 1
        for i in nums:
            cur = 1
            if i - 1 in s:
                continue
            while i + 1 in s:
                cur += 1
                i += 1
            out = max(cur, out)
        return out
            