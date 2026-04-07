class Solution {
    lengthOfLongestSubstring(s) {
        if (s.length === 0) return 0;

        let l = 0;
        let r = 0;
        let hash = new Map();
        let longest_substring = 0;

        while (r < s.length) {
            let right = s[r];

            if (hash.has(right)) {
                l = Math.max(l, hash.get(right) + 1);
            }

            hash.set(right, r);
            longest_substring = Math.max(longest_substring, r - l + 1);
            r++;
        }

        return longest_substring;
    }
}
