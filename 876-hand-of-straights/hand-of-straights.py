from heapq import heapify, heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cards = Counter(hand)
        

        min_hand = list(cards.keys())
        heapq.heapify(min_hand)
        

        while min_hand:
            x = min_hand[0]

            #print(cards, min_hand)
            for i in range(groupSize):
                if cards.get(x,0) != 0 :
                    cards[x] -= 1

                    if not cards[x]:
                        min_hand.remove(x)
                        heapify(min_hand)

                    x += 1
                    
                
                else:
                    return False
                    

        return True