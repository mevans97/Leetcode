'''
Medium

17624

526

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        key = {}
        
        for s in strs:
            if ''.join(sorted(s)) in key:
                key[''.join(sorted(s))].append(s)
            else:
                key[''.join(sorted(s))] = [s]
        
        
        return key.values()

'''
Success
Details 
Runtime: 89 ms, faster than 92.76% of Python3 online submissions for Group Anagrams.
Memory Usage: 20 MB, less than 58.93% of Python3 online submissions for Group Anagrams.
'''
