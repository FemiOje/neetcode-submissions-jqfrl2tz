class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        let s1 = {};
        let t1 = {};

        for (let i = 0; i < s.length; i++){
            if (s[i] in s1){
                s1[s[i]]++;
            }else {
                s1[s[i]] = 1;
            }
        };

        for (let i = 0; i < t.length; i++){
            if (t[i] in t1){
                t1[t[i]]++;
            }else {
                t1[t[i]] = 1;
            }
        };

        for (const k in s1) {
            // if the frequency of key k in s1 is not same as t1 
            if (s1[k] !== t1[k]) {
                return false;
            }
        };
        return true;
    }
}
