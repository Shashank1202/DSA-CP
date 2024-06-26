'''Problem Link:|
https://leetcode.com/problems/middle-of-the-linked-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow=head
        fast=head
        while fast and fast.next and slow:
            fast=fast.next.next
            slow=slow.next
        return slow
        
