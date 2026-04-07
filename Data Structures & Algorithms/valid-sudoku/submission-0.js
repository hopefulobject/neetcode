class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        // first create a function that checks duplicates in an array

        function hasDuplicate(arr) {
            let hash = {};
            for (let n of arr) {
                console.log(n)
                if (n === '.') {
                    continue
                }
                if (hash[n]) {
                    return true
                }
                hash[n] = true
                 
            }
            return false

        }

        for (let row of board) {
            if (hasDuplicate(row)) {
                return false
            }
        }

        // generate columns
        let columns = []
        for (let i = 0; i < 9; i++) {
            let column = [];
            for (let row of board) {
                column.push(row[i])
            }
            columns.push(column)
        } 

        for (let column of columns) {
            if (hasDuplicate(column)) {
                return false
            }
        }


        // generating arrays of the 3x3 squares

        let three_by_threes = []
        for (let s = 0; s < 9; s+=3){
        for (let k = 0; k < 9; k+=3) { 
        let three_by_three = []
        for (let i = s; i < s+3; i++) {
            for (let j = k; j < k+3; j++) {
               three_by_three.push(board[i][j]) 
            }
        }
        three_by_threes.push(three_by_three);
        
        }}

        for (let three_by_three of three_by_threes) {
            if (hasDuplicate(three_by_three)) {
                return false
            }
        }

        return true


    }
}
