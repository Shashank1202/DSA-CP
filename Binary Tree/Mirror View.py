'''Problem Link
https://leetcode.com/problems/symmetric-tree/description/
'''
class Node:
    def __init__(self, val):
        self.val= val
        self.left= None
        self.right= None

class Solution:
    def Mirror(self, root)->bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self,leftroot, rightroot):
        if leftroot== None and rightroot== None:
            return True
        if leftroot==None or rightroot==None:
            return False
        if leftroot.val!=rightroot.val:
            return False
        return self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)

root= Node(1)
root.left= Node(20)
root.right= Node(20)
root.left.left= Node(23)
root.right.right=Node(23)

sol= Solution()
if sol.Mirror(root):
    print("True")
else:
    print("false")
