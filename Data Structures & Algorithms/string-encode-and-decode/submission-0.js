class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = "";
        strs.forEach((str)=> {
            result += str.length + "#" + str;
        });
        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if (str == "") {return []};

        let result = [];
        let i = 0;

        while (i < str.length) {
            let j = i;
            let number = "";

            while (str[j] != "#") {
                number += str[j];
                j++;
            }

            // read the next "number" strings 
            result.push(str.slice(j + 1, j + 1 + Number(number)));
            
            // update i position
            i = j + 1 + Number(number);
        }
        return result;
    }
}