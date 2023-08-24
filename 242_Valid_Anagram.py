"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

My Solution:
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        
        for i in s:
            if i in sDict:
                sDict[i] +=1
            else:
                sDict[i] = 1
        
        for j in t:
            if j in tDict:
                tDict[j] +=1
            else:
                tDict[j] = 1
                
        if sDict == tDict:
            return True
        else:
            return False
"""
Successfully solved in 5.5 minutes
Runtime: 26 ms, faster than 91.92% of Python online submissions for Valid Anagram.
Memory Usage: 13.8 MB, less than 73.98% of Python online submissions for Valid Anagram.
neetcode explanation: https://www.youtube.com/watch?v=9UtInBqnCgA
"""
