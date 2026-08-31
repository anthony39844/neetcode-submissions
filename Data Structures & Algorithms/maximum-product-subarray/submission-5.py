class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = max(nums)
        maxx, minn = 1, 1

        for i in nums:
            if i == 0:
                maxx, minn = 1, 1
            else:
                tmp = maxx
                maxx = max(i * maxx, i * minn, i)
                minn = min(i * tmp, i * minn, i)
                out = max(out, maxx)
        return out
