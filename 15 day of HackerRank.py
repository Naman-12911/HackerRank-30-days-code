#Task
#Complete the insert function in your editor so that it creates a new Node
#(pass  as the Node constructor argument) and inserts it at the tail of the linked list
#referenced by the  parameter. Once the new node is added, return the reference to the  node has  parameters: a pointer to a Node named , and an integer value, .


#Sample Input

#The following input is handled for you by the locked code in the editor:
#The first line contains T, the number of test cases.
#The  subsequent lines of test cases each contain an integer to be inserted at the list's tail.

#4
#2
#3
#4
#1
#Sample Output

#The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:

#2 3 4 1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def insert(self,head,data):
        newNode = Node(data)

        if not head:

           return newNode
        current = head
        while current.next:

            current = current.next
        current.next = newNode
        return head     
    #Complete this method

    

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
