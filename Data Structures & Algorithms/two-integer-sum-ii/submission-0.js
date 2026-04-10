class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        // 1. add all elements to hash map (element -> index)
        let map = new Map();

        // note: handle edge case [1, 1, 3, 4]
        for (let i=0; i< numbers.length; i++) {
            map.set(numbers[i], i+1);
        }

        // 2. traverse through array:
        for (let j = 0; j < numbers.length ; j++) {
        //  for each element, check if two-sum is in the hashmap,
        //      and if 
        //      two-sum index (index 2) > element index (index 1)
            let num = numbers[j];
            let difference = target - num;

            if (map.has(difference) && (j+1) < map.get(difference) ) {
                return [j+1, map.get(difference)];
            }
        }

        // 3. If yes, return both indexes
    }
}
