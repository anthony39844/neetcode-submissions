class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        # make a list of n + 1 items
        freq = [[] for i in range(len(nums) + 1)]

        # each index corresponds with the frequency of a num
        for i in d.items():
            freq[i[1]].append(i[0])
        
        # get the k most frequent nums
        out = []
        for i in range(len(freq) -1 , -1, -1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out
