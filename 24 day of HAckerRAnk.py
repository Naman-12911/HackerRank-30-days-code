#Task
#A Node class is provided for you in the editor.
#A Node object has an integer data field, , and a Node instance pointer, ,
#pointing to another node (i.e.: the next node in a list).

#A removeDuplicates function is declared in your editor,
#which takes a pointer to the  node of a linked list as a parameter.
#Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.


#Sample Input

#6
#1
#2
#2
#3
#3
#4

#Sample Output

#1 2 3 4

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if not head:

           return None
        current = head
        while current.next:
           if current.next.data == current.data:


            current.next = current.next.next
           else:



            current = current.next
        return head

       

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
