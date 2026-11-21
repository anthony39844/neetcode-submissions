class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        d = Counter(hand)
        cards = sorted(d)
        
        for card in cards:
            if d[card] > 0:
                count = d[card]
                for i in range(groupSize):
                    cur = card + i
                    if d[cur] <= 0:
                        return False
                    d[cur] -= count
                        
        return True