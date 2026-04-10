class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let start_index = 0;
        let end_index = s.length - 1;

        while (start_index < end_index) {
            while (start_index < end_index && this.isNonAlphanumeric(s[start_index])) {
                start_index++;
            }

            while (start_index < end_index && this.isNonAlphanumeric(s[end_index])) {
                end_index--;
            }

            if (s[start_index].toLowerCase() !== s[end_index].toLowerCase()) {
                return false;
            }

            start_index++;
            end_index--;
        }

        return true;
    }

    isNonAlphanumeric(s) {
        return /[^A-Za-z0-9]/g.test(s);
    }
}