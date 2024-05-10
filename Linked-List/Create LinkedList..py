class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    

def printList(head):
    temp=head
    while temp is not None:
        print(temp.val, end=" ")
        temp=temp.next
    print()
        
    
    
head=ListNode(1)
head.next=ListNode(3)
head.next.next=ListNode(5)
head.next.next.next=ListNode(7)

print("LinkedList")
printList(head)
