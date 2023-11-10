"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str=''
        
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        
        x = 0
        y = len(new_str) - 1
        
        for i in range(len(new_str)-1):
            if x != y:
                if new_str[x] != new_str[y]:
                    return False
                x+=1
                y-=1
        return True

"""
Success
Details 
Runtime: 295 ms, faster than 21.25% of Python online submissions for Valid Palindrome.
Memory Usage: 16.3 MB, less than 8.53% of Python online submissions for Valid Palindrome.

Neetcode video Solution : https://youtu.be/jJXJ16kPFWg?si=ky7c3E6eW3wZWmAo
"""
