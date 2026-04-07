class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let answer;
        let stack = [];
        if (tokens.length === 1) return tokens[0];
        for (let token of tokens) {
            console.log(stack);
            if (!(['+', '*', '-', '/'].includes(token))) stack.push(parseInt(token)); 
            else if (token === '+') {
                answer = stack.pop()
                answer+=stack.pop()
                stack.push(answer)
            }
            else if (token === '*') {
                answer = stack.pop()
                answer*=stack.pop()
                stack.push(answer)
            }
            else if (token === '-') {
                answer = stack.pop()
                answer = stack.pop() - answer;
                stack.push(answer)
            }
            else if (token === '/') {
                answer = stack.pop();
                answer= Math.trunc(stack.pop()/answer);
                stack.push(answer)
            }

        }
        return answer;
    }
}
