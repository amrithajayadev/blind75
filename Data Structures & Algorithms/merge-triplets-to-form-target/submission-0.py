class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Brute-force is to apply the max operation operation on each pair 
        # 1 level opt : to apply the max operation only with the triplet that has the first element of target.
        # This will take O(n) to linearly search
        # 3 pass solution for each number in the target.
        """
        triplets = [[2,5,6],[1,4,4],[5,7,5],[2,11,12],[7,11,12],[2,11,0]], target = [5,11,12]
        Create 3 maps
        map1 = all the triplets whose first element matches with target[0] and second and third less than target
        map2 = all the triplets whose second element matches with target[1] and first element<= target.
        map3 = all the triplets whose third element matches with target[2] and first and second element<= target.

        If any map empty, then solution is not possible, else true.
        """
        map1 = {}
        map2 = {}
        map3 = {}
        for trip in triplets:
            if trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                map1[trip[0]] = trip
            if trip[1] == target[1] and trip[0] <= target[0] and trip[2] <= target[2]:
                map2[trip[1]] = trip
            if trip[2] == target[2] and trip[1] <= target[1] and trip[0] <= target[0]:
                map3[trip[2]] = trip
        if map1 and map2 and map3:
            return True
        else:
            return False

        