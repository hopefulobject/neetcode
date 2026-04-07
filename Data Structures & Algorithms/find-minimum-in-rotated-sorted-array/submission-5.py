class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        start = 0
        middle = len(nums) // 2
        end = len(nums) - 1
        
        while True:
            if nums[middle] > nums[end]:
                if end - middle == 1:
                    return nums[end]
                start = middle
                middle = start + (end - middle) // 2
            else:
                if middle - start == 1:
                    return nums[middle]
                end = middle
                middle = start + (middle - start) // 2


            




        