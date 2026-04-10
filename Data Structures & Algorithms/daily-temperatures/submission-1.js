class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        // Optimal solution
        let helperStack = [];
        let result = [];

        for (let i = temperatures.length - 1; i >= 0; i--) {
            
            // case 1: stack empty
            if (helperStack.length === 0) {
                result[i] = 0;
                helperStack.push([temperatures[i], i]);
                continue;
            }

            // case 2: i is greater than stack top
            while ((helperStack.length > 0) && (temperatures[i] >= helperStack[helperStack.length - 1][0])) {
                helperStack.pop();
            }


            // case 3: temps[i] is less than stack top
            if (helperStack.length > 0) {
                let diff = helperStack[helperStack.length - 1][1] - i;
                result[i] = diff;
            } else {
                result[i] = 0;
            }
            helperStack.push([temperatures[i], i]);
        }

        return result;
    }
}
