class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = dict()

        for cur in strs:
            sorted_str = ''.join(sorted(cur))
            if sorted_str not in anagrams_dict:
                anagrams_dict[sorted_str] = list()
            anagrams_dict[sorted_str].append(cur)

        return list(anagrams_dict.values())