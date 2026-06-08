class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            
            if i == ')' or i == '}' or i == ']':
                if len(stack) == 0:
                    return False

                if self.isCorrespondingClose(stack[-1], i):
                    stack.pop()
                else:
                    return False
        
        # is valid
        return len(stack) == 0


    def isCorrespondingClose(self, stackTop:str, b: str) -> bool:
        return (stackTop == '(' and b == ')') or (stackTop == '{' and b == '}') or (stackTop == '[' and b == ']')
