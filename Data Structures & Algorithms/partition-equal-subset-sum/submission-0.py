class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half = sum(nums) // 2
        dp = [False] * (half + 1)

        def dfs(total, idx):
            if total > half:
                return False
            if total == half:
                return True
            
            for i in range(idx, len(nums)):
                total += nums[i]
                if dfs(total, i + 1):
                    return True
                total -= nums[i]
            
            return False
        
        return dfs(0, 0)