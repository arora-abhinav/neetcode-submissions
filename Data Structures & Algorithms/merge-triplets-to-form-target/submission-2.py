class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        broken = False
        for j, t in enumerate(triplets):
            for i in range(3):
                if t[i] > target[i]:
                    broken = True
                    break
            if not broken:
                valid_triplets.append(j)
            else:
                broken = False
        
        count = 0
        if len(valid_triplets) > 0:
            for i in range(3):
                for t in valid_triplets:
                    if triplets[t][i] == target[i]:
                        count += 1
                        break

            return True if count == 3 else False
        return False 