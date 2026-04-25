class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in nums[:k]:
            while q and i > q[-1]:
                q.pop()
            q.append(i)
        
        res = [q[0]]
        for i, x in enumerate(nums[k:]):
            # pop out date ele
            if q and q[0]==nums[i]:
                q.popleft()
            
            while q and x > q[-1]:
                q.pop()
            q.append(x)
            res.append(q[0])
        return res

        
