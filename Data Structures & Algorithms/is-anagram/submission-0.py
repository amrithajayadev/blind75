class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for c in s:
            if s_map.get(c) == None:
                s_map[c] = 1
            else:
                s_map[c] += 1
        for c in t:
            if t_map.get(c) == None:
                t_map[c] = 1
            else:
                t_map[c] += 1
        
        if len(s_map) != len(t_map):
            return False

        for k1 in s_map:
            if t_map.get(k1) != s_map.get(k1):
                return False
        for k1 in t_map:
            if t_map.get(k1) != s_map.get(k1):
                return False
        return True

        