import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heap = hand; heapq.heapify(heap); counter = Counter(hand)
        while heap:
            while heap and counter[heap[0]] == 0:
                heapq.heappop(heap)
            if heap:
                for i in range(groupSize):
                    if heap[0] + i in counter and counter[heap[0] + i] > 0:
                        counter[heap[0] + i] -= 1
                        continue
                    return False
        
        return True
             