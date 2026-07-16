class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        

        out = [[] for i in range(len(nums) + 1)]
        for i in d:
            out[d[i]].append(i)
        
        res = []
        for i in range(len(out) - 1, -1, -1):
            for j in out[i]:
                res.append(j)
                if len(res) == k:
                    return res
