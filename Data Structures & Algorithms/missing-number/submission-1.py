class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        l = len(nums)
        return (l * (l+1))//2 - s
