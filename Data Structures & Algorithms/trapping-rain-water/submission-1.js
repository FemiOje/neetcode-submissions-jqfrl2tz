class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
        trap(height) {
        let left = 0, right = height.length - 1;
        let leftMax = 0, rightMax = 0;
        let result = 0;
  
        while (left < right) {
            if (height[left] < height[right]) {
                // Process left side
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    result += leftMax - height[left];
                }
                left++;
            } else {
                // Process right side
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    result += rightMax - height[right];
                }
                right--;
            }
        }
        return result;
    }
}
