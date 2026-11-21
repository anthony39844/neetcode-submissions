class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        d = Counter(hand)
        hand.sort()
        
        for card in hand:
            if d[card] == 0:
                continue
            
            for i in range(groupSize):
                cur = card + i
                if cur not in d or d[cur] <= 0:
                    return False
                d[cur] -= 1
                     
        return True