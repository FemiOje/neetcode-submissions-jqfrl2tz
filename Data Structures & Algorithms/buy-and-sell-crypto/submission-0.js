class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0, r = 1; // initialise pointers
        let maxProfit = 0; // initialise max profit

        while (r < prices.length) { // while right pointer is not out of bounds
            let diff = prices[r] - prices[l]; // check trend 
            
            if (diff > 0) { // if trend is positive
                maxProfit = Math.max(maxProfit, diff);
            } else { // reposition pointers
                l = r;
            }

            r++;
        }

        return maxProfit;
    }
}
