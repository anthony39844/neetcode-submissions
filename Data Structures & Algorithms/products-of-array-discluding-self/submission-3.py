class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input = [1, 2, 4, 6]
        # left = [1, 1, 2, 8]
        # right = [48, 24, 6, 1]
        # out = [48, 24, 12, 8]

        l = 1
        left = [1]
        '''
        - we are looping through the len(list) - 1 because the first left product
        will always be 1
        - the l variable is the accumulation of the left product
        - so we are multiplying nums[i] * l to get the left product of the current index
        - the current index is actually i + 1 as the first one we already precalculated to be 1
        '''
        for i in range(len(nums) - 1):
            l *= nums[i]
            left.append(l)

        x = 1
        out = [0] * len(nums)
        for i in range(len(nums) - 1, -1 , -1):
            out[i] = x * left[i]
            x *= nums[i]
        
        return out
            
        