class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0, r = 0;
        let maxSubstringLength = 0, tempMaxLength = 0;
        let newSet = new Set();

        while (r < s.length) {
            if (!newSet.has(s[r])) {
                newSet.add(s[r]);
                tempMaxLength++;
                r++;
                maxSubstringLength = Math.max(maxSubstringLength, tempMaxLength);
            } else {
                newSet.delete(s[l]);
                l++;
                tempMaxLength--;
            }
        }

        return maxSubstringLength;
    }
}
