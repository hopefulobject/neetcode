class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let p1 = 0;
        let p2 = numbers.length - 1; 

        while (p1 !== p2) {
            let n1 = numbers[p1];
            let n2 = numbers[p2];
            if (n1+n2 === target) return [p1+1,p2+1];
            if (n1+n2 < target) p1++;
            if (n1+n2 > target) p2--;
        }
    }
}
