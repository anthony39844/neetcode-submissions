class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left right product
        # left = [1, 1, 2, 8]
        # right = [24, 24, 6, 1]
        l = [1]
        r = [1]
        for i in range(len(nums) - 1):
            l.append(l[i] * nums[i])
        print(l)
        for i in range(len(nums) - 1, 0, -1):
            r.append(r[-1] * nums[i])
        print(r)
        r = r[::-1]
        for i in range(len(l)):
            r[i] *= l[i]
        return r