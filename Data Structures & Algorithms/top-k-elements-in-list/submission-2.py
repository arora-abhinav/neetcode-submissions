class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for i in nums:
            frequency_map[i] = frequency_map.get(i, 0) + 1
        

        arr = [[] for i in range(len(nums) + 1)]
        
        for key in frequency_map:
            arr[frequency_map[key]].append(key)
        
        final_arr = []

        for x in range(len(arr) - 1, 0, -1):
            for a in arr[x]:
                if k > 0:
                    final_arr.append(a)
                    k -= 1
        
        return final_arr

