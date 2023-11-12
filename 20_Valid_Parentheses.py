'''
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
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for c in s: 
            if len(stack) == 0:
                stack.append(c)
            else:
                if c in closeToOpen:
                    if stack[-1]==closeToOpen[c]:
                        stack.pop()
                    else:
                        return False
                if c not in closeToOpen:
                    stack.append(c)
                
        if len(stack) == 0:
            return True
        else:
            return False  

'''
Success
Details 
Runtime: 14 ms, faster than 66.93% of Python online submissions for Valid Parentheses.
Memory Usage: 13.3 MB, less than 49.96% of Python online submissions for Valid Parentheses.
'''
