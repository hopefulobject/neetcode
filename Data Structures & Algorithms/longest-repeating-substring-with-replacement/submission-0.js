class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {

        let count = new Array(26).fill(0);

        let left = 0;
        let max_freq = 0;
        let longest = 0;

        for (let right = 0; right < s.length; right++) {
            let index = s.charCodeAt(right) - 65;
            count[index]++;

            max_freq = Math.max(max_freq, count[index]);

            while((right-left+1) - max_freq > k) {
                count[s.charCodeAt(left) - 65]--;
                left++;
            }

            longest = Math.max(longest, right-left+1);
        }

        return longest;


    }
}
