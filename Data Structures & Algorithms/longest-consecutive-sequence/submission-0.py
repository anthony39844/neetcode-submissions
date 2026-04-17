class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put nums in a set
        s = set(nums)
        count = 1
        m = 0

        for i in nums:
            while i - 1 in nums:
                count += 1
                i -= 1
            m = max(count, m)
            count = 1
    
        return m