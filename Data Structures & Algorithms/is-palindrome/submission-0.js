class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        // I first need to get the string that consists only of alphanumeric characters.
        
        s = s.replace(/[^a-zA-Z0-9]/g, '').toLocaleLowerCase();
        if (s === s.split('').reverse().join('')) return true;
        return false;


    }
}
