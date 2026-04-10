class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        let leftPointer = 0;
        let rightPointer = heights.length - 1;

        while (leftPointer < rightPointer) {
            let area = (rightPointer - leftPointer) * Math.min(heights[leftPointer], heights[rightPointer]);
            maxArea = Math.max(area, maxArea);
            
            //
            if (heights[leftPointer] < heights[rightPointer]) {
                leftPointer++;
            } else {
                rightPointer--;
            }
        }

        return maxArea;
    }
}
