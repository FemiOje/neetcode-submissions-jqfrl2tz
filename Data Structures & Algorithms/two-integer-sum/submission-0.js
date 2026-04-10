class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = new Map();
        for (let i=0; i< nums.length; i++) {
            let difference = target - nums[i];

            if (hashMap.has(difference)) {
                return [hashMap.get(difference), i];
            }
            hashMap.set(nums[i], i);
        }
    }
}
