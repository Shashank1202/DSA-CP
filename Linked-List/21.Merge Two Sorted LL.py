'''Problem Link:|

https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy

        while list1 is not None and list2 is not None:
            if list1.val <=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
        
            temp=temp.next
        if list1 is not None:
            temp.next=list1
        else:
            temp.next=list2

        return dummy.next
        
