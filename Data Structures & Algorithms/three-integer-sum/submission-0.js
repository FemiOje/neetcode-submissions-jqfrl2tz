class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let result = [];

        nums.sort((a, b) => {
            return a - b;
        }); // 0 (n * log n)

        for (let i = 0; i < nums.length; i++) { // 0 (n ** 2 )
            if (i > 0 && nums[i] === nums[i - 1]) continue;

            let leftPointer = i + 1;
            let rightPointer = nums.length - 1;

            while (leftPointer < rightPointer) {
                let threeSum = nums[i] + nums[leftPointer] + nums[rightPointer];
                
                if (threeSum > 0) {
                    rightPointer--;
                } else if (threeSum < 0) {
                    leftPointer++;
                } else {
                    result.push([nums[i], nums[leftPointer], nums[rightPointer]]);
                    leftPointer++;
                    rightPointer--;

                    while (leftPointer < rightPointer && nums[leftPointer] === nums[leftPointer - 1]) {
                        leftPointer++;
                    }
                }
            };
        };
        return result;
    }
}
