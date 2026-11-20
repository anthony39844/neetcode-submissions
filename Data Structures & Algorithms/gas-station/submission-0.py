class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        out = 0
        i = 0
        
        while i < len(gas):
            if gas[i] >= cost[i]: # we can travel to the next gas station starting at gas[i]
                out = i # the return val
                remaining = gas[i] - cost[i]
                cur = i

                while True:
                    cur = (cur + 1) % len(gas)
                    remaining += gas[cur] - cost[cur]
                    if remaining < 0:
                        break
                    if cur == out:
                        return out
                if cur < out:
                    return -1 
                i = cur + 1
            else: 
                i += 1    
        return -1
                