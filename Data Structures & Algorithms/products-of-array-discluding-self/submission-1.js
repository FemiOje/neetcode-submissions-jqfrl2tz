class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let output = [];
        let prefix = 1;
        let postfix = 1;
        
        for (let i = 0; i < nums.length; i++) {
            if (i === 0) {
                output.push(prefix);
                continue;
            };
            prefix *= nums[i - 1];
            output.push(prefix);
        };

        for (let j = nums.length - 1; j >= 0; j--) {
            output[j] *= postfix;
            postfix *= nums[j];
        };

        return output;
    }
}