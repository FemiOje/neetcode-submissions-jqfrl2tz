class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if self.isOpen(i):
                stack.append(i)
            
            if self.isClose(i):
                if len(stack) == 0:
                    return False

                if self.isCorrespondingClose(stack[-1], i):
                    stack.pop()
                else:
                    return False
        
        # is valid
        if len(stack) == 0:
            return True 
        else:
            return False




    def isOpen(self, s: str) -> bool:
        return s == '(' or s == '{' or s == '['

    def isClose(self, s: str) -> bool:
        return s == ')' or s == '}' or s == ']'

    def isCorrespondingClose(self, stackTop:str, b: str) -> bool:
        return (stackTop == '(' and b == ')') or (stackTop == '{' and b == '}') or (stackTop == '[' and b == ']')
