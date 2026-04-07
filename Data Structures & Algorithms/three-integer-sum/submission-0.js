class Solution {
    threeSum(nums) {
        nums.sort((a,b)=>a-b);
        let result = [];

        for (let i = 0; i < nums.length; i++) {

            if (i > 0 && nums[i] === nums[i-1]) continue;

            let p1 = i + 1;
            let p2 = nums.length - 1;
            let target = -nums[i];

            while (p1 < p2) {
                let sum = nums[p1] + nums[p2];

                if (sum === target) {
                    result.push([nums[i], nums[p1], nums[p2]]);

                    p1++;
                    p2--;

                    while (p1 < p2 && nums[p1] === nums[p1-1]) p1++;
                    while (p1 < p2 && nums[p2] === nums[p2+1]) p2--;
                }
                else if (sum < target) {
                    p1++;
                }
                else {
                    p2--;
                }
            }
        }
        return result;
    }
}
