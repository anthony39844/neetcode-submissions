class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        nums1 = nums[:n-1]
        nums2 = nums[1:]
        one1, two1 = 0, 0
        one2, two2 = 0, 0

        for i in range(len(nums1)):
            cur1 = max(nums1[i] + two1, one1)
            two1 = one1
            one1 = cur1
            cur2 = max(nums2[i] + two2, one2)
            two2 = one2
            one2 = cur2
        
        return max(one1, one2)