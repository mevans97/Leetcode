'''
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # keep track of the current node and previous node
        # make the current node point to the previous node
        # set the previous node to the current node
        # and the current node to the next of current node (before pointer change)
        # previous will store the last node (new head)
        # time O(n) space O(1)
        
        prev,curr = None,head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev #we return prev because curr will eventually become null being the last node always points to null. this will end the while loop however returning curr at this point will return a null value. prev will have the value of the last node as a head 
'''
Success
Details 
Runtime: 43 ms, faster than 49.81% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.9 MB, less than 44.61% of Python3 online submissions for Reverse Linked List.
'''
