class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let maxLeftArray = [];
        let maxRightArray = [];
        let minLeftRightArray = [];
        let maxLeft = 0, maxRight = 0, result = 0;

        // populate maxLeft array
        for (let i = 0; i < height.length; i++) {
            if (i == 0) {
                maxLeftArray.push(0);
                continue;
            }
            maxLeft = Math.max(maxLeft, height[i - 1]);
            maxLeftArray.push(maxLeft);
        }
        
        // populate maxRight array
        for (let i = height.length - 1; i >= 0; i--) {
            if (i == height.length - 1) {
                maxRightArray.push(0);
                continue;
            }
            maxRight = Math.max(maxRight, height[i + 1]);
            maxRightArray.push(maxRight);
        }

        // populate minLeftRightArray
        for (let i = 0; i < height.length; i++) {
            minLeftRightArray.push(Math.min(maxLeftArray[i], maxRightArray[height.length - 1 - i]));
        }

        for (let i = 0; i < height.length; i++) {
            // calculate result
            let water = minLeftRightArray[i] - height[i];
            if (water > 0) {
                result += water;
            }
        }


        return result;
    }
}
