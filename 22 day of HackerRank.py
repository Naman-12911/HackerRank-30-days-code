#Task
#The height of a binary search tree is the number of edges between the tree's
#root and its furthest leaf. You are given a pointer, ,
#pointing to the root of a binary search tree. Complete
#the getHeight function provided in your editor so that it returns the height of the binary search tree.


#Sample Input

#7
#3
#5
#2
#1
#4
#6
#7
#Sample Output

#3
#Explanation

#The input forms the following BST:

#BST.png

#The longest root-to-leaf path is shown below:


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if not root :
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1       

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
