class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if i in operators:
                pop2 = stack.pop()
                pop1 = stack.pop()

                if i == '+': stack.append(pop1 + pop2)
                elif i == '-': stack.append(pop1 - pop2)
                elif i == '*': stack.append(pop1 * pop2)
                elif i == '/': stack.append(int(pop1 / pop2))
            else:
                stack.append(int(i))

        return stack[-1]
        