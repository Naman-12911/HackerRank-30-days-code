#Task
#Read a string, , and print its integer value; if  cannot be converted to an integer, print Bad String


#Print the parsed integer value of , or Bad String if  cannot be converted to an integer.

#Sample Input 0

#3
#Sample Output 0

#3
#Sample Input 1

#za
#Sample Output 1

#Bad String

import sys


S = input().strip()
try:
    integer_value = int(S)
    print(integer_value)
except ValueError:
    print("Bad String")
