from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        output = []
        for word in strs:
            added = False
            st = Counter(word)
            for key in anagram_map.keys():
                if Counter(key) == st:
                    anagram_map[key].append(word)
                    added = True
                    break
            if not added:
                anagram_map[tuple(word)].append(word)
            

        for key, val in anagram_map.items():
            output.append(val)
        return output

        