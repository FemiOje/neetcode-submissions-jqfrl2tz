class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        for bracket in s:
            if bracket in closeToOpen:
                if not stack or stack[-1] != closeToOpen[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        return not stack
        