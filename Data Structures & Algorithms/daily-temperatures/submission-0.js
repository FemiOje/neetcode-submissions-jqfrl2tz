class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        // Brute Force
        let result = [];

        for (let i = 0; i < temperatures.length; i++) {

            if (i === temperatures.length - 1) {
                result.push(0);
            }

            for (let j = i + 1; j < temperatures.length; j++) {
                if (j === temperatures.length - 1 && temperatures[j] <= temperatures[i]) {
                    result.push(0);
                    break;
                }
                
                if (temperatures[j] > temperatures[i]) {
                    result.push(j - i);
                    break;
                }

            }
        }

        return result;
    }
}
