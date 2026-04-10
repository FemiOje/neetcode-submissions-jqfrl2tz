class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map = {};

        for ( let i = 0; i < nums.length; i++) {
            map[nums[i]] ? map[nums[i]]++ : map[nums[i]] = 1; 
        }

        let sortedMap = Object.entries(map).sort((a, b) => b[1] - a[1]);

        return sortedMap.slice(0,k).map(item => item[0]);
    }
}
