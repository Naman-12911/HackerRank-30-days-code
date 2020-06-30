#Write the following declarations and implementations:

#Two instance variables: one for your , and one for your .
#A void pushCharacter(char ch) method that pushes a character onto a stack.
#A void enqueueCharacter(char ch) method that enqueues a character in the  instance variable.
#A char popCharacter() method that pops and returns the character at the top of the  instance variable.
#A char dequeueCharacter() method that dequeues and returns the first character in the  instance variable.

#Sample Input

#racecar

#Sample Output

#The word, racecar, is a palindrome.

from collections import deque
class Solution:
    # Write your code 
    def __init__(self):
        self.queue = deque()
        self.stack = list()

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()  

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
