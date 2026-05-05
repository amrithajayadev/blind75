class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0-p0 : only zeroes
        p0-p1 : only 1s (end goal)
        p2-n : only 2s

        unsorted area is between p1-p2
        """
        p0 = 0
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            if nums[p1] == 0:
                nums[p1], nums[p0] = nums[p0], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1

            

        