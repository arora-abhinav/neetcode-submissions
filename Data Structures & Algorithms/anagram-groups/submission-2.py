class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = dict()

        for cur in strs:
            
            char_map = [0] * 26
            for char in cur:
                char_map[ord(char)-97] += 1
            hashable = tuple(char_map)
            if hashable not in anagrams_dict:
                anagrams_dict[hashable] = []
            anagrams_dict[hashable].append(cur)
        return list(anagrams_dict.values())
