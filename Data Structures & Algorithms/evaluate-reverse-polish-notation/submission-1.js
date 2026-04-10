class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];

        for (let i=0 ; i<tokens.length ; i++) {
            if (!["+", "-", "*", "/"].includes(tokens[i])) {
                stack.push(parseInt(tokens[i]));
            }
            else {
                let pop1 = stack.pop();
                let pop2 = stack.pop();
                let res;

                switch (tokens[i]) {
                    case "+":
                        res = pop2 + pop1;
                        stack.push(res);
                        break;
                    
                    case "-":
                        res = pop2 - pop1;
                        stack.push(res);
                        break;

                    case "*":
                        res = pop2 * pop1;
                        stack.push(res);
                        break;

                    case "/":
                        res = pop2 / pop1;
                        stack.push(Math.trunc(res));
                        break;

                    default:
                        break;
                }
            }
        }
        return stack[stack.length - 1];
    }
}