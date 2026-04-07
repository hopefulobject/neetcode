class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length == 0) return 0;

        let set = new Set(nums);
        let longest = 1;

        for (let n of set) {
            set.add(n);
            if (!set.has(n-1)) {
                let checking = n+1;
                let current = 1;
                while(set.has(checking)) {
                    current++;
                    checking++;
                } 
                if (current > longest) longest = current;
            }

            
        }
        return longest;

    }
}
