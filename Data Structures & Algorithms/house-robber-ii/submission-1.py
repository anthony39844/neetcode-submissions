class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one, two = 0, 0

        for i in range(len(nums) - 1, 0, -1):
            cur = max(one, nums[i] + two)
            two = one
            one = cur
        
        out = one
        one, two = 0, 0
        for i in range(len(nums) - 1):
            cur = max(one, nums[i] + two)
            two = one
            one = cur
        
        return max(out, one)