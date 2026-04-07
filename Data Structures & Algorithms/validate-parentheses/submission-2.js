class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
      let stack = [];
      for (let b of s.split('')) {
        if (b === '(') stack.push(')');
        else if (b === '{') stack.push('}');
        else if (b === '[') stack.push(']');
        else if (b !== stack.pop()) return false; 
      }
      if (stack.length === 0) return true;
      else return false;

    }
}
