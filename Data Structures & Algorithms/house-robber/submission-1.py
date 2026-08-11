class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums)
        n = len(nums)

        for i in range(n-3, -1, -1):
            nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        
        return nums[0]