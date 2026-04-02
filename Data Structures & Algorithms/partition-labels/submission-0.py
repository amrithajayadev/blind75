class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Create a map of char to the max index where it is present. - O(n)
        {
        "x": (0,3),
        "y": (1,4),
        "z":  (5,7),
        "b": (6,9),
        "i": (10,10),
        "s": (11,11),
        "l": (12,12)
        } 

        Scan through the map and merge overlapping intervals - O(n)

        "xy": (0,4)
        "zb": (5,9)
        "i" :
        "s" :
        "l" : 


        return the list of 4-0+1, 9-5+1, 1,1,1
        """
        ch = {}
        for i, c in enumerate(s):
            if ch.get(c):
                ch[c][1] = i
            else:
                ch[c] = [i, i]

        intervals = list(ch.values())
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = merged[-1]
            if intervals[i][0] <= prev[1]:
                if intervals[i][1] > prev[1]:
                    merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        
        output = []
        for intv in merged:
            output.append(intv[1]-intv[0]+1)

        return output