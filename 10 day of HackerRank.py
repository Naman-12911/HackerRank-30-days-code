#Task
#Given a base- integer, , convert it to binary (base-).
#Then find and print the base- integer denoting
#the maximum number of consecutive 's in 's binary representation.

#Input Format

#A single integer, .

#Output Format

#Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

#Sample Input 

#5
#Sample Output 

#1

import sys
n = int(input("input a number that you want ").strip())
current_consecutive_1s = 0
max_consecutive_1s = 1
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_1s += 1
        if current_consecutive_1s > current_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
    else:
        current_consecutive_1s = 0
    n = n//2
print(max_consecutive_1s)                 
