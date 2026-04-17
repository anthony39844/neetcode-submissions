class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left right product
        # 1 2 4 6

        # l = 1
        # 1 1 2 8

        # r = 1
        # 48 24 6 1

        # loop backwards
          
        out = []
        l = 1
        for i in nums:
            out.append(l)
            l *= i

        r = 1
        for i in range(len(nums) - 1, -1 , -1):
            out[i] *= r
            r *= nums[i]

        return out

