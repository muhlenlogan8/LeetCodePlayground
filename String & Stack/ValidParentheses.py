"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:

* 1 <= s.length <= 104
* s consists of parentheses only '()[]{}'.
"""

"""
:type s: str
:rtype: bool
"""

# Stack with if-else statements O(n)
class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ')' and stack[-1] != '(':
                    return False
                if s[i] == ']' and stack[-1] != '[':
                    return False
                if s[i] == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return len(stack) == 0
    
# More efficient solution
"""
Create a stack
Create a dictionary with the closing brackets as keys and the opening brackets as values
Iterate through the string
If the character is a closing bracket, check if the stack is empty or the last element in the stack is not the corresponding opening bracket
If it is, return False
If it is not, pop the last element from the stack
If the stack is empty at the end, return True
"""
class Solution2(object):
    def isValid(self, s):
        stack = []
        bracketMap = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in bracketMap:
                if not stack or bracketMap[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack

# Test cases
s1 = "()"
sol = Solution()
print(sol.isValid(s1)) # Expected: True

s2 = "()[]{}"
sol = Solution()
print(sol.isValid(s2)) # Expected: True

s3 = "(]"
sol = Solution()
print(sol.isValid(s3)) # Expected: False

s4 = "([])"
sol = Solution()
print(sol.isValid(s4)) # Expected: True