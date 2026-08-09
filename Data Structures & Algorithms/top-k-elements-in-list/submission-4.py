class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = count.values()
        max_freq = max(frequencies)
        res = []
        freq_to_num = {}
        for item in count:
            if count[item] not in freq_to_num:
                freq_to_num[count[item]] = []
            freq_to_num[count[item]].append(item)
        
        while k > 0:
            if max_freq in freq_to_num:
                start_ind = 0
                while k > 0 and start_ind < len(freq_to_num[max_freq]):
                    k -= 1
                    res.append(freq_to_num[max_freq][start_ind])
                    start_ind += 1
            max_freq -= 1
        
        return res