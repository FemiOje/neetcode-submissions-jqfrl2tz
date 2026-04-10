class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let sta = [];

        for (let i = 0; i < s.length; i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                sta.push(s[i]);
            } else {
                switch (s[i]) {
                    case ')':
                        if (sta.length > 0 && sta[sta.length - 1] == '(') {
                            sta.pop();
                        } else {
                            return false;
                        }
                        break;

                    case '}':
                        if (sta.length > 0 && sta[sta.length - 1] == '{') {
                            sta.pop();
                        } else {
                            return false;
                        }
                        break;
        
                    case ']':
                        if (sta.length > 0 && sta[sta.length - 1] == '[') {
                            sta.pop();
                        } else {
                            return false;
                        }
                        break;

                    default:
                        return false;
                }
            }
        }

        return sta.length === 0;
    }
}

