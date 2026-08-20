class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums)
        nums1, nums2 = nums[1:], nums[:len(nums)-1]
        one, two = 0, 0

        for i in nums1:
            temp = max(one, i + two)
            two = one
            one = temp
        
        x, y = 0, 0
        for i in nums2:
            temp = max(x, i + y)
            y = x
            x = temp
        
        return max(x, one)