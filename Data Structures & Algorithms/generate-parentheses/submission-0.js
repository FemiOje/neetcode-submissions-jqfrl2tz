class Solution {
    backtrack(openN, closedN, n, res, stack) {
        if (openN === closedN && openN === n) {
            res.push(stack);
            return;
        }

        if (openN < n) {
            this.backtrack(openN + 1, closedN, n, res, stack + '(');
        }

        if (closedN < openN) {
            this.backtrack(openN, closedN + 1, n, res, stack + ')');
        }
    }
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        let result = [];

        this.backtrack(0,0,n,result,'');

        return result;

    }
}
