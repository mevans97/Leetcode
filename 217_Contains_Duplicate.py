"""
Leetcode Easy Arrays And Hashing Question: 

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

# My Solution :

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicate = False

        numsSet = set(nums)
        if len(numsSet) != len(nums):
            duplicate = True
        
        return duplicate


"""
Successfully Completed In 3.5 Minutes
Runtime: 426 ms, faster than 82.44% of Python online submissions for Contains Duplicate.
Memory Usage: 29.1 MB, less than 57.86% of Python online submissions for Contains Duplicate.
Neetcode Explanation : https://www.youtube.com/watch?v=3OamzN90kPg
"""
