'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=list1,list2
        listholder = ListNode(val=0,next=None)
        newlist = listholder
        
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    newlist.next = curr1
                    curr1=curr1.next
                elif curr1.val > curr2.val:
                    newlist.next=curr2
                    curr2=curr2.next
                else :
                    newlist.next = curr1
                    curr1=curr1.next
                    newlist = newlist.next
                    newlist.next=curr2
                    curr2=curr2.next
            elif curr1 and not curr2:
                newlist.next = curr1
                curr1=curr1.next
            else:
                newlist.next=curr2
                curr2=curr2.next
                
            newlist = newlist.next
        return listholder.next

'''
Success
Details 
Runtime: 41 ms, faster than 72.97% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 16.4 MB, less than 16.95% of Python3 online submissions for Merge Two Sorted Lists.
'''
