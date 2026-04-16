class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1. Sort by position,speed (descending order) closest to the target to farthest
        2. Compute the time taken for each car to reach the target.
        3. If the speed is higher than the cars in front of it, it merges
        4. Use a stack to see how many entries are in the stack at the end. 
        """
        pos_speed = [(pos,s) for pos, s in zip(position, speed)]
        pos_speed.sort(reverse=True)
        time = []

        for pos, speed in pos_speed:
            rt = (target-pos)/speed
            if not time or time[-1] < rt:
                time.append(rt)
        return len(time)

        

        