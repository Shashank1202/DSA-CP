'''problem Link:|
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        slow=head
        fast=head

        for i in range(n):
            fast=fast.next

        if fast is None:
            return head.next
        
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
            


        delNode=slow.next
        slow.next=slow.next.next
        delNode=None
        return head
        
