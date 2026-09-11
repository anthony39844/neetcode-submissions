class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(start, end):
            one, two = 0, 0
            for i in range(start, end):
                one, two = max(one, nums[i] + two), one
            
            return one
        
        return max(helper(1, len(nums)), helper(0, len(nums)-1))