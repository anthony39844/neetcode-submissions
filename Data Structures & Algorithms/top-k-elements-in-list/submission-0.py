class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        out = []
        a = sorted(list(d.items()), key=lambda x:x[1], reverse=True)
        for i in range(k):
            out.append(a[i][0])
        
        return out