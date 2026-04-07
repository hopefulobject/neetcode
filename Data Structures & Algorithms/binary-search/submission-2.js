class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length -1;
        let i;
        while (l<=r) {
        i = Math.ceil(r-l/2);
        if (nums[i]===target) return i;
        if (nums[i] > target) r = i-1;
        if (nums[i] < target) l = i+1;
        }
        return -1

            
    }
}
