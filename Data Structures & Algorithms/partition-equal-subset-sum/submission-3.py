class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half = sum(nums) // 2
        dp = set()

        def dfs(total, idx):
            if total > half or (total, idx) in dp:
                return False
            if total == half:
                return True
            
            for i in range(idx, len(nums)):
                total += nums[i]
                if dfs(total, i + 1):
                    return True

                dp.add((total, idx))
                total -= nums[i]

            return False
        
        return dfs(0, 0)