class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                continue
            else:
                if i + nums[i] >= len(nums):
                    dp[i] = 1
                else:
                    for j in range(i, i + nums[i]+1):
                        if dp[j] == 1:
                            dp[i] = 1
        print(dp)
        return dp[0] == 1
