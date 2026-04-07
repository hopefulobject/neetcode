class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        if (heights.length == 1) return heights[0];
        let longesth = 0;
        let longestv = heights[0];
        let stack = [[Math.min(heights[0], heights[1]), 0]];
        let addlater = [];
        for (let i = 1; i < heights.length; i++) {
            longestv = Math.max(heights[i], longestv);


            let min = Math.min(heights[i], heights[i-1])
            
            if (stack.length === 0) {
                stack.push([Math.min(heights[i], heights[i-1]), i-1])
            }
            else if (min > stack[stack.length-1][0]) {
                stack.push([min, i-1]);
            }
            else while (min < stack[stack.length-1][0]) {
                let last = stack.pop();
                longesth = Math.max((i-last[1]) * last[0], longesth);
                if (min > 0) {
                    addlater.push([min, last[1]])
                }
                if (stack.length === 0) break;
            }
            while (addlater.length > 0) stack.push(addlater.pop());
            console.log(stack, i)

            
            
        }

        while (stack.length > 0) {
            let last = stack.pop();
            longesth = Math.max(((heights.length)-last[1]) * last[0], longesth);
        }


        return Math.max(longesth, longestv);
    }
}
