class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur, total = 0, 0
        out = 0

        for i in range(len(gas)):
            remaining = gas[i] - cost[i]
            cur += remaining
            total += remaining

            if cur < 0:
                out = i + 1
                cur = 0
            
        return out if total >= 0 else -1
                