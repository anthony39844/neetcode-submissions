class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            print(x, y)
            if x == y:
                continue
            else:
                heapq.heappush_max(stones, abs(y - x))
        
        if stones:
            return stones[0]
        else:
            return 0
        

