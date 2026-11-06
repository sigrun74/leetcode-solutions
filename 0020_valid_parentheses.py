# 20. Valid Parentheses
# Approach: stack. Push opening brackets; on a closing bracket, pop the latest
# opening one and check it matches. Valid only if the stack is empty at the end.
# Time: O(n)   Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if pairs[ch] != top:
                    return False

        return len(stack) == 0
