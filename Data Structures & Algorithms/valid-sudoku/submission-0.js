class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        let rows = new Map();
        let cols = new Map();
        let boxes = new Map();

        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[i].length; j++) {
                // skip all "." (empty grids)
                if (board[i][j] == ".") continue;

                let boxKey = (Math.floor(i / 3) * 3 + Math.floor(j / 3));
                if (!rows.has(i)) rows.set(i, new Set()); 
                if (!cols.has(j)) cols.set(j, new Set()); 
                if (!boxes.has(boxKey)) boxes.set(boxKey, new Set());

                // check each row for duplicates,
                // if any, return false
                if (rows.get(i).has(board[i][j])) {
                    return false;
                }

                // check each column for duplicates, 
                // if any, return false
                if (cols.get(j).has(board[i][j])) {
                    return false;
                }
                
                // check each square for duplicates, 
                // if any, return false
                if (boxes.get(boxKey).has(board[i][j])) {
                    return false;
                }

                // Else, add it to its corresponding hashMap
                rows.get(i).add(board[i][j]);
                cols.get(j).add(board[i][j]);
                boxes.get(boxKey).add(board[i][j]);
            }
        }
        return true;
    }
}
