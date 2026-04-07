class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for num in nums:
            if table.get(num) != None:
                result = [nums.index(target-num)]
                nums[nums.index(target-num)] = None
                result.append(nums.index(num))
                return result
            table[target-num] = num


        