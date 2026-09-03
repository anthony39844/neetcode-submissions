class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn, maxx = 1, 1
        out = max(nums)

        for i in range(len(nums)):
            if nums[i] < 0:
                minn, maxx = maxx, minn
            maxx = max(maxx * nums[i], nums[i])
            minn = min(minn * nums[i], nums[i])

            out = max(out, maxx)

        return out