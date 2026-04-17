class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums = [1, 2, 4, 6]
        left = [1, 1, 2, 8]
        out = [0, 0, 0, 0] | i = len(nums) - 1
            = [0, 0, 0, 8 * 1] left[i] * right -> right * nums[i] -> i -= 1
            = [0, 0, 2 * 6, 8] left[i] * right -> right * nums[i] -> i -= 1
            = [0, 1 * 24, 12, 8]
            = [1 * 48, 24, 12, 8]
        out = [48, 24, 12, 8]
        '''
        
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

        '''
        - now we loop backwards to multiply the left and right products to get the final output
        - we build the right product as we loop through and multiply by the previously calculated
        left product
        '''
        right = 1
        out = [0] * len(nums)
        for i in range(len(nums) - 1, -1 , -1):
            out[i] = right * left[i]
            right *= nums[i]
        
        return out
            
        