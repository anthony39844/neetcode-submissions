class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = nums[1:]
        one, two = 0, 0
        for i in cur:
            temp = max(i+two, one)
            two = one
            one = temp
        
        one2, two2 = 0, 0
        cur = nums[:len(nums)-1]
        for i in cur:
            temp = max(i+two2, one2)
            two2 = one2
            one2 = temp
        
        return max(one, one2)