class Solution:

    def _find_combi(self, nums, target, combi) -> List[List[int]]:
        if target == 0:
            return [combi]
        if not nums or target < 0:
            return []

        result = []
        n = nums[0]

        for k in range((target // n + 1)):
            result.extend(self._find_combi(nums[1:], target - k * n, combi + [n] * k))

        return result



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self._find_combi(nums, target, [])

            
            
            



        



        