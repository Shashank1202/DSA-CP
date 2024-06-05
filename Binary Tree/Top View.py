'''Problem Link:
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''


#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        ans= []
        if not root:
            return ans
        
        mpp= {}
        q= deque([(root, 0)])
        while q:
            node, line= q.popleft()
            if line not in mpp:
                mpp[line]= node.data
            
            if node.left:
                q.append((node.left, line-1))
            if node.right:
                q.append((node.right, line+1))
            
        for value in sorted(mpp.items()):
            ans.append(value[1])
        return ans
