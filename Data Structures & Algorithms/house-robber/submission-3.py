class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for i in nums:
            cur = max(one, i + two)
            two = one
            one = cur

        return one