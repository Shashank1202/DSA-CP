'''problem link
https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
'''
class Solution():
  def Ceil(self, root, val):
    if root == None:
      return -1

    if root.val<val:
      root= root.right

      val=self.Ceil(root.right, val)
    else:
      val= self.Ceil(root.left, val)


  
