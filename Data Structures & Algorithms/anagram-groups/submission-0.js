class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let groups = new Map();

        for (let i=0; i< strs.length; i++) {
            let signature = strs[i].split('').sort().join('');
            if (!groups.has(signature)){
                groups.set(signature, []);
            }
            groups.get(signature).push(strs[i]);
        }

        return Array.from(groups.values());
    }
}
