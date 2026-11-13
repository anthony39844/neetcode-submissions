class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur, maxx = nums[0], nums[0]

        for i in nums[1:]:
            if cur < 0:
                cur = 0
            cur += i
            maxx = max(cur, maxx)
        return maxx
