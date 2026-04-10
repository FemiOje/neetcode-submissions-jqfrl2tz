class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let set1 = new Set();
        let length = 0;

        // add each element of nums to the set
        for (let i = 0; i < nums.length; i++) {
            set1.add(nums[i]);
        };

        // iterate through nums again:
        // for each element, check if its successor is in the set,
        // and keep increasing the length until breaks
        for (let i = 0; i < nums.length; i++) {
            let new_length = 0;
            let number = nums[i];

            if (!set1.has(number - 1)){
                while (set1.has(number)) {
                    new_length++;
                    number++;
                };
            }

            // check if new length is greater than previous length
            // if yes, set new length
            if (new_length > length) {
                length = new_length;
            }
        }

        return length;
    }
}
